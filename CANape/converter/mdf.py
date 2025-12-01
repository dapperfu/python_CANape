"""MDF Converter Functions.

This module provides functions for MDF file conversion.
"""

import ctypes
from typing import Any, List, Optional

from ..core.exceptions import CANapeError
from ..core.handle import Handle
from ..core.structs import TConverterInfo


class MDFConverter:
    """MDF Converter interface.

    This class provides methods for MDF file conversion.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize MDF converter interface.

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
        if hasattr(self.dll, "Asap3MDFConverterCount"):
            self.dll.Asap3MDFConverterCount.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3MDFConverterCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3MDFConverterInfo"):
            self.dll.Asap3MDFConverterInfo.argtypes = (
                ctypes.c_void_p,
                ctypes.c_int,
                ctypes.POINTER(TConverterInfo),
            )
            self.dll.Asap3MDFConverterInfo.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3MDFConvert"):
            self.dll.Asap3MDFConvert.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_bool,
            )
            self.dll.Asap3MDFConvert.restype = ctypes.c_bool

    def Asap3MDFConverterCount(self) -> int:
        """Get count of installed MDF converters.

        Returns
        -------
        int
            Count of installed MDF converters.

        Raises
        ------
        CANapeError
            If converter count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3MDFConverterCount"):
            raise CANapeError(
                "Asap3MDFConverterCount not available in this DLL version"
            )

        count = ctypes.c_int()
        result = self.dll.Asap3MDFConverterCount(
            self.handle.handle, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to get converter count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3MDFConverterInfo(
        self, index: int
    ) -> Optional[TConverterInfo]:
        """Get information about a specific MDF converter.

        Parameters
        ----------
        index : int
            Index of the converter.

        Returns
        -------
        Optional[TConverterInfo]
            Converter information structure, or None if failed.

        Raises
        ------
        CANapeError
            If converter info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3MDFConverterInfo"):
            raise CANapeError(
                "Asap3MDFConverterInfo not available in this DLL version"
            )

        item = TConverterInfo()
        result = self.dll.Asap3MDFConverterInfo(
            self.handle.handle, ctypes.c_int(index), ctypes.byref(item)
        )
        if result:
            return item
        return None

    def Asap3MDFConvert(
        self,
        converter_id: str,
        mdf_filename: str,
        dest_filename: str,
        overwrite: bool = False,
    ) -> bool:
        """Convert an MDF file into a different format.

        Converts an existing MDF file into a different export format and saves
        it with the given destination filename.

        Parameters
        ----------
        converter_id : str
            Converter ID of an existing CANape MDF converter. The converter
            IDs can be determined with Asap3MDFConverterInfo().
        mdf_filename : str
            Name of the source MDF file.
        dest_filename : str
            Name of the destination file.
        overwrite : bool, optional
            Overwrite existing destination file, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If conversion fails.
        """
        if not hasattr(self.dll, "Asap3MDFConvert"):
            raise CANapeError(
                "Asap3MDFConvert not available in this DLL version"
            )

        c_converter_id = ctypes.c_char_p(converter_id.encode("UTF-8"))
        c_mdf_filename = ctypes.c_char_p(mdf_filename.encode("UTF-8"))
        c_dest_filename = ctypes.c_char_p(dest_filename.encode("UTF-8"))
        c_overwrite = ctypes.c_bool(overwrite)

        result = self.dll.Asap3MDFConvert(
            self.handle.handle,
            c_converter_id,
            c_mdf_filename,
            c_dest_filename,
            c_overwrite,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to convert MDF file (Error Code: {error_code})",
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

