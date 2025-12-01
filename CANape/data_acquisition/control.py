"""Data Acquisition Control Functions.

This module provides functions for starting and stopping data acquisition.
"""

import ctypes
from typing import Any

from ..core.enums import tMeasurementState
from ..core.exceptions import CANapeDataAcquisitionError
from ..core.handle import Handle


class DataAcquisitionControl:
    """Data Acquisition Control interface.

    This class provides methods for controlling data acquisition.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize data acquisition control interface.

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
        if hasattr(self.dll, "Asap3StartDataAcquisition"):
            self.dll.Asap3StartDataAcquisition.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3StartDataAcquisition.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3StopDataAcquisition"):
            self.dll.Asap3StopDataAcquisition.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3StopDataAcquisition.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetMeasurementState"):
            self.dll.Asap3GetMeasurementState.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetMeasurementState.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3HasMCD3License"):
            self.dll.Asap3HasMCD3License.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3HasMCD3License.restype = ctypes.c_bool

    def Asap3StartDataAcquisition(self) -> bool:
        """Start data acquisition.

        Starts the data acquisition process for all configured channels.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If data acquisition cannot be started.
        """
        if not hasattr(self.dll, "Asap3StartDataAcquisition"):
            raise CANapeDataAcquisitionError(
                "Asap3StartDataAcquisition not available in this DLL version"
            )

        result = self.dll.Asap3StartDataAcquisition(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to start data acquisition (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3StopDataAcquisition(self) -> bool:
        """Stop data acquisition.

        Stops the data acquisition process.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If data acquisition cannot be stopped.
        """
        if not hasattr(self.dll, "Asap3StopDataAcquisition"):
            raise CANapeDataAcquisitionError(
                "Asap3StopDataAcquisition not available in this DLL version"
            )

        result = self.dll.Asap3StopDataAcquisition(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to stop data acquisition (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetMeasurementState(self) -> int:
        """Get current state of the measurement.

        Returns
        -------
        int
            Measurement state (see tMeasurementState enum).

        Raises
        ------
        CANapeDataAcquisitionError
            If measurement state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetMeasurementState"):
            raise CANapeDataAcquisitionError(
                "Asap3GetMeasurementState not available in this DLL version"
            )

        state = ctypes.c_int()
        result = self.dll.Asap3GetMeasurementState(
            self.handle.handle, ctypes.byref(state)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get measurement state (Error Code: {error_code})",
                error_code=error_code,
            )
        return state.value

    def Asap3HasMCD3License(self) -> bool:
        """Check if MCD3 option is enabled.

        Returns
        -------
        bool
            True if MCD3 license is available, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If license check fails.
        """
        if not hasattr(self.dll, "Asap3HasMCD3License"):
            raise CANapeDataAcquisitionError(
                "Asap3HasMCD3License not available in this DLL version"
            )

        available = ctypes.c_bool()
        result = self.dll.Asap3HasMCD3License(
            self.handle.handle, ctypes.byref(available)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to check MCD3 license (Error Code: {error_code})",
                error_code=error_code,
            )
        return available.value

    def Asap3ConnectDataAcquisition(self) -> bool:
        """Connect to an already running measurement.

        This function is only available in InteractiveMode.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If connection fails.
        """
        if not hasattr(self.dll, "Asap3ConnectDataAcquisition"):
            raise CANapeDataAcquisitionError(
                "Asap3ConnectDataAcquisition not available in this DLL version"
            )

        result = self.dll.Asap3ConnectDataAcquisition(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to connect to data acquisition (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3StartResumedDataAcquisition(self) -> bool:
        """Start data acquisition in Resume mode.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If resumed acquisition cannot be started.
        """
        if not hasattr(self.dll, "Asap3StartResumedDataAcquisition"):
            raise CANapeDataAcquisitionError(
                "Asap3StartResumedDataAcquisition not available in this DLL version"
            )

        result = self.dll.Asap3StartResumedDataAcquisition(
            self.handle.handle
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to start resumed data acquisition (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DisconnectDataAcquisition(self) -> bool:
        """Disconnect from a running measurement.

        This function can only be used if Asap3ConnectDataAcquisition was
        called before.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If disconnection fails.
        """
        if not hasattr(self.dll, "Asap3DisconnectDataAcquisition"):
            raise CANapeDataAcquisitionError(
                "Asap3DisconnectDataAcquisition not available in this DLL version"
            )

        result = self.dll.Asap3DisconnectDataAcquisition(
            self.handle.handle
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to disconnect from data acquisition (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3TimeSync(self, enabled: bool) -> bool:
        """Enable or disable the SyncMode (CANape timesync option).

        Parameters
        ----------
        enabled : bool
            Enable the CANape timesync option.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If time sync cannot be set.
        """
        if not hasattr(self.dll, "Asap3TimeSync"):
            raise CANapeDataAcquisitionError(
                "Asap3TimeSync not available in this DLL version"
            )

        result = self.dll.Asap3TimeSync(
            self.handle.handle, ctypes.c_bool(enabled)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to set time sync (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsTimeSyncEnabled(self) -> bool:
        """Check if SyncMode is enabled.

        Returns
        -------
        bool
            True if time sync is enabled, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If time sync state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsTimeSyncEnabled"):
            raise CANapeDataAcquisitionError(
                "Asap3IsTimeSyncEnabled not available in this DLL version"
            )

        enabled = ctypes.c_bool()
        result = self.dll.Asap3IsTimeSyncEnabled(
            self.handle.handle, ctypes.byref(enabled)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to check time sync state (Error Code: {error_code})",
                error_code=error_code,
            )
        return enabled.value

    def Asap3UseNAN(self, use: bool) -> bool:
        """Switch NAN identification on or off.

        The default value in CANape is 1. This switch has only an influence
        on monitoring devices.

        Parameters
        ----------
        use : bool
            Switch NAN on (True) or off (False).

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If NAN setting cannot be changed.
        """
        if not hasattr(self.dll, "Asap3UseNAN"):
            raise CANapeDataAcquisitionError(
                "Asap3UseNAN not available in this DLL version"
            )

        result = self.dll.Asap3UseNAN(self.handle.handle, ctypes.c_bool(use))
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to set NAN usage (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsNANUsed(self) -> bool:
        """Get the value of the NAN identification.

        The default value in CANape is 1. This switch has only an influence
        on monitoring devices.

        Returns
        -------
        bool
            True if NAN is enabled (default), False if disabled.

        Raises
        ------
        CANapeDataAcquisitionError
            If NAN state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsNANUsed"):
            raise CANapeDataAcquisitionError(
                "Asap3IsNANUsed not available in this DLL version"
            )

        use = ctypes.c_bool()
        result = self.dll.Asap3IsNANUsed(
            self.handle.handle, ctypes.byref(use)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to check NAN usage (Error Code: {error_code})",
                error_code=error_code,
            )
        return use.value

    def Asap3SetMdfFilename(self, mdf_filename: str) -> bool:
        """Set measurement data filename.

        Parameters
        ----------
        mdf_filename : str
            Name of the used MDF file.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If filename cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetMdfFilename"):
            raise CANapeDataAcquisitionError(
                "Asap3SetMdfFilename not available in this DLL version"
            )

        c_filename = ctypes.c_char_p(mdf_filename.encode("UTF-8"))
        result = self.dll.Asap3SetMdfFilename(
            self.handle.handle, c_filename
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to set MDF filename (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetMdfFilename(self) -> Optional[str]:
        """Get measurement data filename.

        Returns
        -------
        Optional[str]
            Name of the used MDF file, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If filename cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetMdfFilename"):
            raise CANapeDataAcquisitionError(
                "Asap3GetMdfFilename not available in this DLL version"
            )

        filename = ctypes.POINTER(ctypes.c_char_p)()
        result = self.dll.Asap3GetMdfFilename(
            self.handle.handle, ctypes.byref(filename)
        )
        if result and filename:
            return filename.contents.value.decode("UTF-8")
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

