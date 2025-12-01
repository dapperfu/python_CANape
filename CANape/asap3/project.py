"""ASAP3 Project Functions.

This module provides functions for project directory and application name management.
"""

import ctypes
import os
from typing import Any, Optional

from ..core.exceptions import CANapeError
from ..core.handle import Handle
from ..core.type_assignments import assign_project_functions


class ASAP3Project:
    """ASAP3 Project interface.

    This class provides methods for project directory and application name management.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize ASAP3 project interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        # Assign function types
        assign_project_functions(self.dll)

        # Assign application name function types if available
        if hasattr(self.dll, "Asap3SetApplicationName"):
            self.dll.Asap3SetApplicationName.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3SetApplicationName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetApplicationName"):
            self.dll.Asap3GetApplicationName.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3GetApplicationName.restype = ctypes.c_bool

    def Asap3GetProjectDirectory(self) -> Optional[str]:
        """Get the current project directory.

        Returns
        -------
        Optional[str]
            Current project directory as absolute path, or None if failed.

        Raises
        ------
        CANapeError
            If project directory cannot be retrieved.
        """
        # First call to get required buffer size (pass NULL for directory)
        size = ctypes.c_ulong(0)

        # Query size
        result = self.dll.Asap3GetProjectDirectory(self.handle.handle, None, ctypes.byref(size))
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to get project directory size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get directory
        buffer_size = size.value + 1  # Add 1 for null terminator
        directory = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetProjectDirectory(self.handle.handle, directory, ctypes.byref(size))
        if result:
            return os.path.abspath(directory.value.decode("UTF-8"))
        return None

    def Asap3SetApplicationName(self, app_name: str) -> bool:
        """Change the application name used to select logical CAN channel names.

        Parameters
        ----------
        app_name : str
            New application name (e.g., "namexxCAN2").

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If application name cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetApplicationName"):
            raise CANapeError("Asap3SetApplicationName not available in this DLL version")

        c_app_name = ctypes.c_char_p(app_name.encode("UTF-8"))
        result = self.dll.Asap3SetApplicationName(self.handle.handle, c_app_name)
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to set application name (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetApplicationName(self) -> Optional[str]:
        """Get the current application name used to select logical CAN channel names.

        Returns
        -------
        Optional[str]
            Application name, or None if failed.

        Raises
        ------
        CANapeError
            If application name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetApplicationName"):
            raise CANapeError("Asap3GetApplicationName not available in this DLL version")

        # First call to get required buffer size (pass NULL for name)
        size = ctypes.c_ulong(0)

        # Query size
        result = self.dll.Asap3GetApplicationName(self.handle.handle, None, ctypes.byref(size))
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to get application name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = size.value + 1  # Add 1 for null terminator
        name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetApplicationName(self.handle.handle, name, ctypes.byref(size))
        if result:
            return name.value.decode("UTF-8")
        return None

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
