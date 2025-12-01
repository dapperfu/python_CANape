"""Error Code Decoder - Converts DLL error codes to Pythonic error messages.

This module provides comprehensive error code decoding functionality that converts
raw CANape DLL error codes into user-friendly, Pythonic error messages. It uses
both the DLL's Asap3ErrorText function (when available) and a comprehensive
fallback dictionary for all error codes.
"""

from typing import Any, Dict, Optional, Tuple

from . import const
from .exceptions import (
    CANapeCalibrationError,
    CANapeConfigurationError,
    CANapeDataAcquisitionError,
    CANapeDiagnosticError,
    CANapeError,
    CANapeFlashError,
    CANapeHandleError,
    CANapeInitializationError,
    CANapeModuleError,
    CANapeNetworkError,
    CANapeScriptingError,
    CANapeTimeoutError,
    CANapeVersionError,
)


# Comprehensive error code to message mapping
_ERROR_MESSAGES: Dict[int, str] = {
    const.AEC_CMD_NOT_SUP: "Command not supported",
    const.AEC_INTERFACE_NOTSUPPORTED: "Interface type not supported",
    const.AEC_CREATE_MEM_MAPPED_FILE: "Error creating memory mapped file",
    const.AEC_WRITE_CMD: "Error writing data to memory mapped file",
    const.AEC_READ_RESPONSE: "Error reading response from memory mapped file",
    const.AEC_ASAP2_FILE_NOT_FOUND: "ASAP2 file not found",
    const.AEC_INVALID_MODULE_HDL: "Invalid module handle",
    const.AEC_ERR_OPEN_FILE: "Open file error",
    const.AEC_UNKNOWN_OBJECT: "Unknown object name",
    const.AEC_NO_DATABASE: "No database assigned",
    const.AEC_PAR_SIZE_OVERFLOW: "Parameter size too large",
    const.AEC_NOT_WRITE_ACCESS: "Object has no write access",
    const.AEC_OBJECT_TYPE_DOESNT_MATCH: "Object type doesn't match",
    const.AEC_NO_TASKS_OVERFLOW: "Number of tasks overflow",
    const.AEC_CCP_RESPONSE_SIZE_INVALID: "Invalid CCP response size",
    const.AEC_TIMEOUT_RESPONSE: "Timeout reading response from memory mapped file",
    const.AEC_NO_VALUES_SAMPLED: "FIFO doesn't contain any values",
    const.AEC_ACQ_CHNL_OVERRUN: "Too many channels defined relating to single raster",
    const.AEC_NO_RASTER_OVERFLOW: "Too many rasters selected for data acquisition",
    const.AEC_CANAPE_CREATE_PROC_FAILED: "CreateProcess of CANape failed",
    const.AEC_EXIT_DENIED_WHILE_ACQU: "Exit denied because data acquisition is still running",
    const.AEC_WRITE_DATA_FAILED: "Error writing data to application RAM",
    const.AEC_NO_RESPONSE_FROM_ECU: "No response from ECU",
    const.AEC_ACQUIS_ALREADY_RUNNING: "Data acquisition already running",
    const.AEC_ACQUIS_NOT_STARTED: "Data acquisition not started",
    const.AEC_NO_AXIS_PTS_NOT_VALID: "Invalid number of axis points",
    const.AEC_SCRIPT_CMD_TO_LARGE: "Script command size overflow",
    const.AEC_SCRIPT_CMD_INVALID: "Invalid script command",
    const.AEC_UNKNOWN_MODULE_NAME: "Unknown module name",
    const.AEC_FIFO_INTERNAL_ERROR: "CANape internal error concerning FIFO management",
    const.AEC_VERSION_ERROR: "Version error - CANape version mismatch",
    const.AEC_ILLEGAL_DRIVER: "Illegal driver type",
    const.AEC_CALOBJ_READ_FAILED: "Read of calibration object failed",
    const.AEC_ACQ_STP_INIT_FAILED: "Initialization of data acquisition failed",
    const.AEC_ACQ_STP_PROC_FAILED: "Data acquisition failed",
    const.AEC_ACQ_STP_OVERFLOW: "Buffer overflow at data acquisition",
    const.AEC_ACQ_STP_TIME_OVER: "Data acquisition stopped because selected time is elapsed",
    const.AEC_NOSERVER_ERRCODE: "No server application available",
    const.AEC_ERR_OPEN_DATADESCFILE: "Unable to open data description file",
    const.AEC_ERR_OPEN_DATAVERSFILE: "Unable to open a data file",
    const.AEC_TO_MUCH_DISPLAYS_OPEN: "Maximum count of displays are opened",
    const.AEC_INTERNAL_CANAPE_ERROR: "Attempt to create a module failed",
    const.AEC_CANT_OPEN_DISPLAY: "Unable to open a display",
    const.AEC_ERR_NO_PATTERNFILE_DEFINED: "No parameter filename",
    const.AEC_ERR_OPEN_PATTERNFILE: "Unable to open patternfile",
    const.AEC_ERR_CANT_RELEASE_MUTEX: "Release of a mutex failed",
    const.AEC_WRONG_CANAPE_VERSION: "CANape does not fit to DLL version",
    const.AEC_TCP_SERV_CONNECT_FAILED: "Connect to ASAP3 server failed",
    const.AEC_TCP_MISSING_CFG: "Missing CANape TCP Server configuration",
    const.AEC_TCP_SERV_NOT_CONNECTED: "Connection between ASAP3 Server and TCP CANapeAPI is not active",
    const.AEC_FIFO_ALREADY_INIT: "The FIFO Memory was already created",
    const.AEC_ILLEGAL_OPERATION: "It is not possible to operate this command",
    const.AEC_WRONG_TYPE: "The given type is not supported",
    const.AEC_NO_CANAPE_LICENSE: "CANape is not licensed",
    const.AEC_REG_OPEN_KEY_FAILED: "Registry key open failed",
    const.AEC_REG_QUERY_VALUE_FAILED: "Registry value query failed",
    const.AEC_WORKDIR_ACCESS_FAILED: "Working directory access failed",
    const.AEC_INIT_COM_FAILED: "Internal communication error",
    const.AEC_INIT_CMD_FAILED: "Negative response from CANape",
    const.AEC_CANAPE_INVALID_PRG_PATH: "Invalid CANape program path",
    const.AEC_INVALID_ASAP3_HDL: "Invalid ASAP3 handle",
    const.AEC_LOADING_FILE: "File loading failed",
    const.AEC_SAVING_FILE: "File saving failed",
    const.AEC_UPLOAD: "Upload failed",
    const.AEC_WRITE_VALUE_ERROR: "Value could not be written",
    const.AEC_TMTF_NOT_FINSHED: "Other file transmission in process",
    const.AEC_TMTF_SEQUENCE_ERROR: "TransmitFile sequence error",
    const.AEC_TDBO_TYPE_ERROR: "TransmitFile database object type error",
    const.AEC_EXECUTE_SERVICE_ERROR: "CCP request failed",
    const.AEC_INVALID_DRIVERTYPE: "Invalid driver type for this operation",
    const.AEC_DIAG_INVALID_DRIVERTYPE: "Invalid driver type for diagnostic operations",
    const.AEC_DIAG_INVALID_BUSMESSAGE: "Invalid bus message",
    const.AEC_DIAG_INVALID_VARIANT: "Invalid variant",
    const.AEC_DIAG_INVALID_DIAGSERVICE: "Invalid or unknown diagnostic service",
    const.AEC_DIAG_ERR_EXECUTE_SERVICE: "Error while sending diagnostic service",
    const.AEC_DIAG_INVALID_PARAMS: "Invalid or unknown diagnostic parameters",
    const.AEC_DIAG_UNKNOWN_PARAM_NAME: "Invalid or unknown parameter name",
    const.AEC_DIAG_EXCEPTION_ERROR: "Error while creating a diagnostic request",
    const.AEC_DIAG_INVALID_RESPONSE: "Error response cannot be handled",
    const.AEC_DIAG_UNKNOWN_PARAM_TYPE: "Unknown parameter type",
    const.AEC_DIAG_NO_INFO_AVAILABLE: "Currently no information available",
    const.AEC_DIAG_UNKNOWN_RESPHANDLE: "Unknown response handle",
    const.AEC_DIAG_WRONG_SERVICE_STATE: "The current request is in the wrong state for this operation",
    const.AEC_DIAG_INVALID_INDEX_SIZE: "Complex index does not match",
    const.AEC_DIAG_INVALID_RESPONSETYPE: "Invalid response type",
    const.AEC_FLASH_INVALID_MANAGER: "Flash manager invalid",
    const.AEC_FLASH_OBJ_OUT_OF_RANGE: "Flash object out of range",
    const.AEC_FLASH_MANAGER_ERROR: "Flash manager error",
    const.AEC_FLASH_INVALID_APPNAME: "Invalid application name",
    const.AEC_FUNCTION_NOT_SUPPORTED: "This function is not supported in this program version",
    const.AEC_LICENSE_NOT_FOUND: "License file not found",
    const.AEC_RECORDER_ALLREADY_EXISTS: "Recorder already exists",
    const.AEC_RECORDER_NOT_FOUND: "Recorder does not exist",
    const.AEC_RECORDER_INDEX_OUTOFRANGE: "Recorder index out of range",
    const.AEC_REMOVE_RECORDER_ERR: "Error deleting recorder",
    const.AEC_INVALID_PARAMETER: "Wrong parameter value",
    const.AEC_ERROR_CREATERECORDER: "Error creating recorder",
    const.AEC_ERROR_SETRECFILENAME: "Error creating recorder filename",
    const.AEC_ERROR_INVALID_TASKID: "Invalid task ID for the given measurement object",
    const.AEC_DIAG_PARAM_SETERROR: "Parameter cannot be set",
    const.AEC_CNFG_WRONG_MODE: "Command not supported in current mode",
    const.AEC_CNFG_FILE_NOT_FOUND: "Specified file is not found",
    const.AEC_CNFG_FILE_INVALID: "File belongs to a different project",
    const.AEC_INVALID_SCR_HANDLE: "Invalid script handle",
    const.AEC_REMOVE_SCR_HANDLE: "Unable to remove script",
    const.AEC_ERROR_DECALRE_SCR: "Unable to declare script",
    const.AEC_ERROR_RESUME_SUPPORTED: "The requested module doesn't support resume mode",
    const.AEC_UNDEFINED_CHANNEL: "Undefined channel parameter",
    const.AEC_ERR_DRIVER_CONFIG: "No configuration for this driver type available",
    const.AEC_ERR_DCB_EXPORT: "Error creating DBC export file",
    const.AEC_NOT_AVAILABLE_WHILE_ACQ: "Function not available while a measurement is running",
    const.AEC_NOT_MISSING_LICENSE: "ILinkRT Recorder available only with option MCD3",
    const.AEC_EVENT_ALLREADY_REGISERED: "Callback event already registered",
    const.AEC_OBJECT_ALLREADY_DEFINED: "Measurement object already defined",
    const.AEC_CAL_NOT_ALLOWED: "Calibration not allowed if online calibration is switched off",
    const.AEC_DIAG_UNDEFINED_JOB: "Unknown diagnostic service",
    const.AEC_ERROR_MODAL_DIALOG: "Prohibited command while a modal dialog is prompted",
    const.AEC_ERROR_STRUCTURE_OBJECT: "Measurement object is already instantiated in a structure object",
    const.AEC_NETWORK_NOT_FOUND: "Network not found or not available",
    const.AEC_ERROR_LOADING_LABELLIST: "Error loading label list",
    const.AEC_ERROR_CONV_FILE_ACCESS: "Currently the converter has no file access",
    const.AEC_ERROR_COMPLEX_RESPONSES: "Function not available for complex responses",
    const.AEC_ERROR_INIPATH: "Function could not determine the project directory",
    const.AEC_USUPPORTED_INTERFACE_ID: "Interface name is not supported with this driver type",
    const.AEC_INSUFFICENT_BUFFERSIZE: "Buffer size too small",
    const.AEC_PATCHENTRY_NOT_FOUND: "Patch section not found",
    const.AEC_PATCHSECTION_NOT_FOUND: "Patch entry not found",
    const.AEC_SEC_MANAGER_ERROR: "Security manager access error",
    const.AEC_CHANNEL_OPTIMIZED: "Measurement channel is optimized",
}

