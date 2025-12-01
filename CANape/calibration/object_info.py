"""Calibration Object Info Functions.

This module provides functions for getting information about calibration objects.
"""

import ctypes
from typing import Any, Optional, Tuple

from ..core.enums import TValueType
from ..core.exceptions import CANapeCalibrationError
from ..core.handle import Handle
from ..core.structs import TLayoutCoeffs
from ..core.types import TModulHdl


class CalibrationObjectInfo:
    """Calibration Object Info interface.

    This class provides methods for getting calibration object information.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize calibration object info interface.

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
        if hasattr(self.dll, "Asap3CalibrationObjectInfo"):
            self.dll.Asap3CalibrationObjectInfo.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_short),
                ctypes.POINTER(ctypes.c_short),
            )
            self.dll.Asap3CalibrationObjectInfo.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3CalibrationObjectInfoEx"):
            self.dll.Asap3CalibrationObjectInfoEx.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_short),
                ctypes.POINTER(ctypes.c_short),
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3CalibrationObjectInfoEx.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3CalibrationObjectRecordInfo"):
            self.dll.Asap3CalibrationObjectRecordInfo.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(TLayoutCoeffs),
                ctypes.POINTER(ctypes.c_short),
                ctypes.POINTER(ctypes.c_short),
            )
            self.dll.Asap3CalibrationObjectRecordInfo.restype = ctypes.c_bool

    def Asap3CalibrationObjectInfo(
        self, module: TModulHdl, calibration_object_name: str
    ) -> Optional[Tuple[int, int]]:
        """Get dimensions of a calibration object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object.

        Returns
        -------
        Optional[Tuple[int, int]]
            Tuple of (x_dimension, y_dimension), or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If object info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3CalibrationObjectInfo"):
            raise CANapeCalibrationError(
                "Asap3CalibrationObjectInfo not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            calibration_object_name.encode("UTF-8")
        )
        x_dim = ctypes.c_short()
        y_dim = ctypes.c_short()

        result = self.dll.Asap3CalibrationObjectInfo(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.byref(x_dim),
            ctypes.byref(y_dim),
        )
        if result:
            return (x_dim.value, y_dim.value)
        return None

    def Asap3CalibrationObjectInfoEx(
        self, module: TModulHdl, calibration_object_name: str
    ) -> Optional[Tuple[int, int, int]]:
        """Get dimensions and type of a calibration object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object.

        Returns
        -------
        Optional[Tuple[int, int, int]]
            Tuple of (x_dimension, y_dimension, type), or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If object info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3CalibrationObjectInfoEx"):
            raise CANapeCalibrationError(
                "Asap3CalibrationObjectInfoEx not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            calibration_object_name.encode("UTF-8")
        )
        x_dim = ctypes.c_short()
        y_dim = ctypes.c_short()
        obj_type = ctypes.c_int()

        result = self.dll.Asap3CalibrationObjectInfoEx(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.byref(x_dim),
            ctypes.byref(y_dim),
            ctypes.byref(obj_type),
        )
        if result:
            return (x_dim.value, y_dim.value, obj_type.value)
        return None

    def Asap3CalibrationObjectRecordInfo(
        self, module: TModulHdl, calibration_object_name: str
    ) -> Optional[Tuple[TLayoutCoeffs, int, int]]:
        """Get layout information about a calibration object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object.

        Returns
        -------
        Optional[Tuple[TLayoutCoeffs, int, int]]
            Tuple of (layout_coeffs, x_dimension, y_dimension), or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If record info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3CalibrationObjectRecordInfo"):
            raise CANapeCalibrationError(
                "Asap3CalibrationObjectRecordInfo not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            calibration_object_name.encode("UTF-8")
        )
        coeffs = TLayoutCoeffs()
        x_dim = ctypes.c_short()
        y_dim = ctypes.c_short()

        result = self.dll.Asap3CalibrationObjectRecordInfo(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.byref(coeffs),
            ctypes.byref(x_dim),
            ctypes.byref(y_dim),
        )
        if result:
            return (coeffs, x_dim.value, y_dim.value)
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

