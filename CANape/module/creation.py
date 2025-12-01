"""Module Creation Functions.

This module provides functions for creating and attaching modules to CANape.
"""

import ctypes
from typing import Any, Optional

from ..core.enums import tDriverType
from ..core.exceptions import CANapeModuleError
from ..core.handle import Handle
from ..core.types import TModulHdl


class ModuleCreation:
    """Module Creation interface.

    This class provides methods for creating and attaching modules.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize module creation interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle

        # Assign function types
        self._assign_types()

    def _assign_types(self) -> None:
        """Assign DLL function types."""
        # Asap3AttachAsap2
        if hasattr(self.dll, "Asap3AttachAsap2"):
            self.dll.Asap3AttachAsap2.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3AttachAsap2.restype = ctypes.c_bool

        # Asap3CreateModule
        if hasattr(self.dll, "Asap3CreateModule"):
            self.dll.Asap3CreateModule.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.c_short,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3CreateModule.restype = ctypes.c_bool

        # Asap3CreateModule2
        if hasattr(self.dll, "Asap3CreateModule2"):
            self.dll.Asap3CreateModule2.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.c_short,
                ctypes.c_bool,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3CreateModule2.restype = ctypes.c_bool

        # Asap3CreateModule3
        if hasattr(self.dll, "Asap3CreateModule3"):
            self.dll.Asap3CreateModule3.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.c_short,
                ctypes.c_bool,
                ctypes.c_short,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3CreateModule3.restype = ctypes.c_bool

        # Asap3CreateModule4
        if hasattr(self.dll, "Asap3CreateModule4"):
            self.dll.Asap3CreateModule4.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.c_short,
                ctypes.c_char_p,
                ctypes.c_bool,
                ctypes.c_short,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3CreateModule4.restype = ctypes.c_bool

        # Asap3CreateModuleSec
        if hasattr(self.dll, "Asap3CreateModuleSec"):
            self.dll.Asap3CreateModuleSec.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_short,
                ctypes.c_short,
                ctypes.c_char_p,
                ctypes.c_uint,
                ctypes.c_char_p,
                ctypes.c_bool,
                ctypes.c_short,
                ctypes.POINTER(TModulHdl),
            )
            self.dll.Asap3CreateModuleSec.restype = ctypes.c_bool

    def Asap3AttachAsap2(
        self, asap2_filename: str, can_channel: int
    ) -> TModulHdl:
        """Create a new module/device and attach an ASAP2-description file.

        Parameters
        ----------
        asap2_filename : str
            Name of the ASAP2 file to load.
        can_channel : int
            CAN channel to select.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3AttachAsap2"):
            raise CANapeModuleError(
                "Asap3AttachAsap2 not available in this DLL version"
            )

        c_asap2_filename = ctypes.c_char_p(asap2_filename.encode("UTF-8"))
        c_can_channel = ctypes.c_short(can_channel)
        module = TModulHdl()

        result = self.dll.Asap3AttachAsap2(
            self.handle.handle,
            c_asap2_filename,
            c_can_channel,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to attach ASAP2 file (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3CreateModule(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
    ) -> TModulHdl:
        """Create a new module/device and attach a description file (A2L, DB, DBC).

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load.
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel (e.g., CCP:1-4 = CAN1-CAN4,
            255 = TCP/IP, 256 = UDP).

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateModule"):
            raise CANapeModuleError(
                "Asap3CreateModule not available in this DLL version"
            )

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        c_database_filename = ctypes.c_char_p(
            database_filename.encode("UTF-8")
        )
        c_driver_type = ctypes.c_short(driver_type)
        c_channel_no = ctypes.c_short(channel_no)
        module = TModulHdl()

        result = self.dll.Asap3CreateModule(
            self.handle.handle,
            c_module_name,
            c_database_filename,
            c_driver_type,
            c_channel_no,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to create module (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3CreateModule2(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
        go_online: bool = True,
    ) -> TModulHdl:
        """Create a new module with online/offline control.

        If go_online is False, some API calls can be done even if the
        relevant ECU is not connected.

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load.
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel.
        go_online : bool, optional
            If True, the new device will be switched ONLINE. If False,
            allows creating OFFLINE devices, by default True.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateModule2"):
            raise CANapeModuleError(
                "Asap3CreateModule2 not available in this DLL version"
            )

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        c_database_filename = ctypes.c_char_p(
            database_filename.encode("UTF-8")
        )
        c_driver_type = ctypes.c_short(driver_type)
        c_channel_no = ctypes.c_short(channel_no)
        c_go_online = ctypes.c_bool(go_online)
        module = TModulHdl()

        result = self.dll.Asap3CreateModule2(
            self.handle.handle,
            c_module_name,
            c_database_filename,
            c_driver_type,
            c_channel_no,
            c_go_online,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to create module (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3CreateModule3(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
        go_online: bool = True,
        enable_cache: int = -1,
    ) -> TModulHdl:
        """Create a new module with cache control.

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load.
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel.
        go_online : bool, optional
            If True, the new device will be switched ONLINE, by default True.
        enable_cache : int, optional
            Enables the cache (1) or disables it (0). If -1, parameter is
            ignored, by default -1.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateModule3"):
            raise CANapeModuleError(
                "Asap3CreateModule3 not available in this DLL version"
            )

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        c_database_filename = ctypes.c_char_p(
            database_filename.encode("UTF-8")
        )
        c_driver_type = ctypes.c_short(driver_type)
        c_channel_no = ctypes.c_short(channel_no)
        c_go_online = ctypes.c_bool(go_online)
        c_enable_cache = ctypes.c_short(enable_cache)
        module = TModulHdl()

        result = self.dll.Asap3CreateModule3(
            self.handle.handle,
            c_module_name,
            c_database_filename,
            c_driver_type,
            c_channel_no,
            c_go_online,
            c_enable_cache,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to create module (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3CreateModule4(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
        interface_name: str,
        go_online: bool = True,
        enable_cache: int = -1,
    ) -> TModulHdl:
        """Create a new module with interface name.

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load.
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel.
        interface_name : str
            Name of the interface to be used.
        go_online : bool, optional
            If True, the new device will be switched ONLINE, by default True.
        enable_cache : int, optional
            Enables the cache (1) or disables it (0). If -1, parameter is
            ignored, by default -1.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateModule4"):
            raise CANapeModuleError(
                "Asap3CreateModule4 not available in this DLL version"
            )

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        c_database_filename = ctypes.c_char_p(
            database_filename.encode("UTF-8")
        )
        c_driver_type = ctypes.c_short(driver_type)
        c_channel_no = ctypes.c_short(channel_no)
        c_interface_name = ctypes.c_char_p(interface_name.encode("UTF-8"))
        c_go_online = ctypes.c_bool(go_online)
        c_enable_cache = ctypes.c_short(enable_cache)
        module = TModulHdl()

        result = self.dll.Asap3CreateModule4(
            self.handle.handle,
            c_module_name,
            c_database_filename,
            c_driver_type,
            c_channel_no,
            c_interface_name,
            c_go_online,
            c_enable_cache,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to create module (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

    def Asap3CreateModuleSec(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
        interface_name: str,
        sec_profile_id: int,
        security_role: str,
        go_online: bool = True,
        enable_cache: int = -1,
    ) -> TModulHdl:
        """Create a new module with security profile.

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load.
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel.
        interface_name : str
            Name of the interface to be used.
        sec_profile_id : int
            Security profile ID (if != 0, activation of security on network
            will be done).
        security_role : str
            Security role that will be assigned to the module.
        go_online : bool, optional
            If True, the new device will be switched ONLINE, by default True.
        enable_cache : int, optional
            Enables the cache (1) or disables it (0). If -1, parameter is
            ignored, by default -1.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.
        """
        if not hasattr(self.dll, "Asap3CreateModuleSec"):
            raise CANapeModuleError(
                "Asap3CreateModuleSec not available in this DLL version"
            )

        c_module_name = ctypes.c_char_p(module_name.encode("UTF-8"))
        c_database_filename = ctypes.c_char_p(
            database_filename.encode("UTF-8")
        )
        c_driver_type = ctypes.c_short(driver_type)
        c_channel_no = ctypes.c_short(channel_no)
        c_interface_name = ctypes.c_char_p(interface_name.encode("UTF-8"))
        c_sec_profile_id = ctypes.c_uint(sec_profile_id)
        c_security_role = ctypes.c_char_p(security_role.encode("UTF-8"))
        c_go_online = ctypes.c_bool(go_online)
        c_enable_cache = ctypes.c_short(enable_cache)
        module = TModulHdl()

        result = self.dll.Asap3CreateModuleSec(
            self.handle.handle,
            c_module_name,
            c_database_filename,
            c_driver_type,
            c_channel_no,
            c_interface_name,
            c_sec_profile_id,
            c_security_role,
            c_go_online,
            c_enable_cache,
            ctypes.byref(module),
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to create module (Error Code: {error_code})",
                error_code=error_code,
            )
        return module

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

