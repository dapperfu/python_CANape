"""High-Level Data Acquisition Interface.

This module provides a Pythonic, high-level interface for data acquisition,
wrapping the low-level ASAP3 data acquisition functions with clean naming.
"""

from typing import Any, Dict, List, Optional, Tuple

from ..core.decorators import handle_errors, requires_initialization
from ..core.exceptions import CANapeDataAcquisitionError
from ..core.handle import Handle
from ..core.types import TModulHdl
from .control import DataAcquisitionControl
from .reading import DataAcquisitionReading
from .recorder import RecorderManagement
from .setup import DataAcquisitionSetup


class HighLevelDataAcquisitionInterface:
    """High-level data acquisition interface.

    Provides Pythonic methods for data acquisition operations with clean naming
    (removing "Asap3" prefix) and automatic error handling.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize high-level data acquisition interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._setup = DataAcquisitionSetup(dll, handle)
        self._control = DataAcquisitionControl(dll, handle)
        self._reading = DataAcquisitionReading(dll, handle)
        self._recorder = RecorderManagement(dll, handle)

    @requires_initialization
    @handle_errors("start data acquisition")
    def start(self) -> bool:
        """Start data acquisition.

        Pythonic wrapper around Asap3StartDataAcquisition.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeDataAcquisitionError
            If data acquisition cannot be started.

        Examples
        --------
        >>> canape.data_acquisition.start()
        """
        return self._control.Asap3StartDataAcquisition()

    @requires_initialization
    @handle_errors("stop data acquisition")
    def stop(self) -> bool:
        """Stop data acquisition.

        Pythonic wrapper around Asap3StopDataAcquisition.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeDataAcquisitionError
            If data acquisition cannot be stopped.

        Examples
        --------
        >>> canape.data_acquisition.stop()
        """
        return self._control.Asap3StopDataAcquisition()

    @requires_initialization
    @handle_errors("add channel")
    def add_channel(
        self,
        module: TModulHdl,
        measurement_object_name: str,
        format_type: int = 0,
        task_id: int = 0,
        polling_rate: int = 1,
        save_to_file: bool = False,
        transfer_to_client: bool = True,
    ) -> bool:
        """Add a measurement channel to data acquisition.

        Pythonic wrapper around Asap3SetupDataAcquisitionChnl2.

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
            True if successful.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel setup fails.

        Examples
        --------
        >>> canape.data_acquisition.add_channel(module, "EngineSpeed")
        """
        return self._setup.Asap3SetupDataAcquisitionChnl2(
            module,
            measurement_object_name,
            format_type,
            task_id,
            polling_rate,
            save_to_file,
            transfer_to_client,
        )

    @requires_initialization
    @handle_errors("remove channel")
    def remove_channel(self, module: TModulHdl) -> bool:
        """Remove all channels for a module.

        Pythonic wrapper around Asap3ResetDataAcquisitionChnlsByModule.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeDataAcquisitionError
            If channel removal fails.
        """
        return self._setup.Asap3ResetDataAcquisitionChnlsByModule(module)

    @requires_initialization
    @handle_errors("read values")
    def read(self, module: Optional[TModulHdl] = None) -> Optional[Any]:
        """Read current measurement values.

        Pythonic wrapper around Asap3GetCurrentValues.

        Parameters
        ----------
        module : Optional[TModulHdl], optional
            Module handle. If None, reads from all modules, by default None.

        Returns
        -------
        Optional[Any]
            Measurement values structure, or None if failed.

        Examples
        --------
        >>> values = canape.data_acquisition.read(module)
        >>> # Access values through the returned structure
        """
        try:
            if module is not None:
                # Read from specific module - would need module-specific method
                return self._reading.Asap3GetCurrentValues()
            else:
                return self._reading.Asap3GetCurrentValues()
        except CANapeDataAcquisitionError:
            return None

    @requires_initialization
    @handle_errors("configure acquisition")
    def configure(
        self,
        fifo_sizes: Optional[List[Any]] = None,
        time_sync: Optional[bool] = None,
        use_nan: Optional[bool] = None,
    ) -> bool:
        """Configure data acquisition parameters.

        Parameters
        ----------
        fifo_sizes : Optional[List[Any]], optional
            List of FIFO size structures, by default None.
        time_sync : Optional[bool], optional
            Enable time sync mode, by default None.
        use_nan : Optional[bool], optional
            Enable NAN identification, by default None.

        Returns
        -------
        bool
            True if successful.

        Examples
        --------
        >>> canape.data_acquisition.configure(time_sync=True)
        """
        if fifo_sizes is not None:
            self._setup.Asap3SetupFifo(fifo_sizes)

        if time_sync is not None:
            self._control.Asap3TimeSync(time_sync)

        if use_nan is not None:
            self._control.Asap3UseNAN(use_nan)

        return True

    @requires_initialization
    def get_state(self) -> int:
        """Get current measurement state.

        Returns
        -------
        int
            Measurement state (see tMeasurementState enum).

        Examples
        --------
        >>> state = canape.data_acquisition.get_state()
        """
        return self._control.Asap3GetMeasurementState()

    # Expose low-level interfaces for advanced usage
    @property
    def setup(self) -> DataAcquisitionSetup:
        """Access to low-level setup functions."""
        return self._setup

    @property
    def control(self) -> DataAcquisitionControl:
        """Access to low-level control functions."""
        return self._control

    @property
    def reading(self) -> DataAcquisitionReading:
        """Access to low-level reading functions."""
        return self._reading

    @property
    def recorder(self) -> RecorderManagement:
        """Access to recorder management functions."""
        return self._recorder
