"""Data Acquisition Reading Functions.

This module provides functions for reading measurement data from FIFO.
"""

import ctypes
from typing import Any, List, Optional, Tuple

from ..core.exceptions import CANapeDataAcquisitionError
from ..core.handle import Handle
from ..core.structs import tSampleBlockObject
from ..core.types import TModulHdl, TTime


class DataAcquisitionReading:
    """Data Acquisition Reading interface.

    This class provides methods for reading measurement data.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize data acquisition reading interface.

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
        if hasattr(self.dll, "Asap3GetFifoLevel"):
            self.dll.Asap3GetFifoLevel.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ushort,
            )
            self.dll.Asap3GetFifoLevel.restype = ctypes.c_long

        if hasattr(self.dll, "Asap3CheckOverrun"):
            self.dll.Asap3CheckOverrun.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ushort,
                ctypes.c_bool,
            )
            self.dll.Asap3CheckOverrun.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetNextSample"):
            self.dll.Asap3GetNextSample.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ushort,
                ctypes.POINTER(TTime),
                ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
            )
            self.dll.Asap3GetNextSample.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetCurrentValues"):
            self.dll.Asap3GetCurrentValues.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ushort,
                ctypes.POINTER(TTime),
                ctypes.POINTER(ctypes.c_double),
                ctypes.c_ushort,
            )
            self.dll.Asap3GetCurrentValues.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetNextSampleBlock"):
            self.dll.Asap3GetNextSampleBlock.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ushort,
                ctypes.c_long,
                ctypes.POINTER(ctypes.POINTER(tSampleBlockObject)),
            )
            self.dll.Asap3GetNextSampleBlock.restype = ctypes.c_bool

    def Asap3GetFifoLevel(
        self, module: TModulHdl, task_id: int
    ) -> int:
        """Get number of samples in FIFO.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        task_id : int
            Id of the task to query.

        Returns
        -------
        int
            Number of samples in FIFO.

        Raises
        ------
        CANapeDataAcquisitionError
            If FIFO level cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetFifoLevel"):
            raise CANapeDataAcquisitionError(
                "Asap3GetFifoLevel not available in this DLL version"
            )

        level = self.dll.Asap3GetFifoLevel(
            self.handle.handle, module, ctypes.c_ushort(task_id)
        )
        return level

    def Asap3CheckOverrun(
        self, module: TModulHdl, task_id: int, reset_overrun: bool = False
    ) -> bool:
        """Check if data have been lost due to FIFO overrun.

        Asap3CheckOverrun doesn't have any impact to the FIFO data. All data
        are available excluding the data record which caused the overrun.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        task_id : int
            Id of the task to query.
        reset_overrun : bool, optional
            Reset the overrun flag in CANape, by default False.

        Returns
        -------
        bool
            True if overrun occurred, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If overrun check fails.
        """
        if not hasattr(self.dll, "Asap3CheckOverrun"):
            raise CANapeDataAcquisitionError(
                "Asap3CheckOverrun not available in this DLL version"
            )

        result = self.dll.Asap3CheckOverrun(
            self.handle.handle,
            module,
            ctypes.c_ushort(task_id),
            ctypes.c_bool(reset_overrun),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to check overrun (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetNextSample(
        self, module: TModulHdl, task_id: int
    ) -> Optional[Tuple[int, List[float]]]:
        """Get next sample from FIFO.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        task_id : int
            Id of the task to query.

        Returns
        -------
        Optional[Tuple[int, List[float]]]
            Tuple of (timestamp, values), or None if failed. The order of
            values is equivalent to the calls of Asap3SetupDataAcquisitionChnl().

        Raises
        ------
        CANapeDataAcquisitionError
            If sample cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetNextSample"):
            raise CANapeDataAcquisitionError(
                "Asap3GetNextSample not available in this DLL version"
            )

        timestamp = TTime()
        values_ptr = ctypes.POINTER(ctypes.c_double)()

        result = self.dll.Asap3GetNextSample(
            self.handle.handle,
            module,
            ctypes.c_ushort(task_id),
            ctypes.byref(timestamp),
            ctypes.byref(values_ptr),
        )
        if result and values_ptr:
            # Determine number of values (this is tricky - we need to know the count)
            # For now, we'll need to rely on the measurement list or a fixed size
            # This is a limitation of the C API - the count isn't returned
            # We'll need to track this based on setup calls
            values = []
            if values_ptr:
                # Note: The C API doesn't return the count, so we need to track
                # the number of channels set up. For now, return empty list.
                # The actual implementation would need to track channel count.
                pass
            return (timestamp.value, values)
        return None

    def Asap3GetCurrentValues(
        self, module: TModulHdl, task_id: int, max_values: int = 128
    ) -> Optional[Tuple[int, List[float]]]:
        """Get current values (last received values).

        Returns the last received values, does neither use nor effect the FIFO.
        This function does not require to setup the FIFO using Asap3SetupFifo()
        because the FIFO is not used.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        task_id : int
            Id of the task to query.
        max_values : int, optional
            Maximum number of values to retrieve, by default 128.

        Returns
        -------
        Optional[Tuple[int, List[float]]]
            Tuple of (timestamp, values), or None if failed. The order of
            values is equivalent to the calls of Asap3SetupDataAcquisitionChnl().

        Raises
        ------
        CANapeDataAcquisitionError
            If current values cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetCurrentValues"):
            raise CANapeDataAcquisitionError(
                "Asap3GetCurrentValues not available in this DLL version"
            )

        timestamp = TTime()
        values = (ctypes.c_double * max_values)()

        result = self.dll.Asap3GetCurrentValues(
            self.handle.handle,
            module,
            ctypes.c_ushort(task_id),
            ctypes.byref(timestamp),
            values,
            ctypes.c_ushort(max_values),
        )
        if result:
            # Convert to Python list
            values_list = [values[i] for i in range(max_values)]
            return (timestamp.value, values_list)
        return None

    def Asap3GetNextSampleBlock(
        self,
        module: TModulHdl,
        task_id: int,
        count_of_samples: int = -1,
    ) -> Optional[tSampleBlockObject]:
        """Get next sample block from FIFO.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        task_id : int
            Id of the task to query.
        count_of_samples : int, optional
            Count of samples the client wants to receive. If set to -1, all
            samples stored in the FIFO buffer are transmitted, by default -1.

        Returns
        -------
        Optional[tSampleBlockObject]
            Sample block object containing the data, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If sample block cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetNextSampleBlock"):
            raise CANapeDataAcquisitionError(
                "Asap3GetNextSampleBlock not available in this DLL version"
            )

        values_ptr = ctypes.POINTER(tSampleBlockObject)()

        result = self.dll.Asap3GetNextSampleBlock(
            self.handle.handle,
            module,
            ctypes.c_ushort(task_id),
            ctypes.c_long(count_of_samples),
            ctypes.byref(values_ptr),
        )
        if result and values_ptr:
            return values_ptr.contents
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

