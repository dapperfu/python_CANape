"""
Adapted from CANapAPI.h <Copyright (c) by Vector Informatik GmbH.  All rights reserved, where applicable>

The Python:

MIT License
-----------

Copyright (c) 2019 Jed Frey (https://github.com/jed-frey/)
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""
# Command not supported
AEC_CMD_NOT_SUP = 1

# Interface type not supported
AEC_INTERFACE_NOTSUPPORTED = 2

# Error creating memory mapped file
AEC_CREATE_MEM_MAPPED_FILE = 3

# Error writing data to memory mapped file
AEC_WRITE_CMD = 4

# Error reading response from memory mapped file
AEC_READ_RESPONSE = 5

# ASAP2 file not found
AEC_ASAP2_FILE_NOT_FOUND = 6

# Invalid module handle
AEC_INVALID_MODULE_HDL = 7

# Open file error
AEC_ERR_OPEN_FILE = 8

# Unknown object name
AEC_UNKNOWN_OBJECT = 9

# No database assigned
AEC_NO_DATABASE = 10

# Parameter
AEC_PAR_SIZE_OVERFLOW = 11

# Object has no write access
AEC_NOT_WRITE_ACCESS = 12

# Object type doens
AEC_OBJECT_TYPE_DOESNT_MATCH = 13

# Number of tasks overflow
AEC_NO_TASKS_OVERFLOW = 14

# Invalid CCP response size
AEC_CCP_RESPONSE_SIZE_INVALID = 15

# Timeout reading response from memory mapped file
AEC_TIMEOUT_RESPONSE = 16

# FIFO doesn
AEC_NO_VALUES_SAMPLED = 17

# Too many channels defined relating to single raster
AEC_ACQ_CHNL_OVERRUN = 18

# Too many rasters selected for data acquisition
AEC_NO_RASTER_OVERFLOW = 19

# CreateProcess of CANape failed
AEC_CANAPE_CREATE_PROC_FAILED = 20

# Asap3Exit denied because data acquistion is still running
AEC_EXIT_DENIED_WHILE_ACQU = 21

# Error writing data to application RAM
AEC_WRITE_DATA_FAILED = 22

# No response from ECU
AEC_NO_RESPONSE_FROM_ECU = 23

# Asap3StartDataAcquisition denied
AEC_ACQUIS_ALREADY_RUNNING = 24

# Asap3StopAcquisition denied
AEC_ACQUIS_NOT_STARTED = 25

# Invalid number of axis points
AEC_NO_AXIS_PTS_NOT_VALID = 27

# Script command size overflow
AEC_SCRIPT_CMD_TO_LARGE = 28

# Invalid
AEC_SCRIPT_CMD_INVALID = 29

# Unknown module
AEC_UNKNOWN_MODULE_NAME = 30

# CANape internal error concerning FIFO management
AEC_FIFO_INTERNAL_ERROR = 31

# Access denied
AEC_VERSION_ERROR = 32

# Illegal driver type
AEC_ILLEGAL_DRIVER = 33

# Read of calibration object failed
AEC_CALOBJ_READ_FAILED = 34

# Initialization of data acquisition failed
AEC_ACQ_STP_INIT_FAILED = 35

# Data acquisition failed
AEC_ACQ_STP_PROC_FAILED = 36

# Buffer overflow at data acquisition
AEC_ACQ_STP_OVERFLOW = 37

# Data acquisition stopped because selected time is elapsed
AEC_ACQ_STP_TIME_OVER = 38

# No Server application available
AEC_NOSERVER_ERRCODE = 40

# Unable to open data description file
AEC_ERR_OPEN_DATADESCFILE = 41

# Unable to open a data file
AEC_ERR_OPEN_DATAVERSFILE = 42

# Maximal count of displays are opened
AEC_TO_MUCH_DISPLAYS_OPEN = 43

# Attempt to create a module failed
AEC_INTERNAL_CANAPE_ERROR = 44

# Unable to open a display
AEC_CANT_OPEN_DISPLAY = 45

# No parameter filename
AEC_ERR_NO_PATTERNFILE_DEFINED = 46

# Unable to open patternfile
AEC_ERR_OPEN_PATTERNFILE = 47

# Release of a mutex failed
AEC_ERR_CANT_RELEASE_MUTEX = 48

# Canape does not fit to dll version
AEC_WRONG_CANAPE_VERSION = 49

# Connect to ASAP3 server failed
AEC_TCP_SERV_CONNECT_FAILED = 50

# Missing CANape TCP Server configuration
AEC_TCP_MISSING_CFG = 51

# Connection between ASAP3 Server and TCP CANapeAPI is not active
AEC_TCP_SERV_NOT_CONNECTED = 52

# The FIFO Memory was already created
AEC_FIFO_ALREADY_INIT = 54

# It is not possible to operate this command
AEC_ILLEGAL_OPERATION = 55

# The given type is not supported
AEC_WRONG_TYPE = 56

# CANape is not licensed
AEC_NO_CANAPE_LICENSE = 57

# Key
AEC_REG_OPEN_KEY_FAILED = 58

# Value
AEC_REG_QUERY_VALUE_FAILED = 59

# CreateProcess of CANape failed
AEC_WORKDIR_ACCESS_FAILED = 60

# Internal error
AEC_INIT_COM_FAILED = 61

# Negative Response from CANape
AEC_INIT_CMD_FAILED = 62

# CreateProcess of CANape failed
AEC_CANAPE_INVALID_PRG_PATH = 63

# Invalid asap3 handle
AEC_INVALID_ASAP3_HDL = 64

# File loading failed
AEC_LOADING_FILE = 65

# File saving failed
AEC_SAVING_FILE = 66

# Upload failed
AEC_UPLOAD = 67

# Value could not be written
AEC_WRITE_VALUE_ERROR = 68

# Other file transmission in process
AEC_TMTF_NOT_FINSHED = 69

# TransmitFile
AEC_TMTF_SEQUENCE_ERROR = 70

# TransmitFile
AEC_TDBO_TYPE_ERROR = 71

# Asap3_CCP_Request failed
AEC_EXECUTE_SERVICE_ERROR = 72

# Invalid drivertype for this operation
AEC_INVALID_DRIVERTYPE = 73

# Invalid drivertype for for diagnostic operations
AEC_DIAG_INVALID_DRIVERTYPE = 74

# Invalid BusMessage
AEC_DIAG_INVALID_BUSMESSAGE = 75

# Invalid Variant
AEC_DIAG_INVALID_VARIANT = 76

# Invalid or unknown request
AEC_DIAG_INVALID_DIAGSERVICE = 77

# Error while sending service
AEC_DIAG_ERR_EXECUTE_SERVICE = 78

# Invalid or unknown request
AEC_DIAG_INVALID_PARAMS = 79

# Invalid or unknown parameter name
AEC_DIAG_UNKNOWN_PARAM_NAME = 80

# Error while creating a request
AEC_DIAG_EXCEPTION_ERROR = 81

# Error response cannot be handled
AEC_DIAG_INVALID_RESPONSE = 82

# Unknown parameter type
AEC_DIAG_UNKNOWN_PARAM_TYPE = 83

# Currently no information available
AEC_DIAG_NO_INFO_AVAILABLE = 84

# Unknown response handle
AEC_DIAG_UNKNOWN_RESPHANDLE = 85

# The current request is in the wrong state for this operation
ACE_DIAG_WRONG_SERVICE_STATE = 86

# Complex index does not match
AEC_DIAG_INVALID_INDEX_SIZE = 87

# Invalid response type
AEC_DIAG_INVALID_RESPONSETYPE = 88

# Flash manager invalid
AEC_FLASH_INVALID_MANAGER = 89

# Flash object out of range
AEC_FLASH_OBJ_OUT_OF_RANGE = 90

# Flash manager error
AEC_FLASH_MANAGER_ERROR = 91

# Invalid application name
AEC_FLASH_INVALID_APPNAME = 93

# This function is not supported in this program version
AEC_FUNCTION_NOT_SUPPORTED = 94

# License file not found
AEC_LICENSE_NOT_FOUND = 95

# Recorder already exists
AEC_RECORDER_ALLREADY_EXISTS = 96

# Recorder does not exists
AEC_RECORDER_NOT_FOUND = 97

# Recorder index out of range
AEC_RECORDER_INDEX_OUTOFRANGE = 98

# Error deleting Recorder
AEC_REMOVE_RECORDER_ERR = 99

# Wrong parameter value
AEC_INVALID_PARAMETER = 100

# Error creating recorder
AEC_ERROR_CREATERECORDER = 101

# Error creating Filename
AEC_ERROR_SETRECFILENAME = 102

# Invalid task id for the given Measurement object
AEC_ERROR_INVALID_TASKID = 103

# Parameter can not be set
AEC_DIAG_PARAM_SETERROR = 104

# command not supported in current mode
AEC_CNFG_WRONG_MODE = 105

# Specified File is Not Found
AEC_CNFG_FILE_NOT_FOUND = 106

# File belongs to a different project
AEC_CNFG_FILE_INVALID = 107

# Invalid script handle
AEC_INVALID_SCR_HANDLE = 108

# Unable to remove Script
AEC_REMOVE_SCR_HANDLE = 109

# Unable to declare script
AEC_ERROR_DECALRE_SCR = 110

# The requested module doesn
AEC_ERROR_RESUME_SUPPORTED = 111

# undefined channel parameter
AEC_UNDEFINED_CHANNEL = 112

# No configuration for this drivertype available
AEC_ERR_DRIVER_CONFIG = 113

# Error creating DBC export file
AEC_ERR_DCB_EXPORT = 114

# Function not available while a measurement is running
ACE_NOT_AVAILABLE_WHILE_ACQ = 115

# ILinkRT Recorder available only with option MCD3
ACE_NOT_MISSING_LICENSE = 116

# Callback Event already registered
ACE_EVENT_ALLREADY_REGISERED = 117

# Measurement object already defined
AEC_OBJECT_ALLREADY_DEFINED = 118

# Calibration not allowed if online calibration is switched off
AEC_CAL_NOT_ALLOWED = 119

# Unknown service
AEC_DIAG_UNDEFINED_JOB = 120

# Prohibited command while a modal dialog is prompted
AEC_ERROR_MODAL_DIALOG = 121

# Measurement object is already instantiated in a structure object
AEC_ERROR_STRUCTURE_OBJECT = 123

# Network not found or not available
AEC_NETWORK_NOT_FOUND = 124

# Error loading label list
AEC_ERROR_LOADING_LABELLIST = 125

# Currently the converter has no file access
AEC_ERROR_CONV_FILE_ACCESS = 126

# Function not available for complex responses
AEC_ERROR_COMPLEX_RESPONSES = 127

# Function could not determine the project directory
AEC_ERROR_INIPATH = 128

# Interface name is not supported with this drivertype
AEC_USUPPORTED_INTERFACE_ID = 129

# Buffer size too small
AEC_INSUFFICENT_BUFFERSIZE = 130

# Patch section not found
AEC_PATCHENTRY_NOT_FOUND = 131

# Patch entry not found
AEC_PATCHSECTION_NOT_FOUND = 132

# Security manager access error
AEC_SEC_MANAGER_ERROR = 133

# Measurement channel is optimized because it
ACE_CHANNEL_OPTIMIZED = 134
