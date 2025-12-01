"""Data Acquisition Setup Functions.

This module provides functions for setting up data acquisition channels,
FIFO configuration, and task management.
"""

import ctypes
from typing import Any, List, Optional, Tuple

from ..core.enums import TFormat
from ..core.exceptions import CANapeDataAcquisitionError
from ..core.handle import Handle
from ..core.structs import MeasurementListEntries, TTaskInfo, TTaskInfo2, tFifoSize
from ..core.types import TModulHdl


class DataAcquisitionSetup:
    """Data Acquisition Setup interface.

    This class provides methods for setting up data acquisition.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize data acquisition setup interface.

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
        # Task functions
        if hasattr(self.dll, "Asap3GetEcuTasks"):
            self.dll.Asap3GetEcuTasks.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(TTaskInfo),
                ctypes.POINTER(ctypes.c_ushort),
                ctypes.c_ushort,
            )
            self.dll.Asap3GetEcuTasks.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetEcuTasks2"):
            self.dll.Asap3GetEcuTasks2.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(TTaskInfo2),
                ctypes.POINTER(ctypes.c_ushort),
                ctypes.c_ushort,
            )
            self.dll.Asap3GetEcuTasks2.restype = ctypes.c_bool

        # FIFO setup
        if hasattr(self.dll, "Asap3SetupFifo"):
            self.dll.Asap3SetupFifo.argtypes = (
                ctypes.c_void_p,
                ctypes.c_ushort,
                ctypes.POINTER(tFifoSize),
            )
            self.dll.Asap3SetupFifo.restype = ctypes.c_bool

        # Channel setup
        if hasattr(self.dll, "Asap3SetupDataAcquisitionChnl"):
            self.dll.Asap3SetupDataAcquisitionChnl.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.c_ushort,
                ctypes.c_ushort,
                ctypes.c_bool,
            )
            self.dll.Asap3SetupDataAcquisitionChnl.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SetupDataAcquisitionChnl2"):
            self.dll.Asap3SetupDataAcquisitionChnl2.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,
                ctypes.c_ushort,
                ctypes.c_ushort,
                ctypes.c_bool,
                ctypes.c_bool,
            )
            self.dll.Asap3SetupDataAcquisitionChnl2.restype = ctypes.c_bool

        # Channel info
        if hasattr(self.dll, "Asap3GetChnlDefaultRaster"):
            self.dll.Asap3GetChnlDefaultRaster.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_ushort),
                ctypes.POINTER(ctypes.c_ushort),
            )
            self.dll.Asap3GetChnlDefaultRaster.restype = ctypes.c_bool

        # Measurement list
        if hasattr(self.dll, "Asap3GetMeasurementListEntries"):
            self.dll.Asap3GetMeasurementListEntries.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.POINTER(MeasurementListEntries)),
            )
            self.dll.Asap3GetMeasurementListEntries.restype = ctypes.c_bool

        # Reset channels
        if hasattr(self.dll, "Asap3ResetDataAcquisitionChnls"):
            self.dll.Asap3ResetDataAcquisitionChnls.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3ResetDataAcquisitionChnls.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ResetDataAcquisitionChnlsByModule"):
            self.dll.Asap3ResetDataAcquisitionChnlsByModule.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3ResetDataAcquisitionChnlsByModule.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3CreateLoggerConfiguration"):
            self.dll.Asap3CreateLoggerConfiguration.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3CreateLoggerConfiguration.restype = ctypes.c_bool

    def Asap3GetEcuTasks(
        self, module: TModulHdl, max_tasks: int = 100
    ) -> Optional[List[TTaskInfo]]:
        """Get available data acquisition tasks.

        Returns an array of task information structures. TaskInfo[i].description
        can be used to perform user selection. TaskInfo[i].taskId is intended
        to be used in subsequent calls of Asap3InitDataAcquisition() and
        Asap3GetNextSample().

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        max_tasks : int, optional
            Maximum number of tasks to retrieve, by default 100.

        Returns
        -------
        Optional[List[TTaskInfo]]
            List of task information structures, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If task retrieval fails.
        """
        if not hasattr(self.dll, "Asap3GetEcuTasks"):
            raise CANapeDataAcquisitionError(
                "Asap3GetEcuTasks not available in this DLL version"
            )

        task_info_array = (TTaskInfo * max_tasks)()
        no_tasks = ctypes.c_ushort(max_tasks)

        result = self.dll.Asap3GetEcuTasks(
            self.handle.handle,
            module,
            task_info_array,
            ctypes.byref(no_tasks),
            ctypes.c_ushort(max_tasks),
        )
        if result:
            return list(task_info_array[: no_tasks.value])
        return None

    def Asap3GetEcuTasks2(
        self, module: TModulHdl, max_tasks: int = 100
    ) -> Optional[List[TTaskInfo2]]:
        """Get available data acquisition tasks (extended version).

        Returns an array of extended task information structures including
        event channel information.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        max_tasks : int, optional
            Maximum number of tasks to retrieve, by default 100.

        Returns
        -------
        Optional[List[TTaskInfo2]]
            List of extended task information structures, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If task retrieval fails.
        """
        if not hasattr(self.dll, "Asap3GetEcuTasks2"):
            raise CANapeDataAcquisitionError(
                "Asap3GetEcuTasks2 not available in this DLL version"
            )

        task_info_array = (TTaskInfo2 * max_tasks)()
        no_tasks = ctypes.c_ushort(max_tasks)

        result = self.dll.Asap3GetEcuTasks2(
            self.handle.handle,
            module,
            task_info_array,
            ctypes.byref(no_tasks),
            ctypes.c_ushort(max_tasks),
        )
        if result:
            return list(task_info_array[: no_tasks.value])
        return None

    def Asap3SetupFifo(
        self, fifo_sizes: List[tFifoSize]
    ) -> bool:
        """Setup ECU Task specific FIFO size.

        Reconfigures the division of the FIFO Memory. Set the number of
        FIFOs and their size. Default = fifoSize/23 per Task.

        Parameters
        ----------
        fifo_sizes : List[tFifoSize]
            List of FIFO size structures with taskId, module handle, and
            sample size.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If FIFO setup fails.
        """
        if not hasattr(self.dll, "Asap3SetupFifo"):
            raise CANapeDataAcquisitionError(
                "Asap3SetupFifo not available in this DLL version"
            )

        n_fifo_size = ctypes.c_ushort(len(fifo_sizes))
        fifo_array = (tFifoSize * len(fifo_sizes))(*fifo_sizes)

        result = self.dll.Asap3SetupFifo(
            self.handle.handle, n_fifo_size, fifo_array
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to setup FIFO (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3SetupDataAcquisitionChnl(
        self,
        module: TModulHdl,
        measurement_object_name: str,
        format_type: int = 0,
        task_id: int = 0,
        polling_rate: int = 1,
        save_to_file: bool = False,
    ) -> bool:
        """Initialize data acquisition channel.

        Add a measurement object to the data acquisition channel list.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        measurement_object_name : str
            Name of object to measure.
        format_type : int, optional
            Format of ECU measurement or calibration data
            (0=ECU_INTERNAL, 1=PHYSICAL_REPRESENTATION), by default 0.
        task_id : int, optional
            Id of the task to query. Intends the sampling rate at ECU and
            the rate that channel data samples are put into the FIFO buffer,
            by default 0.
        polling_rate : int, optional
            If acquisition mode is polling, this specifies the polling rate.
            Reduces the original sample rate of ECU data. Example: If the
            sample rate of the ECU is 1 per 10msec, but the CANapeAPI client
            is set to receive data only every 50msec, the option 'downsampling'
            must be set to 5, by default 1.
        save_to_file : bool, optional
            Save this channel to measurement file. Therefore the currently
            selected Recorder will be used, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel setup fails.
        """
        if not hasattr(self.dll, "Asap3SetupDataAcquisitionChnl"):
            raise CANapeDataAcquisitionError(
                "Asap3SetupDataAcquisitionChnl not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            measurement_object_name.encode("UTF-8")
        )
        c_format = ctypes.c_int(format_type)
        c_task_id = ctypes.c_ushort(task_id)
        c_polling_rate = ctypes.c_ushort(polling_rate)
        c_save_to_file = ctypes.c_bool(save_to_file)

        result = self.dll.Asap3SetupDataAcquisitionChnl(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            c_task_id,
            c_polling_rate,
            c_save_to_file,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to setup data acquisition channel (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3SetupDataAcquisitionChnl2(
        self,
        module: TModulHdl,
        measurement_object_name: str,
        format_type: int = 0,
        task_id: int = 0,
        polling_rate: int = 1,
        save_to_file: bool = False,
        transfer_to_client: bool = True,
    ) -> bool:
        """Initialize data acquisition channel (extended version).

        Add a measurement object to the data acquisition channel list with
        transfer to client option.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        measurement_object_name : str
            Name of object to measure.
        format_type : int, optional
            Format of ECU measurement or calibration data, by default 0.
        task_id : int, optional
            Id of the task to query, by default 0.
        polling_rate : int, optional
            If acquisition mode is polling, this specifies the polling rate,
            by default 1.
        save_to_file : bool, optional
            Save this channel to measurement file, by default False.
        transfer_to_client : bool, optional
            Transfers the defined measurement object to the client, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel setup fails.
        """
        if not hasattr(self.dll, "Asap3SetupDataAcquisitionChnl2"):
            raise CANapeDataAcquisitionError(
                "Asap3SetupDataAcquisitionChnl2 not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            measurement_object_name.encode("UTF-8")
        )
        c_format = ctypes.c_int(format_type)
        c_task_id = ctypes.c_ushort(task_id)
        c_polling_rate = ctypes.c_ushort(polling_rate)
        c_save_to_file = ctypes.c_bool(save_to_file)
        c_transfer_to_client = ctypes.c_bool(transfer_to_client)

        result = self.dll.Asap3SetupDataAcquisitionChnl2(
            self.handle.handle,
            module,
            c_object_name,
            c_format,
            c_task_id,
            c_polling_rate,
            c_save_to_file,
            c_transfer_to_client,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to setup data acquisition channel (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetChnlDefaultRaster(
        self, module: TModulHdl, measurement_object_name: str
    ) -> Optional[Tuple[int, int]]:
        """Get measurement data info.

        Retrieves the default raster and downsampling time of a requested
        measurement object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        measurement_object_name : str
            Name of object to measure.

        Returns
        -------
        Optional[Tuple[int, int]]
            Tuple of (task_id, downsampling), or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If raster info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetChnlDefaultRaster"):
            raise CANapeDataAcquisitionError(
                "Asap3GetChnlDefaultRaster not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(
            measurement_object_name.encode("UTF-8")
        )
        task_id = ctypes.c_ushort()
        downsampling = ctypes.c_ushort()

        result = self.dll.Asap3GetChnlDefaultRaster(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.byref(task_id),
            ctypes.byref(downsampling),
        )
        if result:
            return (task_id.value, downsampling.value)
        return None

    def Asap3GetMeasurementListEntries(
        self, module: TModulHdl
    ) -> Optional[MeasurementListEntries]:
        """Get entries defined in the CANape Measurement list.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[MeasurementListEntries]
            Measurement list entries structure, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If measurement list cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetMeasurementListEntries"):
            raise CANapeDataAcquisitionError(
                "Asap3GetMeasurementListEntries not available in this DLL version"
            )

        items = ctypes.POINTER(MeasurementListEntries)()
        result = self.dll.Asap3GetMeasurementListEntries(
            self.handle.handle, module, ctypes.byref(items)
        )
        if result and items:
            return items.contents
        return None

    def Asap3ResetDataAcquisitionChnls(self) -> bool:
        """Reset data acquisition channels.

        Clears all configured data acquisition channels.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel reset fails.
        """
        if not hasattr(self.dll, "Asap3ResetDataAcquisitionChnls"):
            raise CANapeDataAcquisitionError(
                "Asap3ResetDataAcquisitionChnls not available in this DLL version"
            )

        result = self.dll.Asap3ResetDataAcquisitionChnls(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to reset data acquisition channels (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3ResetDataAcquisitionChnlsByModule(
        self, module: TModulHdl
    ) -> bool:
        """Clear the data acquisition channel list of a specific module.

        This function only clears measurement objects from the API-Measurement-List
        which are defined by API and the requested module.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel reset fails.
        """
        if not hasattr(self.dll, "Asap3ResetDataAcquisitionChnlsByModule"):
            raise CANapeDataAcquisitionError(
                "Asap3ResetDataAcquisitionChnlsByModule not available in this DLL version"
            )

        result = self.dll.Asap3ResetDataAcquisitionChnlsByModule(
            self.handle.handle, module
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to reset channels by module (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3CreateLoggerConfiguration(
        self, module: TModulHdl
    ) -> bool:
        """Create a Logger configuration file (DBC).

        Creates a DBC file which describes the CCP or XCP CAN frames.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If logger configuration creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateLoggerConfiguration"):
            raise CANapeDataAcquisitionError(
                "Asap3CreateLoggerConfiguration not available in this DLL version"
            )

        result = self.dll.Asap3CreateLoggerConfiguration(
            self.handle.handle, module
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to create logger configuration (Error Code: {error_code})",
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

