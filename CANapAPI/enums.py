import ctypes


def generate_fancy_enum_factory(states, name):
    class FancyEnum(ctypes.c_uint):
        def __init__(self, value):
            self.states = states
            assert value in self.states, Exception(
                "Unknown State"
            )
            self.value = value

        def __eq__(self, other):
            if isinstance(other, int):
                return self.value == other.value
            if isinstance(other, str):
                return self.state == other
            if isinstance(other, self.__class__):
                return self.value == other.value
            raise NotImplementedError()

        @property
        def state(self):
            if self.value in self.states:
                return self.states[self.value]

        def __repr__(self):
            return f"{name}<{self.state}>"

    return FancyEnum


TApplicationType = generate_fancy_enum_factory(
    {0: "eUNDEFINED", 1: "eCANAPE", 3: "eAPPLOCATION"},
    "TApplicationType",
)

TScriptStatus = generate_fancy_enum_factory(
    {
        1: "eTScrReady",
        2: "eTScrStarting",
        3: "eTScrRunning",
        4: "eTScrSleeping",
        5: "eTScrSuspended",
        6: "eTScrTerminated",
        7: "eTScrFinishedReturn",
        8: "eTScrFinishedCancel",
        9: "eTScrFailure",
        10: "eTScrTimeout",
    },
    "TScriptStatus",
)

e_RamMode = generate_fancy_enum_factory(
    {0: "e_TR_MODE_RAM", 1: "e_TR_MODE_ROM"}, "e_RamMode"
)

TRecorderType = generate_fancy_enum_factory(
    {
        0: "eTRecorderTypeMDF",
        1: "eTRecorderTypeILinkRT",
        2: "eTRecorderTypeBLF",
    },
    "TRecorderType",
)

ASAP3_EVENT_CODE = generate_fancy_enum_factory(
    {
        0: "et_ON_DATA_ACQ_START",
        1: "et_ON_DATA_ACQ_STOP",
        2: "et_ON_BEFORE_DATA_ACQ_START",
        3: "et_ON_CLOSEPROJECT",
        4: "et_ON_OPENPROJECT",
        5: "et_ON_CLOSECANAPE",
    },
    "ASAP3_EVENT_CODE",
)

TFormat = generate_fancy_enum_factory(
    {0: "ECU_INTERNAL", 1: "PHYSICAL_REPRESENTATION"},
    "TFormat",
)

TValueType = generate_fancy_enum_factory(
    {
        0: "VALUE",
        1: "CURVE",
        2: "MAP",
        3: "AXIS",
        4: "ASCII",
        5: "VAL_BLK",
    },
    "TValueType",
)

TObjectType = generate_fancy_enum_factory(
    {
        0: "OTT_MEASURE",
        1: "OTT_CALIBRATE",
        2: "OTT_UNKNOWN",
    },
    "TObjectType",
)

eServiceStates = generate_fancy_enum_factory(
    {
        10: "e_Created",
        20: "e_Running",
        30: "e_Finished",
        40: "e_TimeOut",
    },
    "eServiceStates",
)

EnRecorderState = generate_fancy_enum_factory(
    {
        0: "e_RecConfigure",
        1: "e_RecActive",
        2: "e_RecRunning",
        3: "e_RecPaused",
        4: "e_Suspended",
    },
    "EnRecorderState",
)

EnParamType = generate_fancy_enum_factory(
    {
        1: "ParamSigned",
        2: "ParamDouble",
        3: "ParamBCD",
        4: "ParamUnsigned",
        5: "ParamFloat",
        6: "ParamAutoDetect",
    },
    "EnParamType",
)

TAsap3FileType = generate_fancy_enum_factory(
    {0: "TYPE_FILE", 1: "TYPE_VIRTUAL", 2: "TYPE_PHYSICAL"},
    "TAsap3FileType",
)

TAsap3ECUState = generate_fancy_enum_factory(
    {0: "TYPE_SWITCH_ONLINE", 1: "TYPE_SWITCH_OFFLINE"},
    "TAsap3ECUState",
)

TAsap3DataType = generate_fancy_enum_factory(
    {
        0: "TYPE_UNKNOWN",
        1: "TYPE_INT",
        2: "TYPE_FLOAT",
        3: "TYPE_DOUBLE",
        4: "TYPE_SIGNED",
        5: "TYPE_UNSIGNED",
        6: "TYPE_STRING",
    },
    "TAsap3DataType",
)

TAsap3DBOType = generate_fancy_enum_factory(
    {
        1: "DBTYPE_MEASUREMENT",
        2: "DBTYPE_CHARACTERISTIC",
        3: "DBTYPE_ALL",
    },
    "TAsap3DBOType",
)

tDriverType = generate_fancy_enum_factory(
    {
        0: "ASAP3_DRIVER_UNKNOWN",
        1: "ASAP3_DRIVER_CCP",
        2: "ASAP3_DRIVER_XCP",
        20: "ASAP3_DRIVER_CAN",
        40: "ASAP3_DRIVER_HEXEDIT",
        50: "ASAP3_DRIVER_ANALOG",
        60: "ASAP3_DRIVER_CANOPEN",
        70: "ASAP3_DRIVER_CANDELA",
        80: "ASAP3_DRIVER_ENVIRONMENT",
        90: "ASAP3_DRIVER_LIN",
        100: "ASAP3_DRIVER_FLX",
        110: "ASAP3_DRIVER_FUNC",
        120: "ASAP3_DRIVER_NIDAQMX",
        130: "ASAP3_DRIVER_XCP_RAMSCOPE",
        140: "ASAP3_DRIVER_SYSTEM",
        150: "ASAP3_DRIVER_ETH",
        160: "ASAP3_DAIO_SYSTEM",
        170: "ASAP3_DRIVER_SOME_IP",
    },
    "tDriverType",
)

tMeasurementState = generate_fancy_enum_factory(
    {
        0: "eT_MEASUREMENT_STOPPED",
        1: "eT_MEASUREMENT_INIT",
        2: "eT_MEASUREMENT_STOP_ON_START",
        3: "eT_MEASUREMENT_EXIT",
        4: "eT_MEASUREMENT_THREAD_RUNNING",
        5: "eT_MEASUREMENT_RUNNING",
    },
    "tMeasurementState",
)
