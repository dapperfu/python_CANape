import ctypes
from .structs import *
from .types import *


def init_functions(dll):
    """Assign argtypes and restype for init dll functions."""
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


def exit_functions(dll):
    """Set argtipes and restype for dll exit functions."""
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


def assign_dll_types(dll):
    """Set argtipes and restype for dll functions."""
    dll = init_functions(dll)
    dll = exit_functions(dll)

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
