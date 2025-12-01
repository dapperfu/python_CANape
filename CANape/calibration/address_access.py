"""Calibration Address Access Functions.

This module provides functions for reading and writing calibration data
by memory address (special access functions).
"""

import ctypes
from typing import Any

from ..core.exceptions import CANapeCalibrationError
from ..core.handle import Handle
from ..core.types import TModulHdl


class CalibrationAddressAccess:
    """Calibration Address Access interface.

    This class provides methods for accessing calibration RAM by address.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize calibration address access interface.

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
        if hasattr(self.dll, "Asap3ReadByAddress"):
            self.dll.Asap3ReadByAddress.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ulong,
                ctypes.c_ubyte,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ubyte),
            )
            self.dll.Asap3ReadByAddress.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3WriteByAddress"):
            self.dll.Asap3WriteByAddress.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ulong,
                ctypes.c_ubyte,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ubyte),
            )
            self.dll.Asap3WriteByAddress.restype = ctypes.c_bool

    def Asap3ReadByAddress(
        self,
        module: TModulHdl,
        address: int,
        address_ext: int = 0,
        size: int = 1,
    ) -> bytes:
        """Read ECU data from calibration RAM by address.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        address : int
            Address to read.
        address_ext : int, optional
            Used by special multiprocessor ECU. If not required set to 0,
            by default 0.
        size : int, optional
            Size of data to read in bytes, by default 1.

        Returns
        -------
        bytes
            Data read from the address.

        Raises
        ------
        CANapeCalibrationError
            If read operation fails.
        """
        if not hasattr(self.dll, "Asap3ReadByAddress"):
            raise CANapeCalibrationError(
                "Asap3ReadByAddress not available in this DLL version"
            )

        c_address = ctypes.c_ulong(address)
        c_address_ext = ctypes.c_ubyte(address_ext)
        c_size = ctypes.c_ulong(size)
        data = (ctypes.c_ubyte * size)()

        result = self.dll.Asap3ReadByAddress(
            self.handle.handle,
            module,
            c_address,
            c_address_ext,
            c_size,
            data,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeCalibrationError(
                f"Failed to read by address (Error Code: {error_code})",
                error_code=error_code,
            )
        return bytes(data)

    def Asap3WriteByAddress(
        self,
        module: TModulHdl,
        address: int,
        data: bytes,
        address_ext: int = 0,
    ) -> bool:
        """Write ECU data to calibration RAM by address.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        address : int
            Address to write.
        data : bytes
            Data to write.
        address_ext : int, optional
            Used by special multiprocessor ECU. If not required set to 0,
            by default 0.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeCalibrationError
            If write operation fails.
        """
        if not hasattr(self.dll, "Asap3WriteByAddress"):
            raise CANapeCalibrationError(
                "Asap3WriteByAddress not available in this DLL version"
            )

        c_address = ctypes.c_ulong(address)
        c_address_ext = ctypes.c_ubyte(address_ext)
        c_size = ctypes.c_ulong(len(data))
        c_data = (ctypes.c_ubyte * len(data)).from_buffer_copy(data)

        result = self.dll.Asap3WriteByAddress(
            self.handle.handle,
            module,
            c_address,
            c_address_ext,
            c_size,
            c_data,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeCalibrationError(
                f"Failed to write by address (Error Code: {error_code})",
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

