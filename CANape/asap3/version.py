"""ASAP3 Version Functions.

This module provides functions for retrieving version information from
the CANape API and application.
"""

import ctypes
from typing import Any, Optional

from ..core.exceptions import CANapeError
from ..core.handle import Handle
from ..core.structs import Appversion, version_t
from ..core.type_assignments import assign_version_functions


class ASAP3Version:
    """ASAP3 Version interface.

    This class provides methods for retrieving version information.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize ASAP3 version interface.

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
        assign_version_functions(self.dll)

    def Asap3GetVersion(self) -> Optional[version_t]:
        """Get CANape API version.

        Should be executed, and the received data should be compared.
        The current DLL is suitable if:
        - version.dllMainVersion == CANAPE_API_MAIN_VERSION
        - version.dllSubVersion == CANAPE_API_SUB_VERSION
        - version.dllRelease >= CANAPE_API_RELEASE

        Returns
        -------
        Optional[version_t]
            Version structure containing DLL version information, or None if failed.

        Raises
        ------
        CANapeError
            If version retrieval fails.
        """
        version = version_t()
        result = self.dll.Asap3GetVersion(ctypes.byref(version))
        if result:
            return version
        return None

    def Asap3GetApplicationVersion(self) -> Optional[Appversion]:
        """Get current version of the server application (CANape).

        Returns
        -------
        Optional[Appversion]
            Application version structure, or None if failed.

        Raises
        ------
        CANapeError
            If version retrieval fails.
        """
        if not hasattr(self.dll, "Asap3GetApplicationVersion"):
            raise CANapeError("Asap3GetApplicationVersion not available in this DLL version")

        # Assign types if not already assigned
        if not hasattr(self.dll.Asap3GetApplicationVersion, "argtypes"):
            self.dll.Asap3GetApplicationVersion.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(Appversion),
            )
            self.dll.Asap3GetApplicationVersion.restype = ctypes.c_bool

        version = Appversion()
        result = self.dll.Asap3GetApplicationVersion(self.handle.handle, ctypes.byref(version))
        if result:
            return version
        return None
