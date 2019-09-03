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

class tAsap3Hdl(ctypes.Structure):
    def __repr__(self):
        return "tAsap3Hdl<>"

TAsap3Hdl = ctypes.POINTER(tAsap3Hdl)
setattr(TAsap3Hdl, "__repr__", lambda self: f"TAsap3Hdl<>")
setattr(TAsap3Hdl, "byref", property(lambda self: ctypes.byref(self)))

TRecorderID = ctypes.POINTER(ctypes.c_ulong)
setattr(TRecorderID, "__repr__", lambda self: f"TRecorderID<>")
setattr(TRecorderID, "byref", property(lambda self: ctypes.byref(self)))


TModulHdl = ctypes.c_ushort
setattr(TModulHdl, "__repr__", lambda self: f"TModulHdl<>")
setattr(TModulHdl, "byref", property(lambda self: ctypes.byref(self)))

TTime = ctypes.c_ulong
setattr(TTime, "__repr__", lambda self: f"TTime<>")
setattr(TTime, "byref", property(lambda self: ctypes.byref(self)))

TScriptHdl = DWORD_PTR
setattr(TScriptHdl, "__repr__", lambda self: f"TScriptHdl<>")
setattr(TScriptHdl, "byref", property(lambda self: ctypes.byref(self)))


TAsap3DiagHdl = ctypes.c_ulong
setattr(TAsap3DiagHdl, "__repr__", lambda self: f"TAsap3DiagHdl<>")
setattr(TAsap3DiagHdl, "byref", property(lambda self: ctypes.byref(self)))

