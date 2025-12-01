import ctypes

BOOL = ctypes.c_int
DWORD = ctypes.c_ulong
BYTE = ctypes.c_ubyte
BOOLEAN = ctypes.c_uint
UINT = ctypes.c_uint
ULONG_PTR = ctypes.c_ulong
DWORD_PTR = ULONG_PTR

""" 'Special' types. """


# Linchpin
class tAsap3Hdl(ctypes.Structure):
    def __repr__(self):
        return "tAsap3Hdl<>"


TAsap3Hdl = ctypes.POINTER(tAsap3Hdl)
# TODO: Figure out how to extend ctypes types.
TAsap3Hdl.__repr__ = lambda self: "TAsap3Hdl<>"
TAsap3Hdl.byref = property(lambda self: ctypes.byref(self))

TRecorderID = ctypes.POINTER(ctypes.c_ulong)
TRecorderID.__repr__ = lambda self: "TRecorderID<>"
TRecorderID.byref = property(lambda self: ctypes.byref(self))


TModulHdl = ctypes.c_ushort
TModulHdl.__repr__ = lambda self: "TModulHdl<>"
TModulHdl.byref = property(lambda self: ctypes.byref(self))

TTime = ctypes.c_ulong
TTime.__repr__ = lambda self: "TTime<>"
TTime.byref = property(lambda self: ctypes.byref(self))

TScriptHdl = DWORD_PTR
TScriptHdl.__repr__ = lambda self: "TScriptHdl<>"
TScriptHdl.byref = property(lambda self: ctypes.byref(self))


TAsap3DiagHdl = ctypes.c_ulong
TAsap3DiagHdl.__repr__ = lambda self: "TAsap3DiagHdl<>"
TAsap3DiagHdl.byref = property(lambda self: ctypes.byref(self))
