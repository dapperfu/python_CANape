"""High-Level Module Interface.

This module provides a Pythonic, high-level interface for module management,
wrapping the low-level ASAP3 module functions with clean naming and decorators.
"""

from typing import Any, List, Optional

from ..core.decorators import handle_errors, requires_initialization
from ..core.exceptions import CANapeModuleError
from ..core.handle import Handle
from ..core.types import TModulHdl
from . import creation, database, management


class HighLevelModuleInterface:
    """High-level module management interface.

    Provides Pythonic methods for module operations with clean naming
    (removing "Asap3" prefix) and automatic error handling.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize high-level module interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._creation = creation.ModuleCreation(dll, handle)
        self._management = management.ModuleManagement(dll, handle)
        self._database = database.ModuleDatabase(dll, handle)

    @requires_initialization
    @handle_errors("create module")
    def create(
        self,
        module_name: str,
        database_filename: str,
        driver_type: int,
        channel_no: int,
        go_online: bool = True,
        enable_cache: int = -1,
        interface_name: Optional[str] = None,
    ) -> TModulHdl:
        """Create a new module with a database file.

        Pythonic wrapper around Asap3CreateModule variants.

        Parameters
        ----------
        module_name : str
            Name of module to create.
        database_filename : str
            Name of description file to load (A2L, DB, DBC).
        driver_type : int
            Driver type (see tDriverType enum).
        channel_no : int
            Logical communication channel (e.g., CCP:1-4 = CAN1-CAN4,
            255 = TCP/IP, 256 = UDP).
        go_online : bool, optional
            If True, the new device will be switched ONLINE, by default True.
        enable_cache : int, optional
            Enables the cache (1) or disables it (0). If -1, parameter is
            ignored, by default -1.
        interface_name : Optional[str], optional
            Name of the interface to be used. If provided, uses CreateModule4,
            by default None.

        Returns
        -------
        TModulHdl
            Handle to the newly created module.

        Raises
        ------
        CANapeModuleError
            If module creation fails.

        Examples
        --------
        >>> module = canape.module.create(
        ...     "MyModule",
        ...     "database.a2l",
        ...     driver_type=1,
        ...     channel_no=1
        ... )
        """
        if interface_name:
            return self._creation.Asap3CreateModule4(
                module_name,
                database_filename,
                driver_type,
                channel_no,
                interface_name,
                go_online,
                enable_cache,
            )
        elif enable_cache != -1:
            return self._creation.Asap3CreateModule3(
                module_name,
                database_filename,
                driver_type,
                channel_no,
                go_online,
                enable_cache,
            )
        elif not go_online:
            return self._creation.Asap3CreateModule2(
                module_name,
                database_filename,
                driver_type,
                channel_no,
                go_online,
            )
        else:
            return self._creation.Asap3CreateModule(
                module_name,
                database_filename,
                driver_type,
                channel_no,
            )

    add = create  # Alias for better naming

    @requires_initialization
    @handle_errors("remove module")
    def remove(self, module: TModulHdl) -> bool:
        """Remove a module.

        Pythonic wrapper around Asap3ReleaseModule.

        Parameters
        ----------
        module : TModulHdl
            Module handle to remove.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeModuleError
            If module removal fails.
        """
        return self._management.Asap3ReleaseModule(module)

    @requires_initialization
    def list(self) -> List[TModulHdl]:
        """Get list of all modules.

        Note: This requires knowing module names. For a complete list,
        you may need to track modules as they are created.

        Returns
        -------
        List[TModulHdl]
            List of module handles.

        Examples
        --------
        >>> # Get module by name
        >>> module = canape.module.get("MyModule")
        >>> # Or track modules as you create them
        >>> modules = []
        >>> modules.append(canape.module.create("Module1", ...))
        """
        # Note: CANape API doesn't provide a direct way to enumerate all modules
        # without knowing their names. This method is a placeholder.
        # In practice, you should track modules as you create them.
        count = self._management.Asap3GetModuleCount()
        # Return empty list - user should track modules by name
        return []

    @requires_initialization
    @handle_errors("get module")
    def get(self, identifier: str) -> Optional[TModulHdl]:
        """Get module by name.

        Pythonic wrapper around Asap3GetModuleHandle.

        Parameters
        ----------
        identifier : str
            Module name.

        Returns
        -------
        Optional[TModulHdl]
            Module handle if found, None otherwise.

        Examples
        --------
        >>> module = canape.module.get("MyModule")
        """
        try:
            return self._management.Asap3GetModuleHandle(identifier)
        except CANapeModuleError:
            return None

    @requires_initialization
    @handle_errors("get module name")
    def get_name(self, module: TModulHdl) -> str:
        """Get module name from handle.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        str
            Module name.
        """
        return self._management.Asap3GetModuleName(module)
