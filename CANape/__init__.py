"""CANape Python API - Unified High-Level Interface.

This module provides a unified, high-level Python interface to the Vector CANape
ASAP3 API. It wraps the low-level C API functions and provides a clean, Pythonic
interface with proper error handling, type hints, and documentation.

Example
-------
    >>> from CANape import CANape
    >>> canape = CANape(dll_path="path/to/CANapAPI64.dll")
    >>> canape.init(response_timeout=10000, working_dir="./canape_tmp")
    >>> module = canape.module.create("MyModule", "database.a2l", driver_type=1, channel_no=1)
    >>> value = canape.calibration.read(module, "MyCalibrationObject")
    >>> canape.exit()
"""

from typing import Any, Optional

# Import all sub-modules
from .asap3 import error_handling, initialization, project, version
from .calibration import address_access, object_info, read_write
from .callbacks import events as callbacks_events
from .configuration import project as config_project
from .converter import mdf as converter_mdf
from .core.dll_loader import load_dll
from .core.handle import Handle
from .core.type_assignments import assign_basic_dll_types
from .data_acquisition import (
    control as daq_control,
    reading as daq_reading,
    recorder as daq_recorder,
    setup as daq_setup,
)
from .diagnostic import jobs as diag_jobs, requests as diag_requests, responses as diag_responses
from .flash import management as flash_mgmt
from .misc import utilities as misc_utils
from .module import creation, database, management
from .network import management as network_mgmt
from .scripting import execution as script_exec

__all__ = ["CANape"]


class CANape:
    """Unified CANape API interface.

    This class provides a high-level interface to all CANape functionality,
    organized into logical sub-modules.

    Parameters
    ----------
    dll_path : Optional[str], optional
        Path to CANapAPI64.dll. If None, will search automatically, by default None.

    Attributes
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    init : ASAP3Initialization
        Initialization functions.
    version : ASAP3Version
        Version information functions.
    error : ASAP3ErrorHandling
        Error handling functions.
    project : ASAP3Project
        Project management functions.
    module : ModuleInterface
        Module management interface.
    calibration : CalibrationInterface
        Calibration interface.
    """

    def __init__(self, dll_path: Optional[str] = None) -> None:
        """Initialize CANape API.

        Parameters
        ----------
        dll_path : Optional[str], optional
            Path to CANapAPI64.dll, by default None.
        """
        # Load DLL
        self.dll = load_dll(dll_path)
        assign_basic_dll_types(self.dll)

        # Create handle
        self.handle = Handle()

        # Initialize sub-modules
        self.init = initialization.ASAP3Initialization(self.dll, self.handle)
        self.version = version.ASAP3Version(self.dll, self.handle)
        self.error = error_handling.ASAP3ErrorHandling(self.dll, self.handle)
        self.project = project.ASAP3Project(self.dll, self.handle)

        # Module interface
        self.module = ModuleInterface(self.dll, self.handle)

        # Calibration interface
        self.calibration = CalibrationInterface(self.dll, self.handle)

        # Data acquisition interface
        self.data_acquisition = DataAcquisitionInterface(self.dll, self.handle)

        # Converter interface
        self.converter = converter_mdf.MDFConverter(self.dll, self.handle)

        # Diagnostic interface
        self.diagnostic = DiagnosticInterface(self.dll, self.handle)

        # Scripting interface
        self.scripting = script_exec.ScriptExecution(self.dll, self.handle)

        # Flash interface
        self.flash = flash_mgmt.FlashManagement(self.dll, self.handle)

        # Network interface
        self.network = network_mgmt.NetworkManagement(self.dll, self.handle)

        # Configuration interface
        self.configuration = config_project.ProjectConfiguration(
            self.dll, self.handle
        )

        # Callbacks interface
        self.callbacks = callbacks_events.CallbackEvents(self.dll, self.handle)

        # Utilities interface
        self.misc = misc_utils.Utilities(self.dll, self.handle)

    def __enter__(self) -> "CANape":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit - automatically calls exit if initialized."""
        if self.handle.valid:
            try:
                self.init.Asap3Exit()
            except Exception:
                pass


class ModuleInterface:
    """Module management interface.

    Provides access to module creation, management, and database functions.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize module interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.create = creation.ModuleCreation(dll, handle)
        self.manage = management.ModuleManagement(dll, handle)
        self.database = database.ModuleDatabase(dll, handle)


class CalibrationInterface:
    """Calibration interface.

    Provides access to calibration read/write, address access, and object info functions.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize calibration interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.read_write = read_write.CalibrationReadWrite(dll, handle)
        self.address = address_access.CalibrationAddressAccess(dll, handle)
        self.info = object_info.CalibrationObjectInfo(dll, handle)


class DataAcquisitionInterface:
    """Data Acquisition interface.

    Provides access to data acquisition setup, control, reading, and recorder functions.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize data acquisition interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.setup = daq_setup.DataAcquisitionSetup(dll, handle)
        self.control = daq_control.DataAcquisitionControl(dll, handle)
        self.reading = daq_reading.DataAcquisitionReading(dll, handle)
        self.recorder = daq_recorder.RecorderManagement(dll, handle)


class DiagnosticInterface:
    """Diagnostic interface.

    Provides access to diagnostic job execution, request creation, and response retrieval.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize diagnostic interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.jobs = diag_jobs.DiagnosticJobs(dll, handle)
        self.requests = diag_requests.DiagnosticRequests(dll, handle)
        self.responses = diag_responses.DiagnosticResponses(dll, handle)
