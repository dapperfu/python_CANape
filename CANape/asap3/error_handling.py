"""ASAP3 Error Handling Functions.

This module provides functions for error handling and debugging.
"""

import ctypes
from typing import Any, Optional

from ..core.const import AEC_LAST_ERRCODE
from ..core.exceptions import CANapeError
from ..core.handle import Handle


class ASAP3ErrorHandling:
    """ASAP3 Error Handling interface.

    This class provides methods for error handling and debugging.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize ASAP3 error handling interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle

        # Assign function types if available
        if hasattr(self.dll, "Asap3GetLastError"):
            self.dll.Asap3GetLastError.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3GetLastError.restype = ctypes.c_ushort

        if hasattr(self.dll, "Asap3ErrorText"):
            self.dll.Asap3ErrorText.argtypes = (
                ctypes.c_void_p,
                ctypes.c_ushort,
                ctypes.POINTER(ctypes.c_char_p),
            )
            self.dll.Asap3ErrorText.restype = ctypes.c_bool

    def Asap3GetLastError(self) -> int:
        """Get error information (error code) about the previously executed function call.

        Returns
        -------
        int
            Error number (AEC_* constant).

        Raises
        ------
        CANapeError
            If error retrieval fails.
        """
        if not hasattr(self.dll, "Asap3GetLastError"):
            raise CANapeError(
                "Asap3GetLastError not available in this DLL version"
            )

        error_code = self.dll.Asap3GetLastError(self.handle.handle)
        return error_code

    def Asap3ErrorText(self, error_code: int) -> Optional[str]:
        """Get error text corresponding to the result of Asap3GetLastError().

        Parameters
        ----------
        error_code : int
            Number of error (from Asap3GetLastError()).

        Returns
        -------
        Optional[str]
            Error message, or None if failed.

        Raises
        ------
        CANapeError
            If error text retrieval fails.
        """
        if not hasattr(self.dll, "Asap3ErrorText"):
            raise CANapeError(
                "Asap3ErrorText not available in this DLL version"
            )

        err_msg = ctypes.POINTER(ctypes.c_char_p)()
        result = self.dll.Asap3ErrorText(
            self.handle.handle,
            ctypes.c_ushort(error_code),
            ctypes.byref(err_msg),
        )
        if result and err_msg:
            return err_msg.contents.value.decode("UTF-8")
        return None

    def Asap3PopupDebugWindow(self) -> bool:
        """Pop up the debug window of the MCD-system.

        Troubleshooting function.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If debug window cannot be opened.
        """
        if not hasattr(self.dll, "Asap3PopupDebugWindow"):
            raise CANapeError(
                "Asap3PopupDebugWindow not available in this DLL version"
            )

        if not hasattr(self.dll.Asap3PopupDebugWindow, "argtypes"):
            self.dll.Asap3PopupDebugWindow.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3PopupDebugWindow.restype = ctypes.c_bool

        result = self.dll.Asap3PopupDebugWindow(self.handle.handle)
        if not result:
            error_code = self.Asap3GetLastError()
            raise CANapeError(
                f"Failed to pop up debug window (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3SaveDebugWindow(self, file_name: str) -> bool:
        """Save debug window content to file.

        Troubleshooting function.

        Parameters
        ----------
        file_name : str
            File name where debug window content will be saved.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If debug window cannot be saved.
        """
        if not hasattr(self.dll, "Asap3SaveDebugWindow"):
            raise CANapeError(
                "Asap3SaveDebugWindow not available in this DLL version"
            )

        if not hasattr(self.dll.Asap3SaveDebugWindow, "argtypes"):
            self.dll.Asap3SaveDebugWindow.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3SaveDebugWindow.restype = ctypes.c_bool

        c_file_name = ctypes.c_char_p(file_name.encode("UTF-8"))
        result = self.dll.Asap3SaveDebugWindow(
            self.handle.handle, c_file_name
        )
        if not result:
            error_code = self.Asap3GetLastError()
            raise CANapeError(
                f"Failed to save debug window (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

