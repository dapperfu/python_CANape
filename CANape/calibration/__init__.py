"""High-Level Calibration Interface.

This module provides a Pythonic, high-level interface for calibration operations,
wrapping the low-level ASAP3 calibration functions with clean naming.
"""

from typing import Any, Optional, Union

from ..core.decorators import handle_errors, requires_initialization
from ..core.exceptions import CANapeCalibrationError
from ..core.handle import Handle
from ..core.types import TModulHdl
from . import address_access, object_info, read_write


class HighLevelCalibrationInterface:
    """High-level calibration interface.

    Provides Pythonic methods for calibration operations with clean naming
    (removing "Asap3" prefix) and automatic error handling.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize high-level calibration interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._read_write = read_write.CalibrationReadWrite(dll, handle)
        self._address = address_access.CalibrationAddressAccess(dll, handle)
        self._info = object_info.CalibrationObjectInfo(dll, handle)

    @requires_initialization
    @handle_errors("read calibration object")
    def read(
        self,
        module: TModulHdl,
        object_name: str,
        format_type: int = 0,
    ) -> Any:
        """Read a calibration object.

        Pythonic wrapper around Asap3ReadCalibrationObject variants.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the calibration object to read.
        format_type : int, optional
            Format of ECU calibration data
            (0=ECU_INTERNAL, 1=PHYSICAL_REPRESENTATION), by default 0.

        Returns
        -------
        Any
            Calibration object value(s).

        Raises
        ------
        CANapeCalibrationError
            If calibration read fails.

        Examples
        --------
        >>> value = canape.calibration.read(module, "MyCalibrationObject")
        """
        # Try extended version first, fall back to basic
        try:
            return self._read_write.Asap3ReadCalibrationObjectEx(
                module, object_name, format_type
            )
        except (CANapeCalibrationError, AttributeError):
            try:
                return self._read_write.Asap3ReadCalibrationObject2(
                    module, object_name, format_type
                )
            except (CANapeCalibrationError, AttributeError):
                return self._read_write.Asap3ReadCalibrationObject(
                    module, object_name, format_type
                )

    @requires_initialization
    @handle_errors("write calibration object")
    def write(
        self,
        module: TModulHdl,
        object_name: str,
        value: Any,
        format_type: int = 0,
    ) -> bool:
        """Write a calibration object.

        Pythonic wrapper around Asap3WriteCalibrationObject variants.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the calibration object to write.
        value : Any
            Value(s) to write to the calibration object.
        format_type : int, optional
            Format of ECU calibration data
            (0=ECU_INTERNAL, 1=PHYSICAL_REPRESENTATION), by default 0.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeCalibrationError
            If calibration write fails.

        Examples
        --------
        >>> canape.calibration.write(module, "MyCalibrationObject", 42.5)
        """
        # Try extended version first, fall back to basic
        try:
            return self._read_write.Asap3WriteCalibrationObjectEx(
                module, object_name, value, format_type
            )
        except (CANapeCalibrationError, AttributeError):
            return self._read_write.Asap3WriteCalibrationObject(
                module, object_name, value, format_type
            )

    @requires_initialization
    @handle_errors("read by address")
    def read_by_address(
        self,
        module: TModulHdl,
        address: int,
        size: int,
        data_type: int = 0,
    ) -> Any:
        """Read calibration data by memory address.

        Pythonic wrapper around Asap3ReadByAddress.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        address : int
            Memory address to read from.
        size : int
            Number of bytes to read.
        data_type : int, optional
            Data type (see TAsap3DataType enum), by default 0.

        Returns
        -------
        Any
            Read data value.

        Raises
        ------
        CANapeCalibrationError
            If read by address fails.

        Examples
        --------
        >>> value = canape.calibration.read_by_address(module, 0x12345678, 4)
        """
        return self._address.Asap3ReadByAddress(module, address, size, data_type)

    @requires_initialization
    @handle_errors("write by address")
    def write_by_address(
        self,
        module: TModulHdl,
        address: int,
        value: Any,
        size: int,
        data_type: int = 0,
    ) -> bool:
        """Write calibration data by memory address.

        Pythonic wrapper around Asap3WriteByAddress.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        address : int
            Memory address to write to.
        value : Any
            Value to write.
        size : int
            Number of bytes to write.
        data_type : int, optional
            Data type (see TAsap3DataType enum), by default 0.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeCalibrationError
            If write by address fails.

        Examples
        --------
        >>> canape.calibration.write_by_address(module, 0x12345678, 42, 4)
        """
        return self._address.Asap3WriteByAddress(module, address, value, size, data_type)

    @requires_initialization
    def get_info(
        self,
        module: TModulHdl,
        object_name: str,
    ) -> Any:
        """Get calibration object information.

        Pythonic wrapper around Asap3CalibrationObjectInfo.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the calibration object.

        Returns
        -------
        Any
            Object information structure.

        Examples
        --------
        >>> info = canape.calibration.get_info(module, "MyCalibrationObject")
        """
        try:
            return self._info.Asap3CalibrationObjectInfoEx(module, object_name)
        except (CANapeCalibrationError, AttributeError):
            return self._info.Asap3CalibrationObjectInfo(module, object_name)

    # Expose low-level interfaces for advanced usage
    @property
    def read_write(self) -> read_write.CalibrationReadWrite:
        """Access to low-level read/write functions."""
        return self._read_write

    @property
    def address(self) -> address_access.CalibrationAddressAccess:
        """Access to low-level address access functions."""
        return self._address

    @property
    def info(self) -> object_info.CalibrationObjectInfo:
        """Access to low-level object info functions."""
        return self._info
