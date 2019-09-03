from .structs import tAsap3Hdl
import ctypes

BOOL = ctypes.c_int
DWORD = ctypes.c_ulong
BYTE = ctypes.c_ubyte
BOOLEAN = ctypes.c_uint
UINT = ctypes.c_uint
ULONG_PTR = ctypes.c_ulong
DWORD_PTR = ULONG_PTR


def byref(self):
    return ctypes.byref(self)


""" 'Special' types. """
TAsap3Hdl = ctypes.POINTER(tAsap3Hdl)


def __repr__(self):
    return "TAsap3Hdl<>"


setattr(TAsap3Hdl, "__repr__", __repr__)
setattr(TAsap3Hdl, "byref", property(byref))

TRecorderID = ctypes.POINTER(ctypes.c_ulong)


def __repr__(self):
    return "TRecorderID<>"


setattr(TRecorderID, "__repr__", __repr__)
setattr(TRecorderID, "byref", property(byref))

TModulHdl = ctypes.c_ushort


def __repr__(self):
    return "TModulHdl<>"


setattr(TModulHdl, "__repr__", __repr__)
setattr(TModulHdl, "byref", property(byref))

TModulHdl = ctypes.c_ushort


def __repr__(self):
    return "TModulHdl<>"


setattr(TModulHdl, "__repr__", __repr__)
setattr(TModulHdl, "byref", property(byref))

TTime = ctypes.c_ulong


def __repr__(self):
    return "TTime<>"


setattr(TTime, "__repr__", __repr__)
setattr(TTime, "byref", property(byref))

TScriptHdl = DWORD_PTR


def __repr__(self):
    return "TScriptHdl<>"


setattr(TScriptHdl, "__repr__", __repr__)
setattr(TScriptHdl, "byref", property(byref))
