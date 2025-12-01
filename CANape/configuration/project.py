"""Configuration Functions.

This module provides functions for loading CNA files and managing project parameters.
"""

import ctypes
from typing import Any, Optional

from ..core.exceptions import CANapeConfigurationError
from ..core.handle import Handle


class ProjectConfiguration:
    """Project Configuration interface.

    This class provides methods for managing project configuration.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize project configuration interface.

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
        if hasattr(self.dll, "Asap3LoadCNAFile"):
            self.dll.Asap3LoadCNAFile.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3LoadCNAFile.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetCNAFilename"):
            self.dll.Asap3GetCNAFilename.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3GetCNAFilename.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetCanapeProjectParam"):
            self.dll.Asap3GetCanapeProjectParam.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3GetCanapeProjectParam.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SetCanapeProjectParam"):
            self.dll.Asap3SetCanapeProjectParam.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3SetCanapeProjectParam.restype = ctypes.c_bool

    def Asap3LoadCNAFile(self, config_file_name: str) -> bool:
        """Load a CNA configuration file.

        Parameters
        ----------
        config_file_name : str
            Filename of the CNA configuration file.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeConfigurationError
            If CNA file cannot be loaded.
        """
        if not hasattr(self.dll, "Asap3LoadCNAFile"):
            raise CANapeConfigurationError(
                "Asap3LoadCNAFile not available in this DLL version"
            )

        c_file = ctypes.c_char_p(config_file_name.encode("UTF-8"))
        result = self.dll.Asap3LoadCNAFile(self.handle.handle, c_file)
        if not result:
            error_code = self._get_last_error()
            raise CANapeConfigurationError(
                f"Failed to load CNA file (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetCNAFilename(self, max_size: int = 512) -> Optional[str]:
        """Get the current CNA filename.

        Parameters
        ----------
        max_size : int, optional
            Maximum size of filename buffer, by default 512.

        Returns
        -------
        Optional[str]
            CNA filename, or None if failed.

        Raises
        ------
        CANapeConfigurationError
            If CNA filename cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetCNAFilename"):
            raise CANapeConfigurationError(
                "Asap3GetCNAFilename not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_uint(0)
        filename = None

        # Query size
        result = self.dll.Asap3GetCNAFilename(
            self.handle.handle, filename, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeConfigurationError(
                f"Failed to get CNA filename size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get filename
        buffer_size = min(size.value + 1, max_size)
        filename = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetCNAFilename(
            self.handle.handle, filename, ctypes.byref(size)
        )
        if result:
            return filename.value.decode("UTF-8")
        return None

    def Asap3GetCanapeProjectParam(
        self, section: str, param: str, max_size: int = 256
    ) -> Optional[str]:
        """Get a CANape project parameter.

        Parameters
        ----------
        section : str
            Section name.
        param : str
            Parameter name.
        max_size : int, optional
            Maximum size of value buffer, by default 256.

        Returns
        -------
        Optional[str]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeConfigurationError
            If parameter cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetCanapeProjectParam"):
            raise CANapeConfigurationError(
                "Asap3GetCanapeProjectParam not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_uint(0)
        c_section = ctypes.c_char_p(section.encode("UTF-8"))
        c_param = ctypes.c_char_p(param.encode("UTF-8"))
        value = None

        # Query size
        result = self.dll.Asap3GetCanapeProjectParam(
            self.handle.handle, c_section, c_param, value, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeConfigurationError(
                f"Failed to get project parameter size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get value
        buffer_size = min(size.value + 1, max_size)
        value = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetCanapeProjectParam(
            self.handle.handle, c_section, c_param, value, ctypes.byref(size)
        )
        if result:
            return value.value.decode("UTF-8")
        return None

    def Asap3SetCanapeProjectParam(
        self, section: str, param: str, value: str
    ) -> bool:
        """Set a CANape project parameter.

        Parameters
        ----------
        section : str
            Section name.
        param : str
            Parameter name.
        value : str
            Parameter value.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeConfigurationError
            If parameter cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetCanapeProjectParam"):
            raise CANapeConfigurationError(
                "Asap3SetCanapeProjectParam not available in this DLL version"
            )

        c_section = ctypes.c_char_p(section.encode("UTF-8"))
        c_param = ctypes.c_char_p(param.encode("UTF-8"))
        c_value = ctypes.c_char_p(value.encode("UTF-8"))

        result = self.dll.Asap3SetCanapeProjectParam(
            self.handle.handle, c_section, c_param, c_value
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeConfigurationError(
                f"Failed to set project parameter (Error Code: {error_code})",
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