# Error code to exception type mapping
_ERROR_EXCEPTION_MAP: Dict[int, type[CANapeError]] = {
    const.AEC_TIMEOUT_RESPONSE: CANapeTimeoutError,
    const.AEC_WRONG_CANAPE_VERSION: CANapeVersionError,
    const.AEC_INVALID_ASAP3_HDL: CANapeHandleError,
    const.AEC_INVALID_MODULE_HDL: CANapeModuleError,
    const.AEC_CALOBJ_READ_FAILED: CANapeCalibrationError,
    const.AEC_WRITE_VALUE_ERROR: CANapeCalibrationError,
    const.AEC_CAL_NOT_ALLOWED: CANapeCalibrationError,
    const.AEC_ACQUIS_ALREADY_RUNNING: CANapeDataAcquisitionError,
    const.AEC_ACQUIS_NOT_STARTED: CANapeDataAcquisitionError,
    const.AEC_ACQ_STP_INIT_FAILED: CANapeDataAcquisitionError,
    const.AEC_ACQ_STP_PROC_FAILED: CANapeDataAcquisitionError,
    const.AEC_ACQ_STP_OVERFLOW: CANapeDataAcquisitionError,
    const.AEC_ACQ_STP_TIME_OVER: CANapeDataAcquisitionError,
    const.AEC_NO_VALUES_SAMPLED: CANapeDataAcquisitionError,
    const.AEC_ACQ_CHNL_OVERRUN: CANapeDataAcquisitionError,
    const.AEC_NO_RASTER_OVERFLOW: CANapeDataAcquisitionError,
    const.AEC_FIFO_INTERNAL_ERROR: CANapeDataAcquisitionError,
    const.AEC_FIFO_ALREADY_INIT: CANapeDataAcquisitionError,
    const.AEC_EXIT_DENIED_WHILE_ACQU: CANapeDataAcquisitionError,
    const.AEC_NOT_AVAILABLE_WHILE_ACQ: CANapeDataAcquisitionError,
    const.AEC_OBJECT_ALLREADY_DEFINED: CANapeDataAcquisitionError,
    const.AEC_DIAG_INVALID_DRIVERTYPE: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_BUSMESSAGE: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_VARIANT: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_DIAGSERVICE: CANapeDiagnosticError,
    const.AEC_DIAG_ERR_EXECUTE_SERVICE: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_PARAMS: CANapeDiagnosticError,
    const.AEC_DIAG_UNKNOWN_PARAM_NAME: CANapeDiagnosticError,
    const.AEC_DIAG_EXCEPTION_ERROR: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_RESPONSE: CANapeDiagnosticError,
    const.AEC_DIAG_UNKNOWN_PARAM_TYPE: CANapeDiagnosticError,
    const.AEC_DIAG_NO_INFO_AVAILABLE: CANapeDiagnosticError,
    const.AEC_DIAG_UNKNOWN_RESPHANDLE: CANapeDiagnosticError,
    const.AEC_DIAG_WRONG_SERVICE_STATE: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_INDEX_SIZE: CANapeDiagnosticError,
    const.AEC_DIAG_INVALID_RESPONSETYPE: CANapeDiagnosticError,
    const.AEC_DIAG_UNDEFINED_JOB: CANapeDiagnosticError,
    const.AEC_DIAG_PARAM_SETERROR: CANapeDiagnosticError,
    const.AEC_SCRIPT_CMD_TO_LARGE: CANapeScriptingError,
    const.AEC_SCRIPT_CMD_INVALID: CANapeScriptingError,
    const.AEC_INVALID_SCR_HANDLE: CANapeScriptingError,
    const.AEC_REMOVE_SCR_HANDLE: CANapeScriptingError,
    const.AEC_ERROR_DECALRE_SCR: CANapeScriptingError,
    const.AEC_FLASH_INVALID_MANAGER: CANapeFlashError,
    const.AEC_FLASH_OBJ_OUT_OF_RANGE: CANapeFlashError,
    const.AEC_FLASH_MANAGER_ERROR: CANapeFlashError,
    const.AEC_FLASH_INVALID_APPNAME: CANapeFlashError,
    const.AEC_TCP_SERV_CONNECT_FAILED: CANapeNetworkError,
    const.AEC_TCP_MISSING_CFG: CANapeNetworkError,
    const.AEC_TCP_SERV_NOT_CONNECTED: CANapeNetworkError,
    const.AEC_NETWORK_NOT_FOUND: CANapeNetworkError,
    const.AEC_CNFG_WRONG_MODE: CANapeConfigurationError,
    const.AEC_CNFG_FILE_NOT_FOUND: CANapeConfigurationError,
    const.AEC_CNFG_FILE_INVALID: CANapeConfigurationError,
    const.AEC_CANAPE_CREATE_PROC_FAILED: CANapeInitializationError,
    const.AEC_INIT_COM_FAILED: CANapeInitializationError,
    const.AEC_INIT_CMD_FAILED: CANapeInitializationError,
    const.AEC_CANAPE_INVALID_PRG_PATH: CANapeInitializationError,
    const.AEC_WORKDIR_ACCESS_FAILED: CANapeInitializationError,
    const.AEC_NOSERVER_ERRCODE: CANapeInitializationError,
}


