"""Network Management Functions.

This module provides functions for managing network activation and security profiles.
"""

import ctypes
from typing import Any, List, Optional

from ..core.exceptions import CANapeNetworkError
from ..core.handle import Handle
from ..core.structs import SecProfileEntry
from ..core.types import DWORD, TModulHdl


class NetworkManagement:
    """Network Management interface.

    This class provides methods for managing network activation and security.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize network management interface.

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
        if hasattr(self.dll, "Asap3GetNetworkName"):
            self.dll.Asap3GetNetworkName.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3GetNetworkName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetNetworkDevices"):
            self.dll.Asap3GetNetworkDevices.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(TModulHdl),
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3GetNetworkDevices.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ActivateNetwork"):
            self.dll.Asap3ActivateNetwork.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_bool,
            )
            self.dll.Asap3ActivateNetwork.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3IsNetworkActivated"):
            self.dll.Asap3IsNetworkActivated.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3IsNetworkActivated.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetSecProfileCount"):
            self.dll.Asap3GetSecProfileCount.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3GetSecProfileCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetSecProfileIdentifier"):
            self.dll.Asap3GetSecProfileIdentifier.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3GetSecProfileIdentifier.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetSecProfileInfo"):
            self.dll.Asap3GetSecProfileInfo.argtypes = (
                ctypes.c_void_p,
                ctypes.c_uint,
                ctypes.POINTER(SecProfileEntry),
            )
            self.dll.Asap3GetSecProfileInfo.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3AddSecProfileToNetwork"):
            self.dll.Asap3AddSecProfileToNetwork.argtypes = (
                ctypes.c_void_p,
                ctypes.c_uint,
                ctypes.c_char_p,
            )
            self.dll.Asap3AddSecProfileToNetwork.restype = ctypes.c_bool

    def Asap3GetNetworkName(
        self, module: TModulHdl, max_size: int = 256
    ) -> Optional[str]:
        """Get the name of the used network.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        max_size : int, optional
            Maximum size of name buffer, by default 256.

        Returns
        -------
        Optional[str]
            Network name, or None if failed.

        Raises
        ------
        CANapeNetworkError
            If network name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetNetworkName"):
            raise CANapeNetworkError(
                "Asap3GetNetworkName not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_uint(0)
        name = None

        # Query size
        result = self.dll.Asap3GetNetworkName(
            self.handle.handle, module, name, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to get network name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = min(size.value + 1, max_size)
        name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetNetworkName(
            self.handle.handle, module, name, ctypes.byref(size)
        )
        if result:
            return name.value.decode("UTF-8")
        return None

    def Asap3GetNetworkDevices(
        self, network_name: str, max_devices: int = 100
    ) -> Optional[List[TModulHdl]]:
        """Get devices in a network.

        Parameters
        ----------
        network_name : str
            Name of the network.
        max_devices : int, optional
            Maximum number of devices to retrieve, by default 100.

        Returns
        -------
        Optional[List[TModulHdl]]
            List of module handles, or None if failed.

        Raises
        ------
        CANapeNetworkError
            If network devices cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetNetworkDevices"):
            raise CANapeNetworkError(
                "Asap3GetNetworkDevices not available in this DLL version"
            )

        c_network_name = ctypes.c_char_p(network_name.encode("UTF-8"))
        module_array = (TModulHdl * max_devices)()
        count = ctypes.c_uint(max_devices)

        result = self.dll.Asap3GetNetworkDevices(
            self.handle.handle, c_network_name, module_array, ctypes.byref(count)
        )
        if result:
            return list(module_array[: count.value])
        return None

    def Asap3ActivateNetwork(
        self, network_name: str, activate: bool
    ) -> bool:
        """Activate or deactivate a network.

        Parameters
        ----------
        network_name : str
            Name of the network.
        activate : bool
            Activate if True, deactivate if False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeNetworkError
            If network activation fails.
        """
        if not hasattr(self.dll, "Asap3ActivateNetwork"):
            raise CANapeNetworkError(
                "Asap3ActivateNetwork not available in this DLL version"
            )

        c_network_name = ctypes.c_char_p(network_name.encode("UTF-8"))
        result = self.dll.Asap3ActivateNetwork(
            self.handle.handle, c_network_name, ctypes.c_bool(activate)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to activate network (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsNetworkActivated(self, network_name: str) -> bool:
        """Check if a network is activated.

        Parameters
        ----------
        network_name : str
            Name of the network.

        Returns
        -------
        bool
            True if network is activated, False otherwise.

        Raises
        ------
        CANapeNetworkError
            If network state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsNetworkActivated"):
            raise CANapeNetworkError(
                "Asap3IsNetworkActivated not available in this DLL version"
            )

        c_network_name = ctypes.c_char_p(network_name.encode("UTF-8"))
        activated = ctypes.c_bool()

        result = self.dll.Asap3IsNetworkActivated(
            self.handle.handle, c_network_name, ctypes.byref(activated)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to check network activation (Error Code: {error_code})",
                error_code=error_code,
            )
        return activated.value

    def Asap3GetSecProfileCount(self) -> int:
        """Get the count of security profiles.

        Returns
        -------
        int
            Security profile count.

        Raises
        ------
        CANapeNetworkError
            If profile count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetSecProfileCount"):
            raise CANapeNetworkError(
                "Asap3GetSecProfileCount not available in this DLL version"
            )

        count = ctypes.c_uint()
        result = self.dll.Asap3GetSecProfileCount(
            self.handle.handle, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to get security profile count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3GetSecProfileIdentifier(
        self, max_size: int = 4096
    ) -> Optional[str]:
        """Get security profile identifiers.

        Parameters
        ----------
        max_size : int, optional
            Maximum size of identifier buffer, by default 4096.

        Returns
        -------
        Optional[str]
            Security profile identifiers, or None if failed.

        Raises
        ------
        CANapeNetworkError
            If profile identifiers cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetSecProfileIdentifier"):
            raise CANapeNetworkError(
                "Asap3GetSecProfileIdentifier not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        identifiers = None

        # Query size
        result = self.dll.Asap3GetSecProfileIdentifier(
            self.handle.handle, identifiers, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to get profile identifier size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get identifiers
        buffer_size = min(size.value + 1, max_size)
        identifiers = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetSecProfileIdentifier(
            self.handle.handle, identifiers, ctypes.byref(size)
        )
        if result:
            return identifiers.value.decode("UTF-8")
        return None

    def Asap3GetSecProfileInfo(
        self, profile_id: int
    ) -> Optional[SecProfileEntry]:
        """Get information about a security profile.

        Parameters
        ----------
        profile_id : int
            Security profile ID.

        Returns
        -------
        Optional[SecProfileEntry]
            Security profile entry, or None if failed.

        Raises
        ------
        CANapeNetworkError
            If profile info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetSecProfileInfo"):
            raise CANapeNetworkError(
                "Asap3GetSecProfileInfo not available in this DLL version"
            )

        entry = SecProfileEntry()
        result = self.dll.Asap3GetSecProfileInfo(
            self.handle.handle, ctypes.c_uint(profile_id), ctypes.byref(entry)
        )
        if result:
            return entry
        return None

    def Asap3AddSecProfileToNetwork(
        self, profile_id: int, network_name: str
    ) -> bool:
        """Add a security profile to a network.

        Parameters
        ----------
        profile_id : int
            Security profile ID.
        network_name : str
            Name of the network.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeNetworkError
            If profile cannot be added to network.
        """
        if not hasattr(self.dll, "Asap3AddSecProfileToNetwork"):
            raise CANapeNetworkError(
                "Asap3AddSecProfileToNetwork not available in this DLL version"
            )

        c_network_name = ctypes.c_char_p(network_name.encode("UTF-8"))
        result = self.dll.Asap3AddSecProfileToNetwork(
            self.handle.handle, ctypes.c_uint(profile_id), c_network_name
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeNetworkError(
                f"Failed to add security profile to network (Error Code: {error_code})",
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

