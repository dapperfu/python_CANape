"""DLL function type assignments.

This module assigns argtypes and restype for all CANape DLL functions.
Functions are organized by category and assigned incrementally as
they are implemented.
"""

import ctypes
from typing import Any

from .structs import TApplicationID, version_t
from .types import TAsap3Hdl


def assign_init_functions(dll: Any) -> Any:
    """Assign argtypes and restype for initialization DLL functions.

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    # Asap3Init
    dll.Asap3Init.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_bool,
    )
    dll.Asap3Init.restype = ctypes.c_bool

    # Asap3Init2
    dll.Asap3Init2.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_bool,
    )
    dll.Asap3Init2.restype = ctypes.c_bool

    # Asap3Init3
    dll.Asap3Init3.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_bool,
        ctypes.c_bool,
    )
    dll.Asap3Init3.restype = ctypes.c_bool

    # Asap3Init4
    dll.Asap3Init4.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.c_bool,
    )
    dll.Asap3Init4.restype = ctypes.c_bool

    # Asap3Init5
    dll.Asap3Init5.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.c_bool,
    )
    dll.Asap3Init5.restype = ctypes.c_bool

    # Asap3Init6
    dll.Asap3Init6.argtypes = (
        ctypes.POINTER(TAsap3Hdl),
        ctypes.c_ulong,
        ctypes.c_char_p,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.c_bool,
        ctypes.POINTER(TApplicationID),
    )
    dll.Asap3Init6.restype = ctypes.c_bool

    return dll


def assign_exit_functions(dll: Any) -> Any:
    """Assign argtypes and restype for exit DLL functions.

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    # Asap3Exit
    dll.Asap3Exit.argtypes = (TAsap3Hdl,)
    dll.Asap3Exit.restype = ctypes.c_bool

    # Asap3Exit2
    dll.Asap3Exit2.argtypes = (
        TAsap3Hdl,
        ctypes.c_bool,
    )
    dll.Asap3Exit2.restype = ctypes.c_bool

    return dll


def assign_version_functions(dll: Any) -> Any:
    """Assign argtypes and restype for version DLL functions.

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    # Asap3GetVersion
    dll.Asap3GetVersion.argtypes = (ctypes.POINTER(version_t),)
    dll.Asap3GetVersion.restype = ctypes.c_bool

    return dll


def assign_interactive_mode_functions(dll: Any) -> Any:
    """Assign argtypes and restype for interactive mode DLL functions.

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    # Asap3SetInteractiveMode
    dll.Asap3SetInteractiveMode.argtypes = (
        TAsap3Hdl,
        ctypes.c_bool,
    )
    dll.Asap3SetInteractiveMode.restype = ctypes.c_bool

    # Asap3GetInteractiveMode
    dll.Asap3GetInteractiveMode.argtypes = (
        TAsap3Hdl,
        ctypes.POINTER(ctypes.c_bool),
    )
    dll.Asap3GetInteractiveMode.restype = ctypes.c_bool

    return dll


def assign_project_functions(dll: Any) -> Any:
    """Assign argtypes and restype for project DLL functions.

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    # Asap3GetProjectDirectory
    dll.Asap3GetProjectDirectory.argtypes = (
        TAsap3Hdl,
        ctypes.POINTER(ctypes.c_char),
        ctypes.POINTER(ctypes.c_ulong),
    )
    dll.Asap3GetProjectDirectory.restype = ctypes.c_bool

    return dll


def assign_basic_dll_types(dll: Any) -> Any:
    """Assign basic DLL function types (initialization, exit, version, etc.).

    Parameters
    ----------
    dll : Any
        The loaded DLL object.

    Returns
    -------
    Any
        The DLL object with assigned types.
    """
    dll = assign_init_functions(dll)
    dll = assign_exit_functions(dll)
    dll = assign_version_functions(dll)
    dll = assign_interactive_mode_functions(dll)
    dll = assign_project_functions(dll)
    return dll