def decode_error_code(
    error_code: int, error_handling: Optional[Any] = None
) -> Tuple[str, type[CANapeError]]:
    """Decode CANape error code to Pythonic error message and exception type.

    This function attempts to get error text from the DLL's Asap3ErrorText
    function first, then falls back to the comprehensive error message dictionary.

    Parameters
    ----------
    error_code : int
        CANape error code (AEC_* constant).
    error_handling : Optional[Any], optional
        ASAP3ErrorHandling instance to use for Asap3ErrorText, by default None.

    Returns
    -------
    Tuple[str, type[CANapeError]]
        Tuple of (error_message, exception_type).
        - error_message: Human-readable error message
        - exception_type: Appropriate exception class for this error

    Examples
    --------
    >>> message, exc_type = decode_error_code(24)
    >>> message
    'Data acquisition already running'
    >>> exc_type
    <class 'CANapeDataAcquisitionError'>
    """
    # Try to get error text from DLL first (if available)
    if error_handling is not None and hasattr(error_handling, "Asap3ErrorText"):
        try:
            dll_message = error_handling.Asap3ErrorText(error_code)
            if dll_message:
                # Use DLL message, but still map to appropriate exception type
                exc_type = _ERROR_EXCEPTION_MAP.get(error_code, CANapeError)
                return (dll_message, exc_type)
        except Exception:
            # Fall through to dictionary lookup if DLL call fails
            pass

    # Fallback to dictionary lookup
    message = _ERROR_MESSAGES.get(
        error_code, f"Unknown CANape error (Error Code: {error_code})"
    )

    # Get appropriate exception type
    exc_type = _ERROR_EXCEPTION_MAP.get(error_code, CANapeError)

    return (message, exc_type)


def get_error_message(
    error_code: int,
    operation: str,
    error_handling: Optional[Any] = None,
) -> Tuple[str, type[CANapeError]]:
    """Get formatted error message with operation context.

    Parameters
    ----------
    error_code : int
        CANape error code (AEC_* constant).
    operation : str
        Name of the operation that failed (e.g., "start data acquisition").
    error_handling : Optional[Any], optional
        ASAP3ErrorHandling instance to use for Asap3ErrorText, by default None.

    Returns
    -------
    Tuple[str, type[CANapeError]]
        Tuple of (formatted_error_message, exception_type).
        Format: "Failed to {operation}: {decoded_message} (Error Code: {error_code})"

    Examples
    --------
    >>> message, exc_type = get_error_message(24, "start data acquisition")
    >>> message
    'Failed to start data acquisition: Data acquisition already running (Error Code: 24)'
    """
    decoded_message, exc_type = decode_error_code(error_code, error_handling)

    formatted_message = f"Failed to {operation}: {decoded_message} (Error Code: {error_code})"

    return (formatted_message, exc_type)

