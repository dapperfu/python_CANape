import ctypes
from .types import *

from .enums import TApplicationType


class TApplicationID(ctypes.Structure):
    _fields_ = [
        ("tApplicationType", ctypes.c_int),
        ("tApplicationPath", ctypes.c_char_p),
    ]


class DiagJobResponse(ctypes.Structure):
    _fields_ = [
        ("job_responsestring", ctypes.c_char_p),
        ("job_responseValue", ctypes.c_double),
    ]


class PValues(ctypes.Union):
    __slots__ = ["IVal", "UIVal", "FVal", "DVal"]
    _fields_ = [
        ("IVal", ctypes.c_int),
        ("UIVal", ctypes.c_uint),
        ("FVal", ctypes.c_float),
        ("DVal", ctypes.c_double),
    ]
class DiagNumericParamater(ctypes.Structure):
    __slots__ = [
        "DiagNumeric",
        "Values",
    ]

DiagNumericParamater._fields_ = [
    ("DiagNumeric", ctypes.c_int),
    ("Values", PValues),
]

class DiagNotificationStruct(ctypes.Structure):
    """Structure which is a parameter  of the callback function FNCDIAGNOFIFICATION."""
    _fields_ = [
        ("DiagHandle", TAsap3DiagHdl),
        ("DiagState", ctypes.c_int),
        ("PrivateData", ctypes.c_void_p),
    ]


class MeasurementListEntry(ctypes.Structure):
    _fields_ = [
        ("taskId", ctypes.c_ushort),
        ("rate", ctypes.c_ulong),
        ("SaveFlag", BOOL),
        ("Disabled", BOOL),
        ("ObjectName", ctypes.c_char_p),
    ]


class MeasurementListEntries(ctypes.Structure):
    _fields_ = [
        ("ItemCount", ctypes.c_uint),
        (
            "Entries",
            ctypes.POINTER(
                ctypes.POINTER(MeasurementListEntry)
            ),
        ),
    ]


class DBObjectInfo(ctypes.Structure):
    _fields_ = [
        ("DBObjecttype", ctypes.c_int),
        ("type", ctypes.c_int),
        ("min", ctypes.c_double),
        ("max", ctypes.c_double),
        ("minEx", ctypes.c_double),
        ("maxEx", ctypes.c_double),
        ("precision", BYTE),
        ("unit", ctypes.c_char_p),
    ]


class DBFileInfo(ctypes.Structure):
    _fields_ = [
        ("asap2Fname", ctypes.c_char_p),
        ("asap2Path", ctypes.c_char_p),
        ("type", BYTE),
    ]


class SecProfileEntry(ctypes.Structure):
    _fields_ = [
        ("mId", ctypes.c_uint),
        ("mName", ctypes.c_char_p),
        ("mDescription", ctypes.c_char_p),
    ]


class TCalibrationObjectValueEx2(ctypes.Structure):
    _fields_ = [
        ("xAxisValues", ctypes.POINTER(ctypes.c_double)),
        ("yAxisValues", ctypes.POINTER(ctypes.c_double)),
        ("zValues", ctypes.POINTER(ctypes.c_double)),
        ("zValue", ctypes.POINTER(ctypes.c_double)),
        ("xStart", ctypes.c_ulong),
        ("yStart", ctypes.c_ulong),
        ("xSize", ctypes.c_ulong),
        ("ySize", ctypes.c_ulong),
    ]


class TTaskInfo(ctypes.Structure):
    _fields_ = [
        ("description", ctypes.POINTER(ctypes.c_char)),
        ("taskId", ctypes.c_ushort),
        ("taskCycle", ctypes.c_ulong),
    ]


class TConverterInfo(ctypes.Structure):
    _fields_ = [
        ("Comment", ctypes.c_char_p),
        ("Name", ctypes.c_char_p),
        ("ID", ctypes.c_char_p),
    ]


class TTaskInfo2(ctypes.Structure):
    _fields_ = [
        ("description", ctypes.POINTER(ctypes.c_char)),
        ("taskId", ctypes.c_ushort),
        ("taskCycle", ctypes.c_ulong),
        ("eventChannel", ctypes.c_ulong),
    ]


class tFifoSize(ctypes.Structure):
    _fields_ = [
        ("module", TModulHdl),
        ("taskId", ctypes.c_ushort),
        ("noSamples", ctypes.c_ushort),
    ]


class tSampleObject(ctypes.Structure):
    _fields_ = [
        ("countOfEntires", ctypes.c_ulong),
        ("timestamp", TTime),
        ("data", ctypes.POINTER(ctypes.c_double)),
    ]


class tSampleBlockObject(ctypes.Structure):
    _fields_ = [
        ("has_buffer_Overrun", BOOL),
        ("has_Error", ctypes.c_long),
        ("initialized", BOOL),
        ("countofValidEntries", ctypes.c_long),
        ("countofInitilizedEntries", ctypes.c_long),
        (
            "tSample",
            ctypes.POINTER(ctypes.POINTER(tSampleObject)),
        ),
    ]


# Define version_t as a Python ctypes-structure.
class version_t(ctypes.Structure):
    _fields_ = [
        ("dllMainVersion", ctypes.c_int),
        ("dllSubVersion", ctypes.c_int),
        ("dllRelease", ctypes.c_int),
        ("osVersion", ctypes.c_char * 50),
        ("osRelease", ctypes.c_int),
    ]

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return str(other) == str(self)
        if isinstance(other, str):
            return str(other) == str(self)
        raise Exception(
            f"Unsupported class comparison {type(other)}"
        )

    def __repr__(self):
        return f"API_VERSION<{self.dllMainVersion}.{self.dllSubVersion}.{self.dllRelease}>"

    def __str__(self):
        return "{}.{}.{}".format(
            self.dllMainVersion,
            self.dllSubVersion,
            self.dllRelease,
        )


class Appversion(ctypes.Structure):
    _fields_ = [
        ("MainVersion", ctypes.c_int),
        ("SubVersion", ctypes.c_int),
        ("ServicePack", ctypes.c_int),
        ("Application", ctypes.c_char*30),
    ]


class TLayoutCoeffs(ctypes.Structure):
    _fields_ = [
        ("OffNx", ctypes.c_short),
        ("OffNy", ctypes.c_short),
        ("OffX", ctypes.c_short),
        ("FakX", ctypes.c_short),
        ("OffY", ctypes.c_short),
        ("FakY", ctypes.c_short),
        ("OffW", ctypes.c_short),
        ("FakWx", ctypes.c_short),
        ("FakWy", ctypes.c_short),
    ]
