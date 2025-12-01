"""Callback Event Functions.

This module provides functions for registering and managing callback events.
"""

import ctypes
from typing import Any, Callable, Optional

from ..core.exceptions import CANapeCallbackError
from ..core.handle import Handle


class CallbackEvents:
    """Callback Events interface.

    This class provides methods for registering and managing callback events.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize callback events interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._assign_types()

    def _assign_types(self) -> None:
        """Assign DLL function types."""
        if hasattr(self.dll, "Asap3RegisterCallBack"):
            # Note: Callback function type is complex - using c_void_p for now
            self.dll.Asap3RegisterCallBack.argtypes = (
                ctypes.c_void_p,
                ctypes.c_int,  # ASAP3_EVENT_CODE
                ctypes.c_void_p,  # Callback function
                ctypes.c_ulong,  # Private data
            )
            self.dll.Asap3RegisterCallBack.restype = ctypes.c_bool

    def Asap3RegisterCallBack(
        self,
        event_id: int,
        callback_function: Optional[Callable] = None,
        private_data: int = 0,
    ) -> bool:
        """Register a callback function for an event.

        Parameters
        ----------
        event_id : int
            Event code (see ASAP3_EVENT_CODE enum).
        callback_function : Optional[Callable], optional
            Callback function to call on event, by default None.
        private_data : int, optional
            Private data to pass to callback, by default 0.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeCallbackError
            If callback registration fails.
        """
        if not hasattr(self.dll, "Asap3RegisterCallBack"):
            raise CANapeCallbackError(
                "Asap3RegisterCallBack not available in this DLL version"
            )

        # Convert callback to ctypes function pointer if provided
        callback_ptr = None
        if callback_function:
            # Define callback type based on event type
            # This is a simplified version - actual implementation would
            # need to handle different callback signatures per event type
            CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_ulong)
            callback_ptr = CALLBACK(callback_function)

        result = self.dll.Asap3RegisterCallBack(
            self.handle.handle,
            ctypes.c_int(event_id),
            callback_ptr,
            ctypes.c_ulong(private_data),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeCallbackError(
                f"Failed to register callback (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def _get_last_error(self) -> int:
        """Get last error code from CANape.

        Returns
        -------
        int
            Error code.
        """
        if hasattr(self.dll, "Asap3GetLastError"):
            return self.dll.Asap3GetLastError(self.handle.handle)
        return 0

