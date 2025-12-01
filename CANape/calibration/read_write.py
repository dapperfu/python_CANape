"""Calibration Read/Write Functions.

This module provides functions for reading and writing calibration objects
using record layout information from ASAP2.
"""

import ctypes
from typing import TYPE_CHECKING, Any, Optional

from ..core.exceptions import CANapeCalibrationError
from ..core.handle import Handle
from ..core.types import TModulHdl

# Note: TCalibrationObjectValue and TCalibrationObjectValueEx are complex unions
# that need to be properly defined. Using ctypes.Structure as placeholder.
# TODO: Implement proper union structures matching CANapAPI.h definitions
if TYPE_CHECKING:
    TCalibrationObjectValue = Any
    TCalibrationObjectValueEx = Any
else:
    # Placeholder structures - these are actually complex unions in the C API
    class TCalibrationObjectValue(ctypes.Structure):
        _fields_ = [("type", ctypes.c_int)]

    class TCalibrationObjectValueEx(ctypes.Structure):
        _fields_ = [("type", ctypes.c_int)]


class CalibrationReadWrite:
    """Calibration Read/Write interface.

    This class provides methods for reading and writing calibration objects.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize calibration read/write interface.

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
        if hasattr(self.dll, "Asap3ReadCalibrationObject"):
            self.dll.Asap3ReadCalibrationObject.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.POINTER(TCalibrationObjectValue),
            )
            self.dll.Asap3ReadCalibrationObject.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ReadCalibrationObject2"):
            self.dll.Asap3ReadCalibrationObject2.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.c_bool,
                ctypes.POINTER(TCalibrationObjectValue),
            )
            self.dll.Asap3ReadCalibrationObject2.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ReadCalibrationObjectEx"):
            self.dll.Asap3ReadCalibrationObjectEx.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.POINTER(TCalibrationObjectValueEx),
            )
            self.dll.Asap3ReadCalibrationObjectEx.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3WriteCalibrationObject"):
            self.dll.Asap3WriteCalibrationObject.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.POINTER(TCalibrationObjectValue),
            )
            self.dll.Asap3WriteCalibrationObject.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3WriteCalibrationObjectEx"):
            self.dll.Asap3WriteCalibrationObjectEx.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.POINTER(TCalibrationObjectValueEx),
            )
            self.dll.Asap3WriteCalibrationObjectEx.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3TestObject"):
            self.dll.Asap3TestObject.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3TestObject.restype = ctypes.c_bool

    def Asap3ReadCalibrationObject(
        self,
        module: TModulHdl,
        calibration_object_name: str,
        format_type: int = 0,
    ) -> Optional[Any]:  # TCalibrationObjectValue
        """Read calibration object using record layout information from ASAP2.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object to read.
        format_type : int, optional
            Format of ECU measurement or calibration data
            (0=ECU_INTERNAL, 1=PHYSICAL_REPRESENTATION), by default 0.

        Returns
        -------
        Optional[TCalibrationObjectValue]
            Value of the calibration object, or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If read operation fails.
        """
        if not hasattr(self.dll, "Asap3ReadCalibrationObject"):
            raise CANapeCalibrationError("Asap3ReadCalibrationObject not available in this DLL version")

        c_object_name = ctypes.c_char_p(calibration_object_name.encode("UTF-8"))
        c_format = ctypes.c_int(format_type)
        # Note: TCalibrationObjectValue is a complex union, using placeholder
        # TODO: Implement proper union structure
        from ctypes import Structure

        class TCalibrationObjectValue(Structure):
            _fields_ = [("type", ctypes.c_int)]

        value = TCalibrationObjectValue()

        result = self.dll.Asap3ReadCalibrationObject(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            ctypes.byref(value),
        )
        if result:
            return value
        return None

    def Asap3ReadCalibrationObject2(
        self,
        module: TModulHdl,
        calibration_object_name: str,
        format_type: int = 0,
        force_upload: bool = False,
    ) -> Optional[Any]:  # TCalibrationObjectValue
        """Read calibration object with force upload option.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object to read.
        format_type : int, optional
            Format of ECU measurement or calibration data, by default 0.
        force_upload : bool, optional
            Forces an upload of the calibration object, by default False.

        Returns
        -------
        Optional[TCalibrationObjectValue]
            Value of the calibration object, or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If read operation fails.
        """
        if not hasattr(self.dll, "Asap3ReadCalibrationObject2"):
            raise CANapeCalibrationError("Asap3ReadCalibrationObject2 not available in this DLL version")

        c_object_name = ctypes.c_char_p(calibration_object_name.encode("UTF-8"))
        c_format = ctypes.c_int(format_type)
        c_force_upload = ctypes.c_bool(force_upload)
        # Note: TCalibrationObjectValue is a complex union, using placeholder
        from ctypes import Structure

        class TCalibrationObjectValue(Structure):
            _fields_ = [("type", ctypes.c_int)]

        value = TCalibrationObjectValue()

        result = self.dll.Asap3ReadCalibrationObject2(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            c_force_upload,
            ctypes.byref(value),
        )
        if result:
            return value
        return None

    def Asap3ReadCalibrationObjectEx(
        self,
        module: TModulHdl,
        calibration_object_name: str,
        format_type: int = 0,
    ) -> Optional[Any]:  # TCalibrationObjectValueEx
        """Read calibration object (extended version).

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object to read.
        format_type : int, optional
            Format of ECU measurement or calibration data, by default 0.

        Returns
        -------
        Optional[TCalibrationObjectValueEx]
            Extended value of the calibration object, or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If read operation fails.
        """
        if not hasattr(self.dll, "Asap3ReadCalibrationObjectEx"):
            raise CANapeCalibrationError("Asap3ReadCalibrationObjectEx not available in this DLL version")

        c_object_name = ctypes.c_char_p(calibration_object_name.encode("UTF-8"))
        c_format = ctypes.c_int(format_type)
        # Note: TCalibrationObjectValueEx is a complex union, using placeholder
        # TODO: Implement proper union structure
        from ctypes import Structure

        class TCalibrationObjectValueEx(Structure):
            _fields_ = [("type", ctypes.c_int)]

        value = TCalibrationObjectValueEx()

        result = self.dll.Asap3ReadCalibrationObjectEx(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            ctypes.byref(value),
        )
        if result:
            return value
        return None

    def Asap3WriteCalibrationObject(
        self,
        module: TModulHdl,
        calibration_object_name: str,
        value: Any,  # TCalibrationObjectValue
        format_type: int = 0,
    ) -> bool:
        """Write calibration object using record layout information from ASAP2.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object to write.
        value : TCalibrationObjectValue
            Value of the calibration object.
        format_type : int, optional
            Format of ECU measurement or calibration data, by default 0.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeCalibrationError
            If write operation fails.
        """
        if not hasattr(self.dll, "Asap3WriteCalibrationObject"):
            raise CANapeCalibrationError("Asap3WriteCalibrationObject not available in this DLL version")

        c_object_name = ctypes.c_char_p(calibration_object_name.encode("UTF-8"))
        c_format = ctypes.c_int(format_type)

        # Ensure value is a ctypes structure
        if not isinstance(value, ctypes.Structure):
            raise TypeError("value must be a ctypes.Structure")

        result = self.dll.Asap3WriteCalibrationObject(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            ctypes.byref(value),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeCalibrationError(
                f"Failed to write calibration object (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3WriteCalibrationObjectEx(
        self,
        module: TModulHdl,
        calibration_object_name: str,
        value: Any,  # TCalibrationObjectValueEx
        format_type: int = 0,
    ) -> bool:
        """Write calibration object (extended version).

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        calibration_object_name : str
            Name of the calibration object to write.
        value : TCalibrationObjectValueEx
            Extended value of the calibration object.
        format_type : int, optional
            Format of ECU measurement or calibration data, by default 0.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeCalibrationError
            If write operation fails.
        """
        if not hasattr(self.dll, "Asap3WriteCalibrationObjectEx"):
            raise CANapeCalibrationError("Asap3WriteCalibrationObjectEx not available in this DLL version")

        c_object_name = ctypes.c_char_p(calibration_object_name.encode("UTF-8"))
        c_format = ctypes.c_int(format_type)

        # Ensure value is a ctypes structure
        if not isinstance(value, ctypes.Structure):
            raise TypeError("value must be a ctypes.Structure")

        result = self.dll.Asap3WriteCalibrationObjectEx(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            ctypes.byref(value),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeCalibrationError(
                f"Failed to write calibration object (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3TestObject(self, module: TModulHdl, object_name: str) -> Optional[int]:
        """Test whether the name is a valid object of ASAP2 file.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the calibration object to test.

        Returns
        -------
        Optional[int]
            Object type (0=OTT_MEASURE, 1=OTT_CALIBRATE, 2=OTT_UNKNOWN),
            or None if failed.

        Raises
        ------
        CANapeCalibrationError
            If object test fails.
        """
        if not hasattr(self.dll, "Asap3TestObject"):
            raise CANapeCalibrationError("Asap3TestObject not available in this DLL version")

        c_object_name = ctypes.c_char_p(object_name.encode("UTF-8"))
        obj_type = ctypes.c_int()

        result = self.dll.Asap3TestObject(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.byref(obj_type),
        )
        if result:
            return obj_type.value
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
