"""CANape Python API - Unified High-Level Interface.

This module provides a unified, high-level Python interface to the Vector CANape
ASAP3 API. It wraps the low-level C API functions and provides a clean, Pythonic
interface with proper error handling, type hints, and documentation.

Example (High-Level Pythonic Interface)
----------------------------------------
    >>> from CANape import CANape
    >>> with CANape() as canape:
    ...     canape.start()
    ...     module = canape.module.create("MyModule", "database.a2l", driver_type=1, channel_no=1)
    ...     canape.data_acquisition.add_channel(module, "EngineSpeed")
    ...     canape.data_acquisition.start()
    ...     values = canape.data_acquisition.read()
    ...     canape.diagnostic.execute_job(module, "ReadDTCs")
    ...     value = canape.calibration.read(module, "MyCalibrationObject")

Example (Low-Level Direct DLL Access)
-------------------------------------
    >>> from CANape import CANape
    >>> canape = CANape()
    >>> canape.init.Asap3Init(response_timeout=10000, working_dir="./canape_tmp")
    >>> module = canape.module.create.Asap3CreateModule(
    ...     "MyModule", "database.a2l", driver_type=1, channel_no=1
    ... )
    >>> canape.init.Asap3Exit()
"""

from typing import Any, Optional

# Import all sub-modules
from .asap3 import error_handling, initialization, project, version
from .calibration import address_access, object_info, read_write
from .calibration import HighLevelCalibrationInterface
from .core.decorators import handle_errors, requires_initialization
from .core.dll_loader import load_dll
from .core.handle import Handle
from .core.type_assignments import assign_basic_dll_types
from .data_acquisition import (
    control,
    reading,
    recorder,
    setup,
)
from .data_acquisition import HighLevelDataAcquisitionInterface
from .diagnostic import HighLevelDiagnosticInterface
from .module import creation, database, management
from .module import HighLevelModuleInterface

__all__ = ["CANape"]


class CANape:
    """Unified CANape API interface.

    This class provides both high-level Pythonic and low-level direct DLL access
    to all CANape functionality, organized into logical sub-modules.

    Parameters
    ----------
    dll_path : Optional[str], optional
        Path to CANapAPI64.dll. If None, will search automatically, by default None.

    Attributes
    ----------
    dll : Any
        The loaded CANape DLL object (for direct DLL access).
    handle : Handle
        The CANape handle object.
    init : ASAP3Initialization
        Low-level initialization functions (direct DLL access).
    version : ASAP3Version
        Version information functions.
    error : ASAP3ErrorHandling
        Error handling functions.
    project : ASAP3Project
        Project management functions.
    module : HighLevelModuleInterface
        High-level module management interface (Pythonic).
    calibration : HighLevelCalibrationInterface
        High-level calibration interface (Pythonic).
    data_acquisition : HighLevelDataAcquisitionInterface
        High-level data acquisition interface (Pythonic).
    diagnostic : HighLevelDiagnosticInterface
        High-level diagnostic interface (Pythonic).
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

        # Initialize low-level sub-modules (for direct DLL access)
        self.init = initialization.ASAP3Initialization(self.dll, self.handle)
        self.version = version.ASAP3Version(self.dll, self.handle)
        self.error = error_handling.ASAP3ErrorHandling(self.dll, self.handle)
        self.project = project.ASAP3Project(self.dll, self.handle)

        # Initialize high-level interfaces (Pythonic)
        self.module = HighLevelModuleInterface(self.dll, self.handle)
        self.calibration = HighLevelCalibrationInterface(self.dll, self.handle)
        self.data_acquisition = HighLevelDataAcquisitionInterface(self.dll, self.handle)
        self.diagnostic = HighLevelDiagnosticInterface(self.dll, self.handle)

    @handle_errors("start CANape")
    def start(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        debug_mode: bool = True,
    ) -> bool:
        """Start/initialize CANape connection.

        Pythonic wrapper around Asap3Init. Removes "Asap3" prefix.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.

        Returns
        -------
        bool
            True if successful.

        Examples
        --------
        >>> canape = CANape()
        >>> canape.start()
        """
        return self.init.Asap3Init(
            response_timeout=response_timeout,
            working_dir=working_dir,
            fifo_size=fifo_size,
            debug_mode=debug_mode,
        )

    connect = start  # Alias for better naming

    @requires_initialization
    @handle_errors("stop CANape")
    def stop(self) -> bool:
        """Stop/disconnect from CANape.

        Pythonic wrapper around Asap3Exit. Removes "Asap3" prefix.

        Returns
        -------
        bool
            True if successful.

        Examples
        --------
        >>> canape.stop()
        """
        return self.init.Asap3Exit()

    disconnect = stop  # Alias for better naming
    exit = stop  # Alias for compatibility

    @property
    def project_directory(self) -> Optional[str]:
        """Get current project directory.

        Returns
        -------
        Optional[str]
            Current project directory as absolute path, or None if failed.

        Examples
        --------
        >>> dir_path = canape.project_directory
        """
        try:
            return self.project.Asap3GetProjectDirectory()
        except Exception:
            return None

    def __enter__(self) -> "CANape":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit - automatically calls exit if initialized."""
        if self.handle.valid:
            try:
                self.stop()
            except Exception:
                pass


# Keep low-level interfaces for backward compatibility and direct DLL access
class ModuleInterface:
    """Low-level module management interface (for direct DLL access).

    Provides direct access to module creation, management, and database functions.
    Use the high-level `module` attribute for Pythonic interface.
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
    """Low-level calibration interface (for direct DLL access).

    Provides direct access to calibration read/write, address access, and object info functions.
    Use the high-level `calibration` attribute for Pythonic interface.
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
    """Low-level data acquisition interface (for direct DLL access).

    Provides direct access to data acquisition setup, control, reading, and recorder functions.
    Use the high-level `data_acquisition` attribute for Pythonic interface.
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
        self.setup = setup.DataAcquisitionSetup(dll, handle)
        self.control = control.DataAcquisitionControl(dll, handle)
        self.reading = reading.DataAcquisitionReading(dll, handle)
        self.recorder = recorder.RecorderManagement(dll, handle)
