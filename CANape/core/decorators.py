"""Decorators for CANape API functions.

This module provides Python decorators for common patterns in CANape API usage,
including error handling, validation, retry logic, and logging.
"""

import functools
import logging
from typing import Any, Callable, Optional, TypeVar, cast

from .error_decoder import get_error_message
from .exceptions import CANapeError, CANapeHandleError
from .handle import Handle

# Type variable for generic function signatures
F = TypeVar("F", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


def requires_initialization(func: F) -> F:
    """Decorator to ensure CANape is initialized before calling a function.

    Checks that the handle is valid before executing the function.

    Parameters
    ----------
    func : F
        Function to decorate. Must have 'self' with 'handle' attribute.

    Returns
    -------
    F
        Decorated function that checks initialization.

    Raises
    ------
    CANapeHandleError
        If CANape is not initialized (handle is invalid).

    Examples
    --------
    >>> class MyClass:
    ...     def __init__(self):
    ...         self.handle = Handle()
    ...
    ...     @requires_initialization
    ...     def my_method(self):
    ...         return "success"
    """
    functools.wraps(func)

    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper function that checks initialization."""
        if not hasattr(self, "handle"):
            raise CANapeHandleError(
                "Object does not have a handle attribute",
                error_code=None,
            )

        handle = self.handle
        if isinstance(handle, Handle) and not handle.valid:
            raise CANapeHandleError(
                "CANape is not initialized. Call init() or start() first.",
                error_code=None,
            )

        return func(self, *args, **kwargs)

    return cast(F, wrapper)


def requires_module(module_param: str = "module") -> Callable[[F], F]:
    """Decorator to validate module handle exists.

    Parameters
    ----------
    module_param : str, optional
        Name of the parameter that contains the module handle, by default "module".

    Returns
    -------
    Callable[[F], F]
        Decorator function.

    Raises
    ------
    CANapeModuleError
        If module handle is None or invalid.

    Examples
    --------
    >>> @requires_module("module")
    ... def my_function(self, module):
    ...     return "success"
    """
    def decorator(func: F) -> F:
        functools.wraps(func)

        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            """Wrapper function that validates module."""
            from .exceptions import CANapeModuleError
            from .types import TModulHdl

            # Get module from args or kwargs
            module = None
            if args:
                # Try to get from positional args (assuming first arg after self)
                try:
                    module = args[0]
                except IndexError:
                    pass

            if module is None and module_param in kwargs:
                module = kwargs[module_param]

            if module is None:
                raise CANapeModuleError(
                    f"Module handle is required for {func.__name__}",
                    error_code=None,
                )

            # Check if module is a valid TModulHdl (has value attribute)
            if not hasattr(module, "value") and module is not None:
                # Might be a valid handle, just check it's not None
                if module is None:
                    raise CANapeModuleError(
                        f"Invalid module handle for {func.__name__}",
                        error_code=None,
                    )

            return func(self, *args, **kwargs)

        return cast(F, wrapper)

    return decorator


def handle_errors(operation: Optional[str] = None) -> Callable[[F], F]:
    """Decorator to convert DLL errors to Python exceptions with decoded messages.

    This decorator automatically:
    1. Catches DLL function failures (returns False)
    2. Gets the error code via Asap3GetLastError
    3. Decodes the error code to a Pythonic message
    4. Raises the appropriate exception type

    Parameters
    ----------
    operation : Optional[str], optional
        Name of the operation for error messages (e.g., "start data acquisition").
        If None, will use the function name, by default None.

    Returns
    -------
    Callable[[F], F]
        Decorator function.

    Examples
    --------
    >>> class MyClass:
    ...     def __init__(self):
    ...         self.error = error_handling_instance
    ...
    ...     @handle_errors("start acquisition")
    ...     def start(self):
    ...         result = self.dll.Asap3StartDataAcquisition(self.handle.handle)
    ...         if not result:
    ...             # Error will be automatically handled by decorator
    ...             pass
    ...         return result
    """
    def decorator(func: F) -> F:
        functools.wraps(func)

        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            """Wrapper function that handles errors."""
            # Execute the function
            try:
                result = func(self, *args, **kwargs)
            except Exception:
                # If function raises an exception, let it propagate
                # (it might already be a CANapeError with decoded message)
                raise

            # Check if result indicates failure (False for bool returns)
            # Only check for False, not None, as None might be a valid return value
            if result is False:
                # Get error code
                error_code = 0
                error_handling = None

                # Try to get error handling instance
                if hasattr(self, "error"):
                    error_handling = self.error
                    if hasattr(error_handling, "Asap3GetLastError"):
                        try:
                            error_code = error_handling.Asap3GetLastError()
                        except Exception:
                            pass

                # If no error code found, try direct DLL access
                if error_code == 0 and hasattr(self, "dll"):
                    if hasattr(self.dll, "Asap3GetLastError"):
                        try:
                            if hasattr(self, "handle"):
                                error_code = self.dll.Asap3GetLastError(
                                    self.handle.handle
                                )
                        except Exception:
                            pass

                # Get operation name
                op_name = operation or func.__name__.replace("Asap3", "").replace(
                    "_", " "
                )

                # Decode error and raise appropriate exception
                message, exc_type = get_error_message(
                    error_code, op_name, error_handling
                )
                raise exc_type(message, error_code=error_code)

            return result

        return cast(F, wrapper)

    return decorator


def validate_types(func: F) -> F:
    """Decorator to validate function parameter types.

    Uses function annotations to validate types at runtime.

    Parameters
    ----------
    func : F
        Function to decorate with type annotations.

    Returns
    -------
    F
        Decorated function with type validation.

    Examples
    --------
    >>> @validate_types
    ... def my_function(self, value: int):
    ...     return value * 2
    """
    functools.wraps(func)

    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Wrapper function that validates types."""
        import inspect

        sig = inspect.signature(func)
        bound_args = sig.bind(self, *args, **kwargs)
        bound_args.apply_defaults()

        # Check parameter types
        for param_name, param_value in bound_args.arguments.items():
            if param_name == "self":
                continue

            param = sig.parameters[param_name]
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(param_value, expected_type):
                    raise TypeError(
                        f"Parameter '{param_name}' must be of type {expected_type.__name__}, "
                        f"got {type(param_value).__name__}"
                    )

        return func(self, *args, **kwargs)

    return cast(F, wrapper)


def retry_on_failure(max_retries: int = 3, delay: float = 0.1) -> Callable[[F], F]:
    """Decorator to automatically retry function on failure.

    Parameters
    ----------
    max_retries : int, optional
        Maximum number of retry attempts, by default 3.
    delay : float, optional
        Delay between retries in seconds, by default 0.1.

    Returns
    -------
    Callable[[F], F]
        Decorator function.

    Examples
    --------
    >>> @retry_on_failure(max_retries=5, delay=0.5)
    ... def my_function(self):
    ...     return self.dll.SomeFunction()
    """
    def decorator(func: F) -> F:
        functools.wraps(func)

        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            """Wrapper function that retries on failure."""
            import time

            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(self, *args, **kwargs)
                except CANapeError as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        logger.debug(
                            f"Attempt {attempt + 1} failed for {func.__name__}, "
                            f"retrying in {delay}s..."
                        )
                        time.sleep(delay)
                    else:
                        logger.warning(
                            f"All {max_retries} attempts failed for {func.__name__}"
                        )

            # All retries failed, raise last exception
            raise last_exception

        return cast(F, wrapper)

    return decorator


def log_operation(level: int = logging.DEBUG) -> Callable[[F], F]:
    """Decorator to log function calls and results.

    Parameters
    ----------
    level : int, optional
        Logging level to use, by default logging.DEBUG.

    Returns
    -------
    Callable[[F], F]
        Decorator function.

    Examples
    --------
    >>> @log_operation(logging.INFO)
    ... def my_function(self, param: str):
    ...     return "result"
    """
    def decorator(func: F) -> F:
        functools.wraps(func)

        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            """Wrapper function that logs operations."""
            logger.log(
                level,
                f"Calling {func.__name__} with args={args}, kwargs={kwargs}",
            )

            try:
                result = func(self, *args, **kwargs)
                logger.log(level, f"{func.__name__} completed successfully")
                return result
            except Exception as e:
                logger.log(
                    level,
                    f"{func.__name__} failed with error: {e}",
                    exc_info=True,
                )
                raise

        return cast(F, wrapper)

    return decorator

