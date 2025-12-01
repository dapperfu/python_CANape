"""Module Management Functions.

This module provides functions for managing module activation, memory pages,
resume mode, and other module operations.
"""

import ctypes
from typing import Any, Optional

from ..core.exceptions import CANapeModuleError
from ..core.handle import Handle
from ..core.types import TModulHdl


class ModuleManagement:
    """Module Management interface.

    This class provides methods for managing modules.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize module management interface.

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
        # Module count and info
        if hasattr(self.dll, "Asap3GetModuleCount"):
            self.dll.Asap3GetModuleCount.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3GetModuleCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetModuleName"):
            self.dll.Asap3GetModuleName.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char_p),
            )
            self.dll.Asap3GetModuleName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetModuleHandle"):
            self.dll.Asap3GetModuleHandle.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3GetModuleHandle.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ReleaseModule"):
            self.dll.Asap3ReleaseModule.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3ReleaseModule.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetCommunicationType"):
            self.dll.Asap3GetCommunicationType.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char_p),
            )
            self.dll.Asap3GetCommunicationType.restype = ctypes.c_bool

        # Module activation
        if hasattr(self.dll, "Asap3IsModuleActive"):
            self.dll.Asap3IsModuleActive.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3IsModuleActive.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ModuleActivation"):
            self.dll.Asap3ModuleActivation.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_bool,
            )
            self.dll.Asap3ModuleActivation.restype = ctypes.c_bool

        # Memory pages
        if hasattr(self.dll, "Asap3SwitchToMemoryPage"):
            self.dll.Asap3SwitchToMemoryPage.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_int,
            )
            self.dll.Asap3SwitchToMemoryPage.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetMemoryPage"):
            self.dll.Asap3GetMemoryPage.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetMemoryPage.restype = ctypes.c_bool

        # Resume mode
        if hasattr(self.dll, "Asap3HasResumeMode"):
            self.dll.Asap3HasResumeMode.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3HasResumeMode.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SetResumeMode"):
            self.dll.Asap3SetResumeMode.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3SetResumeMode.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3IsResumeModeActive"):
            self.dll.Asap3IsResumeModeActive.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3IsResumeModeActive.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ClearResumeMode"):
            self.dll.Asap3ClearResumeMode.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3ClearResumeMode.restype = ctypes.c_bool

        # Restart measurement on error
        if hasattr(self.dll, "Asap3RestartMeasurementOnError"):
            self.dll.Asap3RestartMeasurementOnError.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_bool,
            )
            self.dll.Asap3RestartMeasurementOnError.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3IsRestartMeasurementOnErrorEnabled"):
            self.dll.Asap3IsRestartMeasurementOnErrorEnabled.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3IsRestartMeasurementOnErrorEnabled.restype = ctypes.c_bool

        # ECU online/offline
        if hasattr(self.dll, "Asap3ECUOnOffline"):
            self.dll.Asap3ECUOnOffline.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_int,
                ctypes.c_bool,
            )
            self.dll.Asap3ECUOnOffline.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3IsECUOnline"):
            self.dll.Asap3IsECUOnline.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3IsECUOnline.restype = ctypes.c_bool

        # Driver type
        if hasattr(self.dll, "Asap3GetEcuDriverType"):
            self.dll.Asap3GetEcuDriverType.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetEcuDriverType.restype = ctypes.c_bool

    def Asap3GetModuleCount(self) -> int:
        """Get the count of instantiated modules in the current project.

        Returns
        -------
        int
            Count of modules.

        Raises
        ------
        CANapeModuleError
            If module count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetModuleCount"):
            raise CANapeModuleError("Asap3GetModuleCount not available in this DLL version")

        count = ctypes.c_ulong()
        result = self.dll.Asap3GetModuleCount(self.handle.handle, ctypes.byref(count))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get module count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3GetModuleName(self, module: TModulHdl) -> Optional[str]:
        """Get the name of a module.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[str]
            Module name, or None if failed.

        Raises
        ------
        CANapeModuleError
            If module name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetModuleName"):
            raise CANapeModuleError("Asap3GetModuleName not available in this DLL version")

        module_name = ctypes.POINTER(ctypes.c_char_p)()
        result = self.dll.Asap3GetModuleName(self.handle.handle, module, ctypes.byref(module_name))
        if result and module_name:
            return module_name.contents.value.decode("UTF-8")
        return None

    def Asap3GetModuleHandle(self, module_name: str) -> TModulHdl:
        """Get handle of an existing module (created by another application).

        Parameters
        ----------
        module_name : str
            Name of module to get handle.

        Returns
        -------
        TModulHdl
            Module handle.

        Raises
        ------
        CANapeModuleError
            If module handle cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetModuleHandle"):
            raise CANapeModuleError("Asap3GetModuleHandle not available in this DLL version")

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        module = TModulHdl()

        result = self.dll.Asap3GetModuleHandle(self.handle.handle, c_module_name, ctypes.byref(module))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get module handle (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3ReleaseModule(self, module: TModulHdl) -> bool:
        """Release a module (opposite of AttachAsap2/CreateModule).

        Parameters
        ----------
        module : TModulHdl
            Handle of module to release.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If module cannot be released.
        """
        if not hasattr(self.dll, "Asap3ReleaseModule"):
            raise CANapeModuleError("Asap3ReleaseModule not available in this DLL version")

        result = self.dll.Asap3ReleaseModule(self.handle.handle, module)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to release module (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetCommunicationType(self, module: TModulHdl) -> Optional[str]:
        """Get current communication type (e.g., "CAN").

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[str]
            Communication type, or None if failed.

        Raises
        ------
        CANapeModuleError
            If communication type cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetCommunicationType"):
            raise CANapeModuleError("Asap3GetCommunicationType not available in this DLL version")

        comm_type = ctypes.POINTER(ctypes.c_char_p)()
        result = self.dll.Asap3GetCommunicationType(self.handle.handle, module, ctypes.byref(comm_type))
        if result and comm_type:
            return comm_type.contents.value.decode("UTF-8")
        return None

    def Asap3IsModuleActive(self, module: TModulHdl) -> bool:
        """Get the activation state of a specific module.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if module is active, False otherwise.

        Raises
        ------
        CANapeModuleError
            If module state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsModuleActive"):
            raise CANapeModuleError("Asap3IsModuleActive not available in this DLL version")

        activate = ctypes.c_bool()
        result = self.dll.Asap3IsModuleActive(self.handle.handle, module, ctypes.byref(activate))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get module state (Error Code: {error_code})",
                error_code=error_code,
            )
        return activate.value

    def Asap3ModuleActivation(self, module: TModulHdl, activate: bool) -> bool:
        """Switch module activation state (activated/deactivated).

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        activate : bool
            True to activate, False to deactivate.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If module activation cannot be changed.
        """
        if not hasattr(self.dll, "Asap3ModuleActivation"):
            raise CANapeModuleError("Asap3ModuleActivation not available in this DLL version")

        c_activate = ctypes.c_bool(activate)
        result = self.dll.Asap3ModuleActivation(self.handle.handle, module, c_activate)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to change module activation (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3SwitchToMemoryPage(self, module: TModulHdl, mode: int) -> bool:
        """Switch the module's cal page between RAM and ROM.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        mode : int
            RAM mode (0=e_TR_MODE_RAM, 1=e_TR_MODE_ROM).

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If memory page cannot be switched.
        """
        if not hasattr(self.dll, "Asap3SwitchToMemoryPage"):
            raise CANapeModuleError("Asap3SwitchToMemoryPage not available in this DLL version")

        c_mode = ctypes.c_int(mode)
        result = self.dll.Asap3SwitchToMemoryPage(self.handle.handle, module, c_mode)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to switch memory page (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetMemoryPage(self, module: TModulHdl) -> int:
        """Get the active cal page.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        int
            RAM mode (0=e_TR_MODE_RAM, 1=e_TR_MODE_ROM).

        Raises
        ------
        CANapeModuleError
            If memory page cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetMemoryPage"):
            raise CANapeModuleError("Asap3GetMemoryPage not available in this DLL version")

        mode = ctypes.c_int()
        result = self.dll.Asap3GetMemoryPage(self.handle.handle, module, ctypes.byref(mode))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get memory page (Error Code: {error_code})",
                error_code=error_code,
            )
        return mode.value

    def Asap3HasResumeMode(self, module: TModulHdl) -> bool:
        """Check if the device supports resume mode.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if resume mode is supported, False otherwise.

        Raises
        ------
        CANapeModuleError
            If resume mode support cannot be determined.
        """
        if not hasattr(self.dll, "Asap3HasResumeMode"):
            raise CANapeModuleError("Asap3HasResumeMode not available in this DLL version")

        possible = ctypes.c_bool()
        result = self.dll.Asap3HasResumeMode(self.handle.handle, module, ctypes.byref(possible))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to check resume mode (Error Code: {error_code})",
                error_code=error_code,
            )
        return possible.value

    def Asap3SetResumeMode(self, module: TModulHdl) -> bool:
        """Enable the resume mode of the ECU.

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
        CANapeModuleError
            If resume mode cannot be enabled.
        """
        if not hasattr(self.dll, "Asap3SetResumeMode"):
            raise CANapeModuleError("Asap3SetResumeMode not available in this DLL version")

        result = self.dll.Asap3SetResumeMode(self.handle.handle, module)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to set resume mode (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsResumeModeActive(self, module: TModulHdl) -> bool:
        """Check if an ECU is in resume mode.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if resume mode is enabled, False otherwise.

        Raises
        ------
        CANapeModuleError
            If resume mode state cannot be determined.
        """
        if not hasattr(self.dll, "Asap3IsResumeModeActive"):
            raise CANapeModuleError("Asap3IsResumeModeActive not available in this DLL version")

        enabled = ctypes.c_bool()
        result = self.dll.Asap3IsResumeModeActive(self.handle.handle, module, ctypes.byref(enabled))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to check resume mode state (Error Code: {error_code})",
                error_code=error_code,
            )
        return enabled.value

    def Asap3ClearResumeMode(self, module: TModulHdl) -> bool:
        """Disable resume mode.

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
        CANapeModuleError
            If resume mode cannot be cleared.
        """
        if not hasattr(self.dll, "Asap3ClearResumeMode"):
            raise CANapeModuleError("Asap3ClearResumeMode not available in this DLL version")

        result = self.dll.Asap3ClearResumeMode(self.handle.handle, module)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to clear resume mode (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3RestartMeasurementOnError(self, module: TModulHdl, restart: bool) -> bool:
        """Enable or disable the option "Restart measurement on Error".

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        restart : bool
            True to enable restart option, False to disable.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If restart option cannot be set.
        """
        if not hasattr(self.dll, "Asap3RestartMeasurementOnError"):
            raise CANapeModuleError("Asap3RestartMeasurementOnError not available in this DLL version")

        c_restart = ctypes.c_bool(restart)
        result = self.dll.Asap3RestartMeasurementOnError(self.handle.handle, module, c_restart)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to set restart option (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsRestartMeasurementOnErrorEnabled(self, module: TModulHdl) -> bool:
        """Get the "Restart measurement on Error" option state.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if restart option is enabled, False otherwise.

        Raises
        ------
        CANapeModuleError
            If restart option state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsRestartMeasurementOnErrorEnabled"):
            raise CANapeModuleError("Asap3IsRestartMeasurementOnErrorEnabled not available in this DLL version")

        restart = ctypes.c_bool()
        result = self.dll.Asap3IsRestartMeasurementOnErrorEnabled(self.handle.handle, module, ctypes.byref(restart))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get restart option state (Error Code: {error_code})",
                error_code=error_code,
            )
        return restart.value

    def Asap3ECUOnOffline(self, module: TModulHdl, state: int, download: bool = False) -> bool:
        """Switch an ECU from online to offline and vice versa.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        state : int
            State flag (0=TYPE_SWITCH_ONLINE, 1=TYPE_SWITCH_OFFLINE).
        download : bool, optional
            If True and state is TYPE_SWITCH_ONLINE, CANape will execute
            a download, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If ECU state cannot be changed.
        """
        if not hasattr(self.dll, "Asap3ECUOnOffline"):
            raise CANapeModuleError("Asap3ECUOnOffline not available in this DLL version")

        c_state = ctypes.c_int(state)
        c_download = ctypes.c_bool(download)
        result = self.dll.Asap3ECUOnOffline(self.handle.handle, module, c_state, c_download)
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to change ECU state (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsECUOnline(self, module: TModulHdl) -> int:
        """Check if an ECU is online or offline.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        int
            State flag (0=TYPE_SWITCH_ONLINE, 1=TYPE_SWITCH_OFFLINE).

        Raises
        ------
        CANapeModuleError
            If ECU state cannot be determined.
        """
        if not hasattr(self.dll, "Asap3IsECUOnline"):
            raise CANapeModuleError("Asap3IsECUOnline not available in this DLL version")

        state = ctypes.c_int()
        result = self.dll.Asap3IsECUOnline(self.handle.handle, module, ctypes.byref(state))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get ECU state (Error Code: {error_code})",
                error_code=error_code,
            )
        return state.value

    def Asap3GetEcuDriverType(self, module: TModulHdl) -> int:
        """Get the driver type of an ECU.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        int
            Driver type (see tDriverType enum).

        Raises
        ------
        CANapeModuleError
            If driver type cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetEcuDriverType"):
            raise CANapeModuleError("Asap3GetEcuDriverType not available in this DLL version")

        driver_type = ctypes.c_int()
        result = self.dll.Asap3GetEcuDriverType(self.handle.handle, module, ctypes.byref(driver_type))
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get driver type (Error Code: {error_code})",
                error_code=error_code,
            )
        return driver_type.value

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
