/*----------------------------------------------------------------------------
| Project:
|
| Description:
|    ASAP3-Interface
|    Version    : 1.0 28-AUG-2000
|
|-----------------------------------------------------------------------------
| Copyright (c) by Vector Informatik GmbH.  All rights reserved.
----------------------------------------------------------------------------*/
#pragma once

//disable deprecated warnings
#pragma warning(disable : 4996)

#include <pshpack1.h>

/** @defgroup definition Definitions
 *  List of definitions used in CANapeAPI and CANapeTCP interface.
 *  @{
 */

/*
NAN (not a number)
~~~~~~~~~~~~~~~~~~
The IEEE double precision floating point standard representation requires a 64 bit word,
which may be represented as numbered from 0 to 63, left to right. The first bit is
the sign bit, S, the next eleven bits are the exponent bits, 'E', and the final 52 bits
are the fraction 'F':

  S EEEEEEEEEEE FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
  0 1        11 12                                                63

  If E=2047 and F is nonzero, then V=NaN ("Not a number")
*/


#ifndef MATLABAPI
#ifndef _DOUBLE_NOTANUMBER_
#define _DOUBLE_NOTANUMBER_
  const union {
    unsigned char c[8];
    double d;
  } gDoubleNotANumber = { 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF }; // S = 0, E = 2047, F = all bits set

  const double DOUBLE_NOTANUMBER = gDoubleNotANumber.d;

  // must only be called with double variable, no expression!
  #define IS_DOUBLE_NOTANUMBER(_v_)  _isnan(_v_)

#endif // _DOUBLE_NOTANUMBER_
/** @} end of definition */
#endif  // MATLABAPI

/*
// ! Special Modulehandle for the CANape Environment HEXEDIT Driver
#define VMODULE_ENIRONMENT 0xFFFE
*/

/** @defgroup Errorcodes Error Codes
 *  If an Error occurs, after call of Asap3GetLastError one of these
 *  errornumber will return.
 *  @{
 */
#define AEC_CMD_NOT_SUP               1  //!< Command not supported
#define AEC_INTERFACE_NOTSUPPORTED    2  //!< Interface type not supported
#define AEC_CREATE_MEM_MAPPED_FILE    3  //!< Error creating memory mapped file
#define AEC_WRITE_CMD                 4  //!< Error writing data to memory mapped file
#define AEC_READ_RESPONSE             5  //!< Error reading response from memory mapped file
#define AEC_ASAP2_FILE_NOT_FOUND      6  //!< ASAP2 file not found
#define AEC_INVALID_MODULE_HDL        7  //!< Invalid module handle
#define AEC_ERR_OPEN_FILE             8  //!< Open file error
#define AEC_UNKNOWN_OBJECT            9  //!< Unknown object name
#define AEC_NO_DATABASE               10 //!< No database assigned
#define AEC_PAR_SIZE_OVERFLOW         11 //!< Parameter 'size' too large
#define AEC_NOT_WRITE_ACCESS          12 //!< Object has no write access
#define AEC_OBJECT_TYPE_DOESNT_MATCH  13 //!< Object type doens't match
#define AEC_NO_TASKS_OVERFLOW         14 //!< Number of tasks overflow
#define AEC_CCP_RESPONSE_SIZE_INVALID 15 //!< Invalid CCP response size
#define AEC_TIMEOUT_RESPONSE          16 //!< Timeout reading response from memory mapped file
#define AEC_NO_VALUES_SAMPLED         17 //!< FIFO doesn't contain any values
#define AEC_ACQ_CHNL_OVERRUN          18 //!< Too many channels defined relating to single raster
#define AEC_NO_RASTER_OVERFLOW        19 //!< Too many rasters selected for data acquisition (overflow of internal parameter)
#define AEC_CANAPE_CREATE_PROC_FAILED 20 //!< CreateProcess of CANape failed
#define AEC_EXIT_DENIED_WHILE_ACQU    21 //!< Asap3Exit denied because data acquistion is still running
#define AEC_WRITE_DATA_FAILED         22 //!< Error writing data to application RAM
#define AEC_NO_RESPONSE_FROM_ECU      23 //!< No response from ECU (attach Asap2 failed)
#define AEC_ACQUIS_ALREADY_RUNNING    24 //!< Asap3StartDataAcquisition denied: data acquisition already running
#define AEC_ACQUIS_NOT_STARTED        25 //!< Asap3StopAcquisition denied: data acquisition not started
// #define AEC_VALUES_NOT_ACCESSIBLE     26 // If cache is disabled, values aren't accessible while acquisition is running

#define AEC_NO_AXIS_PTS_NOT_VALID     27 //!< Invalid number of axis points (see following note).
// Note: While acquisition is running the number of axis points of particular
//       maps/curves cannot be determined. Only those maps/curves are affected whose
//       number of axis points is deposited at ECU-memory.
// Workaround: Please read map/curve once before start of acquisition.

#define AEC_SCRIPT_CMD_TO_LARGE       28  //!< Script command size overflow
#define AEC_SCRIPT_CMD_INVALID        29  //!< Invalid/unknown script command
#define AEC_UNKNOWN_MODULE_NAME       30  //!< Unknown module
#define AEC_FIFO_INTERNAL_ERROR       31  //!< CANape internal error concerning FIFO management
#define AEC_VERSION_ERROR             32  //!< Access denied: incompatible CANape version
#define AEC_ILLEGAL_DRIVER            33  //!< Illegal driver type
#define AEC_CALOBJ_READ_FAILED        34  //!< Read of calibration object failed
#define AEC_ACQ_STP_INIT_FAILED       35  //!< Initialization of data acquisition failed
#define AEC_ACQ_STP_PROC_FAILED       36  //!< Data acquisition failed
#define AEC_ACQ_STP_OVERFLOW          37  //!< Buffer overflow at data acquisition
#define AEC_ACQ_STP_TIME_OVER         38  //!< Data acquisition stopped because selected time is elapsed

#define AEC_NOSERVER_ERRCODE          40  //!< No Server application available
#define AEC_ERR_OPEN_DATADESCFILE     41  //!< Unable to open data description file, may be nonexistent
#define AEC_ERR_OPEN_DATAVERSFILE     42  //!< Unable to open a data file
#define AEC_TO_MUCH_DISPLAYS_OPEN     43  //!< Maximal count of displays are opened
#define AEC_INTERNAL_CANAPE_ERROR     44  //!< Attempt to create a module failed
#define AEC_CANT_OPEN_DISPLAY         45  //!< Unable to open a display
#define AEC_ERR_NO_PATTERNFILE_DEFINED 46 //!< No parameter filename
#define AEC_ERR_OPEN_PATTERNFILE      47  //!< Unable to open patternfile
#define AEC_ERR_CANT_RELEASE_MUTEX    48  //!< Release of a mutex failed
#define AEC_WRONG_CANAPE_VERSION      49  //!< Canape does not fit to dll version

#define AEC_TCP_SERV_CONNECT_FAILED   50  //!< Connect to ASAP3 server failed
#define AEC_TCP_MISSING_CFG           51  //!< Missing CANape TCP Server configuration
#define AEC_TCP_SERV_NOT_CONNECTED    52  //!< Connection between ASAP3 Server and TCP CANapeAPI is not active
#define AEC_TCP_EXIT_NOTCLOSED        53
#define AEC_FIFO_ALREADY_INIT         54  //!< The FIFO Memory was already created. Close all conections to reconfigure.
#define AEC_ILLEGAL_OPERATION         55  //!< It is not possible to operate this command
#define AEC_WRONG_TYPE                56  //!< The given type is not supported
#define AEC_NO_CANAPE_LICENSE         57  //!< CANape is not licensed
#define AEC_REG_OPEN_KEY_FAILED       58  //!< Key "HKEY_LOCAL_MACHINE\\SOFTWARE\\VECTOR\\CANape" missing at Windows Registry, maybe CANape setup has not been correctly performed
#define AEC_REG_QUERY_VALUE_FAILED    59  //!< Value "Path" missing at Windows Registry, maybe CANape setup has not been correctly performed
#define AEC_WORKDIR_ACCESS_FAILED     60  //!< CreateProcess of CANape failed: working directory not accessible/exists
#define AEC_INIT_COM_FAILED           61  //!< Internal error: Asap3InitCom() failed
#define AEC_INIT_CMD_FAILED           62  //!< Negative Response from CANape: Init() failed
#define AEC_CANAPE_INVALID_PRG_PATH   63  //!< CreateProcess of CANape failed: programme directory not accessible/nonexistent
#define AEC_INVALID_ASAP3_HDL         64  //!< Invalid asap3 handle
#define AEC_LOADING_FILE              65  //!< File loading failed
#define AEC_SAVING_FILE               66  //!< File saving failed
#define AEC_UPLOAD                    67  //!< Upload failed
#define AEC_WRITE_VALUE_ERROR         68  //!< Value could not be written
#define AEC_TMTF_NOT_FINSHED          69  //!< Other file transmission in process
#define AEC_TMTF_SEQUENCE_ERROR       70  //!< TransmitFile: sequence error (internal error)
#define AEC_TDBO_TYPE_ERROR           71  //!< TransmitFile: sequence error (internal error)
#define AEC_EXECUTE_SERVICE_ERROR     72  //!< Asap3_CCP_Request failed
#define AEC_INVALID_DRIVERTYPE        73  //!< Invalid drivertype for this operation

///////////////// Diagnostic Errors
#define AEC_DIAG_INVALID_DRIVERTYPE   74  //!< Invalid drivertype for for diagnostic operations
#define AEC_DIAG_INVALID_BUSMESSAGE   75  //!< Invalid BusMessage
#define AEC_DIAG_INVALID_VARIANT      76  //!< Invalid Variant
#define AEC_DIAG_INVALID_DIAGSERVICE  77  //!< Invalid or unknown request
#define AEC_DIAG_ERR_EXECUTE_SERVICE  78  //!< Error while sending service
#define AEC_DIAG_INVALID_PARAMS       79  //!< Invalid or unknown request
#define AEC_DIAG_UNKNOWN_PARAM_NAME   80  //!< Invalid or unknown parameter name
#define AEC_DIAG_EXCEPTION_ERROR      81  //!< Error while creating a request
#define AEC_DIAG_INVALID_RESPONSE     82  //!< Error response cannot be handled
#define AEC_DIAG_UNKNOWN_PARAM_TYPE   83  //!< Unknown parameter type
#define AEC_DIAG_NO_INFO_AVAILABLE    84  //!< Currently no information available
#define AEC_DIAG_UNKNOWN_RESPHANDLE   85  //!< Unknown response handle
#define ACE_DIAG_WRONG_SERVICE_STATE  86  //!< The current request is in the wrong state for this operation
#define AEC_DIAG_INVALID_INDEX_SIZE   87  //!< Complex index does not match
#define AEC_DIAG_INVALID_RESPONSETYPE 88  //!< Invalid response type

#define AEC_FLASH_INVALID_MANAGER     89  //!< Flash manager invalid
#define AEC_FLASH_OBJ_OUT_OF_RANGE    90  //!< Flash object out of range
#define AEC_FLASH_MANAGER_ERROR       91  //!< Flash manager error
#define AEC_FLASH_ALLREADY_RUNNING    92
#define AEC_FLASH_INVALID_APPNAME     93  //!< Invalid application name


#define AEC_FUNCTION_NOT_SUPPORTED    94  //!< This function is not supported in this program version
#define AEC_LICENSE_NOT_FOUND         95  //!< License file not found


#define AEC_RECORDER_ALLREADY_EXISTS  96  //!< Recorder already exists
#define AEC_RECORDER_NOT_FOUND        97  //!< Recorder does not exists
#define AEC_RECORDER_INDEX_OUTOFRANGE 98  //!< Recorder index out of range
#define AEC_REMOVE_RECORDER_ERR       99  //!< Error deleting Recorder
#define AEC_INVALID_PARAMETER        100  //!< Wrong parameter value
#define AEC_ERROR_CREATERECORDER     101  //!< Error creating recorder
#define AEC_ERROR_SETRECFILENAME     102  //!< Error creating Filename


#define AEC_ERROR_INVALID_TASKID     103  //!< Invalid task id for the given Measurement object
#define AEC_DIAG_PARAM_SETERROR      104  //!< Parameter can not be set

#define AEC_CNFG_WRONG_MODE          105  //!< command not supported in current mode
#define AEC_CNFG_FILE_NOT_FOUND      106  //!< Specified File is Not Found
#define AEC_CNFG_FILE_INVALID        107  //!< File belongs to a different project

#define AEC_INVALID_SCR_HANDLE       108  //!< Invalid script handle
#define AEC_REMOVE_SCR_HANDLE        109  //!< Unable to remove Script
#define AEC_ERROR_DECALRE_SCR        110  //!< Unable to declare script

#define AEC_ERROR_RESUME_SUPPORTED   111  //!< The requested module doesn't support resume mode
#define AEC_UNDEFINED_CHANNEL        112  //!< undefined channel parameter
#define AEC_ERR_DRIVER_CONFIG        113  //!< No configuration for this drivertype available

#define AEC_ERR_DCB_EXPORT           114  //!< Error creating DBC export file
#define ACE_NOT_AVAILABLE_WHILE_ACQ  115  //!< Function not available while a measurement is running

#define ACE_NOT_MISSING_LICENSE      116  //!< ILinkRT Recorder available only with option MCD3
#define ACE_EVENT_ALLREADY_REGISERED 117  //!< Callback Event already registered
#define AEC_OBJECT_ALLREADY_DEFINED  118  //!< Measurement object already defined
#define AEC_CAL_NOT_ALLOWED          119  //!< Calibration not allowed if online calibration is switched off

#define AEC_DIAG_UNDEFINED_JOB       120  //!< Unknown service

#define AEC_ERROR_MODAL_DIALOG       121  //!< Prohibited command while a modal dialog is prompted
#define AEC_ERROR_CHANNEL_ASSIGNMENT 122  //!<wrong hardware channel assignment"
#define AEC_ERROR_STRUCTURE_OBJECT   123  //!< Measurement object is already instantiated in a structure object

#define AEC_NETWORK_NOT_FOUND        124  //!< Network not found or not available
#define AEC_ERROR_LOADING_LABELLIST  125  //!< Error loading label list

#define AEC_ERROR_CONV_FILE_ACCESS   126  //!< Currently the converter has no file access - please try it later
#define AEC_ERROR_COMPLEX_RESPONSES  127  //!< Function not available for complex responses

#define AEC_ERROR_INIPATH            128  //!< Function could not determine the project directory
#define AEC_USUPPORTED_INTERFACE_ID  129  //!< Interface name is not supported with this drivertype

#define AEC_INSUFFICENT_BUFFERSIZE   130  //!< Buffer size too small
#define AEC_PATCHENTRY_NOT_FOUND     131  //!< Patch section not found
#define AEC_PATCHSECTION_NOT_FOUND   132  //!< Patch entry not found

#define AEC_SEC_MANAGER_ERROR        133  //!< Security manager access error
#define ACE_CHANNEL_OPTIMIZED        134  //!< Measurement channel is optimized because it's parent will already be measured

#define ACE_ERR_PROFILE_ID           135  //!< Profile not registered
#define ACE_ERR_UNSUPPORTED_TYPE     136  //!< Unsupported datataype for measurement

#define AEC_LAST_ERRCODE             137 // in client.CPP erweitern, wenn neue Fehlercodes hinzukommen

/** @} end of Errorcodes */


enum TApplicationType 
{
  eUNDEFINED   = 0,
  eCANAPE      = 1,    //!< Identification for CANape
  eAPPLOCATION = 3     //!< Identification to Start the application with a given path and executable file
};


//! Type definition for TScriptStatus
enum TScriptStatus
{
  eTScrReady = 1,      //!< Initial status after creation of the task
  eTScrStarting,       //!< Waiting in the list for execution
  eTScrRunning,        //!< Status if task was not finished in one Eval step
  eTScrSleeping,       //!< Function contained Sleep function
  eTScrSuspended,      //!< Suspended by user
  eTScrTerminated,     //!< Terminated by user
  eTScrFinishedReturn, //!< Successful finish, Return value available
  eTScrFinishedCancel, //!< Successful finish, No Return value
  eTScrFailure,        //!< Failure
  eTScrTimeout         //!< Terminated due to timeout
};

//! possible Modes for pageswitching
enum e_RamMode
{
  e_TR_MODE_RAM=      0, //!< Switch to RAM page
  e_TR_MODE_ROM=      1  //!< Switch to ROM page
};


//! Typedefinition for Recordertypes
enum TRecorderType
{
  eTRecorderTypeMDF                  = 0, //!< MDF Recorder type
  eTRecorderTypeILinkRT              = 1, //!< ILinkRT Recorder type
  eTRecorderTypeBLF                  = 2  //!< ILinkRT Recorder type
};


//! Typedefinition for Callback Event IDs
enum ASAP3_EVENT_CODE
{
  et_ON_DATA_ACQ_START,              //!< Callback ID to register the event onMeasurementStart
  et_ON_DATA_ACQ_STOP,               //!< Callback ID to register the event onMeasurementStop
  et_ON_BEFORE_DATA_ACQ_START,       //!< Callback ID to register the event before Measurement starts
  et_ON_CLOSEPROJECT,                //!< Callback ID to register if a new Project is closed
  et_ON_OPENPROJECT,                 //!< Callback ID to register if a new Project is opened
  et_ON_CLOSECANAPE                  //!< Callback ID to register when CANape will be closed
};

/** @} end of enumeration */

struct TApplicationID
{
 TApplicationType tApplicationType;
 char             tApplicationPath[_MAX_PATH];
};

/** @defgroup enumeration Enumerations
 *  If an Error occurs, after call of Asap3GetLastError one of these
 *  error number will return.
 *  @{
 */

//! Format of ECU measurement or calibration data
enum TFormat
{
  ECU_INTERNAL = 0,                 //!< HEX: ECU-internal data format
  PHYSICAL_REPRESENTATION = 1,      //!< PHYS: physical value including unit
};


//! Valid types of ECU measurement or calibration data
enum TValueType
{
  VALUE  = 0, //!< Represents scalar object
  CURVE  = 1, //!< Represents curve object
  MAP    = 2, //!< Represents map object
  AXIS   = 3, //!< Represents axis object
  ASCII  = 4, //!< Represents ASCII string object
  VAL_BLK= 5  //!< Represents ValueBlock
};


//! Selector to declare an object to be used for measurement or calibration
enum TObjectType 
{
  OTT_MEASURE   = 0, //!< Represents Measurement objects
  OTT_CALIBRATE = 1, //!< Represents Calibration and writable Measurement objects
  OTT_UNKNOWN   = 2  //!< fall back value - should not appear!
};

//! possible states for diagnostic services
enum eServiceStates
{
 e_Created  =10,             //!< Service is created but not send
 e_Running  =e_Created +10,  //!< Service is created and send
 e_Finished =e_Running +10,  //!< Service is still running -> no response received
 e_TimeOut  =e_Finished+10   //!< Service is created and send but a timeout occurred while CANape was waiting for response
};
/** @} end of enumeration */

//! Handle for Diagnostic Services
typedef unsigned long TAsap3DiagHdl;

#ifndef EnParamType
//! types of responseparameters

/** @defgroup enumeration Enumerations
 *  @{
 */
//! possible states of the Recorder
enum EnRecorderState
{
 e_RecConfigure, //!< Recorder is configured
 e_RecActive,    //!< Recorder is active and ready to run
 e_RecRunning,   //!< Recorder is running
 e_RecPaused,    //!< Recorder paused but measurement is still running
 e_Suspended     //!< Recorder has stopped
};

//! possible states of a diagnostic response parameter
enum EnParamType
{
  ParamSigned     = 1, //!< Parameter value is signed
  ParamDouble     = 2, //!< Parameter value double
  ParamBCD        = 3, //!< not supported in CANape
  ParamUnsigned   = 4, //!< Parameter value is unsigned
  ParamFloat      = 5, //!< Parameter value float
  ParamAutoDetect = 6  //!< Parameter type assignment by CANape automatically

};
/** @} end of enumeration */

/** @defgroup structs Structures
 *  @{
 */
//! structure DiagJobResponse used in function \link Asap3DiagExecuteJob \endlink
struct DiagJobResponse
{
  char   *job_responsestring; //!< Response string of the diagnostic Job if defined
  double  job_responseValue;  //!< Response value of the diagnostic Job if defined
};



//! structure NumericParameter used in the functions \n \link Asap3DiagSetNumericParameter \endlink \n \link Asap3DiagGetNumericResponseParameter \endlink and \n \link Asap3DiagGetComplexNumericResponseParameter \endlink \n
struct DiagNumericParameter
{
 EnParamType DiagNumeric; //!< Identification of the PValue data type

 //!> union to transport numeric diagnostic parameters
 union PValues
 {
  int           IVal;  //!< corresponding union parameter for type ParamSigned
  unsigned int  UIVal; //!< corresponding union parameter for type ParamUnsigned
  float         FVal;  //!< corresponding union parameter for type ParamFloat
  double        DVal;  //!< corresponding union parameter for type ParamDouble
 };
 PValues Values;
};

//! structure which is a parameter  of the callback function FNCDIAGNOTIFICATION
struct DiagNotificationStruct
{
 TAsap3DiagHdl  DiagHandle;    //!< Handle of the corresponding request
 eServiceStates DiagState;     //!< current state of the request
 void          *PrivateData;   //!< user defined private data
};

/********************** Struct to retrieve the object entries from the measurement list*****************************/
//! structure MeasurementListEntry used in the functions is a member of the structure MeasurementListEntries
// SSR-BEGIN
struct TMeasurementListEntry// SSR-APPEND:_stream
{
 unsigned short  taskId;    //!< assigned Task id of the measurement object
 unsigned long   rate;      //!< assigned rate of the measurement object in ms
 BOOL            SaveFlag;  //!< TRUE is the measurement object will be saved in the MDF file, otherwise FALSE
 BOOL            Disabled;  //!< TRUE is the measurement object is enabled for measurement, otherwise FALSE
 #if 1// SSR-REPLACE: #if 0
 char           *ObjectName;//!< Label name of the measurement object
 #else
 TReservedOffset_stream ObjectName;
 #endif
};
// SSR-END

//! structure MeasurementListEntries used in the functions \n \link Asap3GetMeasurementListEntries \endlink \n

struct MeasurementListEntries
{
 unsigned int ItemCount;            //!< count of \link MeasurementListEntry \endlink items
 TMeasurementListEntry **Entries;   //!< \link MeasurementListEntry \endlink array
};

//! structure DBObjectInfo used in the functions \n \link Asap3GetDBObjectInfo \endlink \n

typedef struct DBObjectInfo
{
  TObjectType  DBObjecttype; //!< Type of the Object
  TValueType type;           //!< ValueType of the Object // scalar etc.
  double     min;            //!< Min Limit
  double     max;            //!< Max Limit
  double     minEx;          //!< ext. Min Limit
  double     maxEx;          //!< ext. Max Limit
  BYTE       precision;      //!< count of digits (decimal place)
  char       unit[MAX_PATH]; //!< Object Unit
}DBObjectInfo;

//! structure DBFileInfo used in the functions \n \link Asap3GetDatabaseInfo \endlink \n
struct  DBFileInfo  //! DBFileInfo structure
{
  char asap2Fname[MAX_PATH]; //!< name of the Database file
  char asap2Path[MAX_PATH];  //!< path of the Database file
  BYTE type;                /*!< type of the Database file: \n  UNKNOWN      = 0,ASAP2        = 1,DB           = 2,DBB          = 3,DBC          = 4,CANDELA      = 5,
                                                              ODF          = 6,EDS          = 7,EHR          = 8,ROB          = 9,LST          = 10,LDF          = 11,
                                                              CDM          = 12,MDF          = 13,XML          = 14,Update       = 15,CDP          = 16,LostVariable = 17,
                                                              PDX          = 18,\n AutosarXML   = 19,System       = 20,Anonymous    = 21*/


};

// Coefficients approach to process the ASAP2-record-layouts
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

struct TLayoutCoeffs
{
  short OffNx;    //!< Address offset of 'number of X-axis coordinates' (= -1, if constant)
  short OffNy;    //!< Address offset of 'number of Y-axis coordinates' (= -1, if constant)

  short OffX;     //!< Address offset of 'X-axis coordinates'
  short FakX;     //!< Factor of 'X-axis coordinates'

  short OffY;     //!< Address offset of 'Y-axis coordinates'
  short FakY;     //!< Factor of 'Y-axis coordinates'

  short OffW;     //!< Address offset of result values
  short FakWx;    //!< X-factor of result values
  short FakWy;    //!< Y-factor of result values
};
/*!   Address( NumberOfXAxisCoordinates ) = Object_Baseaddress + OffNx
*
*     Address( NumberOfYAxisCoordinates ) = Object_Baseaddress + OffNy
*
*     Address( XAxisCoordinate(ix) ) = Object_Baseaddress + OffX + (ix * FakX)
*             where   ix = ´{0...n-1}
*
*     Address( YAxisCoordinate(iy) ) = Object_Baseaddress + OffY + (iy * FakY)
*             where   iy = ´{0...m-1}
*
*     Address( ResultValue(ix, iy) ) = Object_Baseaddress + OffW + (ix * FakWx) + (iy * FakWy)
*             where   ix = ´{0...n-1} and  iy = ´{0...m-1}
*/


//! structure SecurityProfileEntry used in the functions \n \link Asap3GetSecurityProfileInfo \endlink \n
struct SecProfileEntry         //! SecurityProfileEntry structure
{
  unsigned int mId;            //!< profile identifier
  char mName[MAX_PATH];        //!< name of the profile file
  char mDescription[MAX_PATH]; //!< profile description
};


/** @} end of structs */

//! callback function to notify the client if a state change occurs
//!< sizeofstruct : size of DiagNotificationStruct structure
typedef long (CALLBACK* FNCDIAGNOFIFICATION)(unsigned long sizeofstruct, DiagNotificationStruct*);

#endif

/** @defgroup structs Structures
 *  @{
 */

// Remark to the following definition of calibrationObjectValue_t
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/*! <em>In case of verbal conversion table 'values' / 'xAxis' / 'yAxis' always
 *  contains the ECU-internal value.</em>
 *
 *  The value TValueType  contains the type of the object.
 *  4 different types are possible.
 *  <ul><li>value<br> A simple value.
 *  <li>axis<br> Describes an axis.
 *      <ul><li><em>dimension</em><br>Size of the pAxis array/number of values
 *          <li><em>pAxis</em><br>Array with values of the axis
 *      </ul>
 *
 *  <li>curve<br> Describes a curve with a x-axis.
 *      <ul><li><em>dimension</em><br>Size of the pAxis and the pValues array/number of values
 *          <li><em>pAxis</em><br>Array with values of the axis
 *          <li><em>pValues</em><br>Array with sequential arranged values.
 *          <li><em>\image HTML curvearrange.gif  curve & axis</em><br>
 *      </ul>
 *
 *
 *   <li>map<br> Describes a map with a x-axis and y-axis.
 *      <ul><li><em>xDimension</em><br>Size of the pXAxis and the pXValues array/number of values
 *          <li><em>yDimension</em><br>Size of the pYAxis and the pYValues array/number of values
 *          <li><em>pXAxis</em><br>Array with values of the x-axis
 *          <li><em>pYAxis</em><br>Array with values of the y-axis
 *          <li><em>pValues</em><br>Array with sequential arranged values. The rows are one after the other.
 *         <li><em>\image HTML maparrange.gif  map</em><br>
*      </ul>
  *
 * </ul>
 *
 */


 // SSR-BEGIN
typedef union { // TCalibrationObjectValueEx

  TValueType type;

  struct {
    TValueType type;

    double value; //!< ECU-internal value or physical value
  } value;        //!< Single value (Kennwert)

  struct {
    TValueType type; //!< Shared axis

    short dimension;        //!< Number of elements
    #if 1// SSR-REPLACE:    #if 0
    double*       pAxis;    //!< Axis coordinates of curve (ECU-internal value or physical value)
    #else
    TReservedOffset_stream axis;
    #endif
    unsigned long oAxis;    //!< Reserved
  } axis;      //!< Array of axis coordinates

  struct {        // completely identical to struct axis, union should be compatible
    TValueType type;        //!< ASCII string,

    short len;              //!< Number of characters
    #if 1// SSR-REPLACE:    #if 0
    char*         pAscii;   //!< Ascii string
    #else
    TReservedOffset_stream ascii;
    #endif
    unsigned long oAscii;   //!< Reserved
  } ascii;      //!< Array of characters

  struct {
    TValueType type;

    short dimension;        //!< Number of elements
    #if 1// SSR-REPLACE:    #if 0
    double*       pAxis;    //!< Axis coordinates of curve (ECU-internal value or physical value)
    #else
    TReservedOffset_stream axis;
    #endif
    unsigned long oAxis;    //!< Reserved
    #if 1// SSR-REPLACE:    #if 0
    double*       pValues;  //!< Output values of curve (ECU-internal value or physical value)
    #else
    TReservedOffset_stream values;
    #endif
    unsigned long oValues;  //!< Reserved
  } curve;     //!< Array of value pairs comprising an axis coordinate and a corresponding output value.

  struct {
    TValueType type;

    short xDimension;      //!< Number of elements = xDimension + yDimension
    short yDimension;      //!< Number of elements = xDimension + yDimension
    #if 1// SSR-REPLACE:    #if 0
    double*       pXAxis;  //!< X-axis coordinates of the map (ECU-internal value or physical value).
    unsigned long oXAxis;  //!< Reserved
    double*       pYAxis;  //!< Y-axis coordinates of the map (ECU-internal value or physical value).
    unsigned long oYAxis;  //!< Reserved
    double*       pValues; //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
    unsigned long oValues; //!< Reserved
    #else
    TReservedOffset_stream xAxis;
    unsigned long oXAxis;
    TReservedOffset_stream yAxis;
    unsigned long oYAxis;
    TReservedOffset_stream values;
    unsigned long oValues;
    #endif
  } map;       //!< 2 arrays of X- and Y-axis-coordinates respectively and a 2-dimensional matrix of output values

  struct {
    TValueType type;

    short xDimension;      //!< Number of elements = xDimension + yDimension
    short yDimension;      //!< Number of elements = xDimension + yDimension
#if 1// SSR-REPLACE:    #if 0
    double*       values;  //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
    unsigned long oValues; //!< Reserved
#else
    TReservedOffset_stream values;
    unsigned long oValues;
#endif
  } valblk;
}
TCalibrationObjectValueEx// SSR-APPEND:_stream
;
// SSR-END

// SSR-BEGIN
typedef struct // TCalibrationObjectValueEx2
{
  #if 1// SSR-REPLACE:  #if 0
  double        * xAxisValues; //!< X-axis coordinates of the map (ECU-internal value or physical value).
  double        * yAxisValues; //!< Y-axis coordinates of the map (ECU-internal value or physical value).
  double        * zValues;     //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
  double        * zValue;      //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
  #else
  TReservedOffset_stream xAxisValues;
  TReservedOffset_stream yAxisValues;
  TReservedOffset_stream zValues;
  TReservedOffset_stream zValue;
  #endif
  unsigned long   xStart;      //!< Reserved
  unsigned long   yStart;      //!< Reserved
  unsigned long   xSize;       //!< Reserved
  unsigned long   ySize;       //!< Reserved
}
TCalibrationObjectValueEx2// SSR-APPEND:_stream
;
// SSR-END

// SSR-BEGIN
typedef union { // TCalibrationObjectValue

  TValueType type;

  struct {
    TValueType type;

    double value; //!< ECU-internal value or physical value
  } value;        //!< Single value

  struct {
    TValueType type; //!< Shared axis

    short dimension;       //!< Number of elements
    #if 1// SSR-REPLACE:    #if 0
    double*       axis;    //!< Axis coordinates of curve (ECU-internal value or physical value)
    #else
    TReservedOffset_stream axis;
    #endif
  } axis;      //!< Array of axis coordinates

  struct {        // completely identical to struct axis, union should be compatible
    TValueType type;        //!< ASCII string,

    short len;              //!< Number of characters
    #if 1// SSR-REPLACE:    #if 0
    char*          ascii;   //!< Ascii string
    #else
    TReservedOffset_stream ascii;
    #endif
  } ascii;      //!< Array of characters

  struct {
    TValueType type;

    short dimension;        //!< Number of elements
    #if 1// SSR-REPLACE:    #if 0
    double*       axis;    //!< Axis coordinates of curve (ECU-internal value or physical value)
    double*       values;  //!< Output values of curve (ECU-internal value or physical value)
    #else
    TReservedOffset_stream        axis;
    TReservedOffset_stream        values;
    #endif
  } curve;     //!< Array of value pairs comprising an axis coordinate and a corresponding output value.

  struct {
    TValueType type;

    short xDimension;      //!< Number of elements = xDimension + yDimension
    short yDimension;      //!< Number of elements = xDimension + yDimension
    #if 1// SSR-REPLACE:    #if 0
    double*       xAxis;  //!< X-axis coordinates of the map (ECU-internal value or physical value).
    double*       yAxis;  //!< Y-axis coordinates of the map (ECU-internal value or physical value).
    double*       values; //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
    #else
    TReservedOffset_stream        xAxis;
    TReservedOffset_stream        yAxis;
    TReservedOffset_stream        values;
    #endif
  } map;       //!< 2 arrays of X- and Y-axis-coordinates respectively and a 2-dimensional matrix of output values

  struct {
    TValueType type;

    short xDimension;      //!< Number of elements = xDimension + yDimension
    short yDimension;      //!< Number of elements = xDimension + yDimension
#if 1// SSR-REPLACE:    #if 0
    double*       values; //!< Output values of the map deposited in rows (ECU-internal  value or physical value).
#else
    TReservedOffset_stream        values;
#endif
  } valblk;
}
TCalibrationObjectValue// SSR-APPEND:_stream
;
// SSR-END


//! Basic information about the available acquisition tasks.\see Asap3GetEcuTasks()
 /*!  The tasks are defined at the ASAP2 File.
  *   Some predefined tasks are added to the list by CANape (mode polling and cycle)
 */
// SSR-BEGIN
typedef struct { // TTaskInfo
  #if 1// SSR-REPLACE:  #if 0
  const char     *description;  //!< Description text
  #else
  TReservedOffset_stream description;
  #endif
  unsigned short  taskId;       //!< Identification number. The task Id is dynamically generated by CANape depending on internal definitions.
  unsigned long   taskCycle;    /*!< Cycle rate in msec 0 if not a cyclic task or unknown.
                                      In case of modes polling or cycle this parameter has no sense.*/
}
TTaskInfo// SSR-APPEND:_stream
;
// SSR-END


//! Basic information about the available mdf converter.\see Asap3GetEcuTasks()

struct TConverterInfo
{ 
  char Comment[_MAX_PATH];  //!< comment text
  char Name   [_MAX_PATH];  //!< Converter name.
  char ID     [_MAX_PATH];  //!< Identification id.
};


//! Basic information about the available acquisition tasks.\see Asap3GetEcuTasks()
 /*!  The tasks are defined at the ASAP2 File.
  *   Some predefined tasks are added to the list by CANape (mode polling and cycle)
 */
// SSR-BEGIN
typedef struct {
  #if 1// SSR-REPLACE:  #if 0
  const char     *description;  //!< Description text
  #else
  TReservedOffset_stream description;
  #endif
  unsigned short  taskId;       //!< Identification number. The task Id is dynamically generated by CANape depending on internal definitions.
  unsigned long   taskCycle;    /*!< Cycle rate in msec 0 if not a cyclic task or unknown.
                                      In case of modes polling or cycle this parameter has no sense.*/
  unsigned long   eventChannel;
}
TTaskInfo2// SSR-APPEND:_stream
;
// SSR-END

/** @} end of structs */

/** @defgroup enumeration Enumerations
 *  @{
 */

 //! possible states for diagnostic services
typedef enum  {
  TYPE_FILE,         //!< Destination File (Hex file)
  TYPE_VIRTUAL,      //!< Destination Memory
  TYPE_PHYSICAL      //!< Destination Memory ECU
} TAsap3FileType;

//! possible On-Offline states of the ECU
typedef enum {

  TYPE_SWITCH_ONLINE,  //!< Switches the ECU state from offline to online
  TYPE_SWITCH_OFFLINE, //!< Switches the ECU state from online to offline
}TAsap3ECUState;

//! possible data types of characteristic objects
typedef enum {
  TYPE_UNKNOWN, //!< Default value - should not occur
  TYPE_INT,     //!< Characteristic Object is type of integer
  TYPE_FLOAT,   //!< Characteristic Object is type of float
  TYPE_DOUBLE,  //!< Characteristic Object is type of double
  TYPE_SIGNED,  //!< Characteristic Object is type of signed
  TYPE_UNSIGNED,//!< Characteristic Object is type of unsigned
  TYPE_STRING   //!< Characteristic Object is type of ASCII string
}TAsap3DataType;

//! possible database object types
typedef enum {
 DBTYPE_MEASUREMENT=1,  //!< Selects measurement objects from the database
 DBTYPE_CHARACTERISTIC, //!< Selects characteristic objects from the database
 DBTYPE_ALL             //!< Selects both, measurement and characteristic objects from the database
}TAsap3DBOType;

/** @} end of enumeration */




/** @defgroup definition Definitions
 *  @{
 */

//! Definitions used by function \link Asap3GetDatabaseObjectsByType \endlink

#define TDBE_VALUE_SCALAR 0x00000001   //!< definition for scalar object selection
#define TDBE_VALUE_CURVE  0x00000002   //!< definition for curve object selection
#define TDBE_VALUE_MAP    0x00000004   //!< definition for map object selection
#define TDBE_VALUE_AXIS   0x00000008   //!< definition for axis object selection
#define TDBE_VALUE_ASCII  0x00000010   //!< definition for ASCII object selection
#define TDBE_VALUE_VALBLK 0x00000020   //!< definition for Value Block object selection
#define TDBE_VALUE_ALL    (TDBE_VALUE_SCALAR|TDBE_VALUE_CURVE|TDBE_VALUE_MAP|TDBE_VALUE_AXIS|TDBE_VALUE_ASCII|TDBE_VALUE_VALBLK) //!< definition for all object types



//! Handle represents the connection to CANape started with \link Asap3Init() \endlink.
#define ASAP3_INVALID_HDL (TAsap3Hdl)0          //!< definition for a invalid communication handle between client and CANape
#define ASAP3_UNUSED_SECURITY (unsigned int)0   //!< default definition if no security is used
#define ASAP3_NO_SECURITY_JOB ""                //!< default definition if no security job


struct tAsap3Hdl;
typedef struct tAsap3Hdl *TAsap3Hdl;

typedef unsigned long *TRecorderID;


//! Handle represents one ASAP2 module initialized by call of AttachAsap2().
#define ASAP3_INVALID_MODULE_HDL (-1) //!< definition for a invalid module or device handle
/** @} end of definition */

typedef unsigned short TModulHdl;
typedef unsigned long  TScriptHdl;


//! Time stamp of measurement data. Resolution = 0.1 msec
typedef unsigned long TTime;


/** @defgroup structs Structures
 *  @{
 */


//! Setup of raster-specific FIFO size see  \link Asap3SetupFifo \endlink
typedef struct {
  TModulHdl module;         //!< Specifies the Module (see also \link Asap3CreateModule \endlink)
  unsigned short taskId;    //!< Specifies the TaskID of the Module (see also \link Asap3GetEcuTasks \endlink)
  unsigned short noSamples; //!< Specifies Buffer size for the TaskID
} tFifoSize;


//! Represents a complete sample. This structure is a member of the structure \link tSampleBlockObject \endlink
// SSR-BEGIN
typedef struct
{
 unsigned long countOfEntires;  //!< Specifies the size of the sample (count of measurement entries)
 ::TTime  timestamp;              //!< Timestamp of the sample (0.1 ms resolution)
 #if 1// SSR-REPLACE: #if 0
 double *data;                  //!< double array of the sample
 #else
 TReservedOffset_stream data;
 #endif
}
tSampleObject// SSR-APPEND:_stream
;
// SSR-END

//! Represents a structure that returns a block of samples the the client. (see also \link Asap3GetNextSampleBlock \endlink)
struct tSampleBlockObject
{
 BOOL has_buffer_Overrun;      //!< Signals a Buffer overrun
 long has_Error;               //!< Signals an error while measurement is running
 BOOL initialized;             //!< must be true
 long countofValidEntries;     //!< count of available and valid samples
 long countofInitilizedEntries;//!< count of available and valid and invalid (older)samples
 tSampleObject **tSample;      //!< Array of samples (see structure  \link tSampleObject \endlink)
};

/** @} end of structs */

/** @defgroup Driver Driver
 *  @{
 */

//! Value of parameter 'driverType' of subroutine Asap3CreateModule()
typedef enum {
  ASAP3_DRIVER_UNKNOWN     = 0,        //!< Default value for Error case (must not be used)
  ASAP3_DRIVER_CCP         = 1,        //!< CCP: CAN calibration protocol
  ASAP3_DRIVER_XCP         = 2,        //!< XCP
  ASAP3_DRIVER_CAN         = 20,       //!< CAN
  ASAP3_DRIVER_HEXEDIT     = 40,       //!< Pure offline driver
  ASAP3_DRIVER_ANALOG      = 50,       //!< Analog measurement data (e.g. 'National Instruments' PCMCIA-card)
  ASAP3_DRIVER_CANOPEN     = 60,       //!< CANopen
  ASAP3_DRIVER_CANDELA     = 70,       //!< CANdela Diagnostic
  ASAP3_DRIVER_ENVIRONMENT = 80,       //!< Environment - access to global variables
  ASAP3_DRIVER_LIN         = 90,       //!< LIN Driver
  ASAP3_DRIVER_FLX         = 100,      //!< FlexRay
  ASAP3_DRIVER_FUNC        = 110,      //!< Functional Diagnostic Driver
  ASAP3_DRIVER_NIDAQMX     = 120,      //!< NI DAQ Driver 'National Instruments'
  ASAP3_DRIVER_XCP_RAMSCOPE= 130,      //!< XCP Driver for Ramscope
  ASAP3_DRIVER_SYSTEM      = 140,      //!< System driver
  ASAP3_DRIVER_ETH         = 150,      //!< Ethernet driver
  ASAP3_DAIO_SYSTEM        = 160,      //!< DAIO_SYSTEM driver
  ASAP3_DRIVER_SOME_IP     = 170,      //!< SOME-IP driver
  ASAP3_DRIVER_DLT         = 180       //!< DLT driver
} tDriverType;
/** @} end of ´Drivers */

//! Version control of CANapAPI.DLL
#ifndef VERSION_T

/** @defgroup enumeration Enumerations
 *  @{
 */
typedef enum
{
 eT_MEASUREMENT_STOPPED             = 0, //!< No measurement running
 eT_MEASUREMENT_INIT                = 1, //!< measurement started, measurement thread still not running
 eT_MEASUREMENT_STOP_ON_START       = 2, //!< measurement will be stopped by a prStart function
 eT_MEASUREMENT_EXIT                = 3, //!< measurement will stop, but is still running
 eT_MEASUREMENT_THREAD_RUNNING      = 4, //!< measurement started, measurement thread running
 eT_MEASUREMENT_RUNNING             = 5  //!< measurement running
}tMeasurementState;
/** @} end of enumeration */


//! DLL_INTERFACE_VERSION MAIN_VERSION  SUB_VESION  RELEASE  OS_VERSION  OS_RELEASE as string
#define DLL_INTERFACE_VERSION  "02.03.01.Windows95/WindowsNT.1  "

//! DLL_INTERFACE_VERSION MAIN_VERSION  SUB_VESION  RELEASE  OS_VERSION  OS_RELEASE
//! See QM                  HV            NV        ES        BV         BS
#define CANAPE_API_MAIN_VESION   2
#define CANAPE_API_SUB_VESION    3
#define CANAPE_API_RELEASE       1
#define CANAPE_API_OS_VERSION    "Windows95/WindowsNT"
#define CANAPE_API_OS_RELEASE    1

#ifndef CUSTOMER_ID
#define CUSTOMER_ID           "Unknown"
#endif

#define VERSION_T
#define MAX_OS_VERSION 50



/** @defgroup structs Structures
 *  @{
 */
//! structure version_t used in function \link Asap3GetVersion \endlink
typedef struct {
  int dllMainVersion; //!< Main version of CANapeAPI DLL
  int dllSubVersion;  //!< Subversion version of CANapeAPI DLL
  int dllRelease;     //!< Release version of CANapeAPI DLL
  char osVersion[MAX_OS_VERSION];//!< Name of the minimum OS System
  int osRelease;      //!< minimum OS System version
} version_t;

#endif

//! structure version_t used in function \link Asap3GetApplicationVersion \endlink

typedef struct {
  int MainVersion;  //!< Main version of the current application
  int SubVersion;   //!< Subversion version of the current application
  int ServicePack;  //!< Installed service pack
  char Application[30]; //!<Application name (CANape)
} Appversion;

/** @} end of structs */

/** @defgroup Channels Channels
 *  @ingroup  Driver

 *  @{
 */

//!\n
//!Definitions for CAN\n
//!\n
#define   DEV_CAN1        1
#define   DEV_CAN2        2
#define   DEV_CAN3        3
#define   DEV_CAN4        4
#define   DEV_CAN5        5
#define   DEV_CAN6        6
#define   DEV_CAN7        7
#define   DEV_CAN8        8
#define   DEV_CAN20      20

//!\n
//!Definitions for FlexRay 1-8\n
//!\n
#define   DEV_FLX1       31
#define   DEV_FLX2       32
#define   DEV_FLX3       33
#define   DEV_FLX4       34
#define   DEV_FLX5       35
#define   DEV_FLX6       36
#define   DEV_FLX7       37
#define   DEV_FLX8       38

//!\n
//!Definitions for LIN 1-8\n
//!\n
#define   DEV_LIN1       61
#define   DEV_LIN2       62
#define   DEV_LIN3       63
#define   DEV_LIN4       64
#define   DEV_LIN5       65
#define   DEV_LIN6       66
#define   DEV_LIN7       67
#define   DEV_LIN8       68


//!\n
//!Definitions for CAN on VX 1-4\n
//!\n
#define   DEV_VX_CAN1    81
#define   DEV_VX_CAN2    82
#define   DEV_VX_CAN3    83
#define   DEV_VX_CAN4    84

//!\n
//!Definitions for TCP on VX\n
//!\n
#define   DEV_VX_TCP     85
#define   DEV_VX_UDP     86

//!\n
//!Definitions for SXI\n
//!\n
#define   DEV_SXI1       91
#define   DEV_SXI2       92
#define   DEV_SXI3       93
#define   DEV_SXI4       94
#define   DEV_SXI5       95
#define   DEV_SXI6       96
#define   DEV_SXI7       97
#define   DEV_SXI8       98

//!\n
//!Definitions for USB\n
//!\n
#define   DEV_USB        110

//!\n
//!Definitions for CAN CANFD\n
//!\n
#define   DEV_CANFD1        121
#define   DEV_CANFD2        122
#define   DEV_CANFD3        123
#define   DEV_CANFD4        124
#define   DEV_CANFD5        125
#define   DEV_CANFD6        126
#define   DEV_CANFD7        127
#define   DEV_CANFD8        128
#define   DEV_CANFD9        129



//!\n
//!Definitions for TCP\n
//!\n
#define   DEV_TCP         255
//!\n
//!Definitions for UDP\n
//!\n
#define   DEV_UDP         256
//!\n
//!Definitions for user defined Interface\n
//!\n
#define   DEV_USERDEFINED 261

//!\n
//!Definitions for user Ethernet Interface\n
//!\n
#define   DEV_VX_ETHERNET1 271
#define   DEV_VX_ETHERNET2 272

//!\n
//!Definitions for user DAIO Interface\n
//!\n
#define   DEV_DAIO_DLL     280

/** @} end of Channels */



#define ASAP3_EXPORT __declspec(dllexport)
#define CALL_CONV WINAPI

#ifndef MATLABAPI
extern "C" {


#ifndef _CANAPE_API_TCP_
// Hidden for API Dokumentation
bool ASAP3_EXPORT CALL_CONV Asap3IsUsCANapeVersion(BOOL *USVersion);
#endif




// -----------------------------------------------------------------------------------------------------------------
// CANapeAPI Functions
// ~~~~~~~~~~~~~~~~~~~

/** @defgroup ApiFunctions  Api Functions
 *  The CANapeApi will be controlled by these functions
 */

/** @defgroup Initialization Init & Control Functions
 *  @ingroup ApiFunctions
 *  initializes CANape for ASAP3 connection
 *  @{
 */

//! Version control
// ~~~~~~~~~~~~~~~
/*! Should be executed, the received data should be compared.
 *  The current DLL is suitable,<br>
 *  if (version.dllMainVersion == CANAPE_API_MAIN_VESION) and<br>
 *      (version.dllSubVersion  == CANAPE_API_SUB_VESION) and<br>
 *      (version.dllRelease     >=  CANAPE_API_RELEASE)
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetVersion(version_t * version);

//! Configure ASAP3 TCP connection
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/*! This function must be called before any of the Asap3Init calls.
 *  It will prepare the ASAP3 module for the connection to the ASAP3 CANAPE server.\n This function is only available in the Ethernet version of CANapeAPI , the CANapeTCP.dll
 *
 * \param ipAddress \input Specify the string with ipAddress in form (123.2.3.14) of the PC where CANape is running in ASAP3 TCP mode
 * \param portNumber \input Specify port number of the CANpe ASAP3 TCP Server.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetTCPOptions(const char* ipAddress, unsigned long portNumber);

//! Initialize ASAP3 connection
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~

/*! Returns a handle to be used in
 * subsequent function calls. CANape will be started (if not actually
 * running).<br>
 *
 *  \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape  working directory
 *        By default the project file CANape.INI is saved at the working directory
 *        used for the CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape in 'minimized' mode.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3Init(TAsap3Hdl * hdl,
                                             unsigned long responseTimeout,
                                             const char *workingDir,
                                             unsigned long fifoSize,
                                             bool debugMode);

//! In addition to Asap3Init() the maximum number of measurement values per FIFO entry can be set (option 'sampleSize').
/*!  \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape  working directory
 *        by default the project file CANape.INI saved at the working directory
 *        is used for the CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *  \param sampleSize \input The maximum number of measurement values per FIFO entry is 256.
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape starts in 'minimized' mode.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3Init2(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode);

//! In addition to Asap3Init2() the device list of CANape ist only cleared if the value of clearDeviceList is 'true'.
/*! \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape working directory
 *        By default the project file CANape.INI saved at the working directory
 *        is used for the CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *  \param sampleSize \input The maximum number of measurement values per FIFO entry is 256.
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape starts in 'minimized' mode.
 *
 * \param clearDeviceList \input If it is true the CANape device list will be cleared.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3Init3(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList);

//! In addition to Asap3Init3() CANape is started in Hexmode if value of bool bHexmode is 'true'.
/*! Hex is a special CANape mode to view your databases or/and hex files without an device.
 *  In this mode data acquisition is impossible.
/*! \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape working directory
 *        By default the project file CANape.INI, saved at the working directory,
 *        is used for the current CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *  \param sampleSize \input The maximum number of measurement values per FIFO entry is 256.
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape starts in 'minimized' mode.
 *
 *  \param clearDeviceList \input If it is true the CANape device list will be cleared.
 *  \param bHexmode \input If it is true the CANape will be started in HexMode
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3Init4(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList,
                                              bool bHexmode);


//! In addition to Asap3Init4() CANape is started in nonmodal mode, if value of bool bModalMode is 'false'.
/*! \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape  working directory
 *        By default the project file CANape.INI saved at the working directory
 *        is used for the CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *  \param sampleSize \input The maximum number of measurement values per FIFO entry is 256.
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape starts in 'minimized' mode.
 *
 *  \param clearDeviceList \input If it is true the CANape device list will be cleared.
 *  \param bHexmode \input If it is true the CANape will be started in HexMode
 *  \param bModalMode \input If it is true the CANape will be started in the NON MODAL mode.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3Init5(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList,
                                              bool bHexmode,
                                              bool bModalMode);


//! In addition to Asap3Init5() CANape is started in nonmodal mode, if value of bool bModalMode is 'false'.
/*! \param hdl \output Asap3Handle for further access to this interface.
 *  \param responseTimeout \input Maximum response time
 *  \param workingDir \input Sets CANape  working directory
 *        By default the project file CANape.INI saved at the working directory
 *        is used for the CANape session. If you want to load a different
 *        project file, please append the project file name to 'workingDir'.
 *  \param fifoSize \input Total size of FIFO used for data acquisition, i.e. number of FIFO
 *        entries which can be read out using Asap3GetNextSample(). Each FIFO entry
 *        includes at most ACQ_MAX_VALUES=128 measurement values.
 *  \param sampleSize \input The maximum number of measurement values per FIFO entry is 256.
 *  \param debugMode \input if this is true call CANape in 'normal' screen size instead of 'minimized'.<br>
 *          if it is false call CANape starts in 'minimized' mode.
 *
 *  \param clearDeviceList \input If it is true the CANape device list will be cleared.
 *  \param bHexmode \input If it is true the CANape will be started in HexMode
 *  \param bModalMode \input If it is true the CANape will be started in NON MODAL mode.
 *  \param eAppType \input this parameter describes the Application (eCANAPE) which the client wants to start
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3Init6(TAsap3Hdl *hdl,
                                       unsigned long responseTimeout,
                                       const char *projectFile,
                                       unsigned long fifoSize,
                                       unsigned long sampleSize,
                                       bool debugMode,
                                       bool clearDeviceList,
                                       bool bHexmode,
                                       bool bModalMode,
                                       TApplicationID  *strApplication);


//! Returns the current project Directory
/*! \param hdl \input Asap3 Handle
*   \param directory \output current directory is returned.
*   \param size \output returns the size of the character buffer. The size parameter is also used to inform the function \n
*     concerning the client defined buffer size. If the parameter directory is NULL, size returns the necessary size of the character buffer
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetProjectDirectory(TAsap3Hdl hdl, char* directory, unsigned long *size);


//! Shut down ASAP3 connection to CANape (terminates CANape)
/*! \param hdl \input Asap3 Handle
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3Exit(TAsap3Hdl hdl);

//! Call this function to get error information (error code) about the previously executed function call.
/*!  \param hdl \input Asap3 Handle
 *   \see Error codes
 *   \return error number.
 */
extern unsigned short ASAP3_EXPORT CALL_CONV Asap3GetLastError(TAsap3Hdl hdl);


//! Call this function to change the application name which is used to select the logical CAN channel name. E.g. namexxCAN2
/*!  \param hdl \input Asap3 Handle
/*!  \param AppName \input new application name
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3SetApplicationName(TAsap3Hdl hdl, const char *AppName);

//! Call this function to get the current application name which is used to select the logical CAN channel name. E.g. namexxCAN2
/*!  \param hdl \input Asap3 Handle
/*!  \param Name \output application name
/*!  \param Size \output size of the name buffer
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetApplicationName(TAsap3Hdl hdl,char *Name,unsigned long *Size);



//! Call this function to get the current version of the server application (CANape).
/*!  \param hdl \input Asap3 Handle
 *  \param version \output version info
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3GetApplicationVersion(TAsap3Hdl hdl,Appversion * version);


//! Shut down ASAP3 connection to CANape with optional termination of CANape. true
/*! \param hdl \input Asap3 Handle
 *  \param close_CANape \input true -> CANape will be shutdown otherwise CANape will not be shutdown
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3Exit2(TAsap3Hdl hdl,bool close_CANape);



//! Call this function to get an error text corresponding to the result of Asap3GetLastError().
/*! \param hdl \input Asap3 Handle
 *  \param errCode  \input Number of error
 *  \param errMsg  \output After call, it contains the error message.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ErrorText(TAsap3Hdl hdl, unsigned short errCode, char ** errMsg);

//! Trouble shooting: call this function to pop up the debug window of the MCD-system.
/*! \param hdl \input Asap3 Handle
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3PopupDebugWindow(TAsap3Hdl hdl);

//! Trouble shooting: call this function to pop up the debug window of the MCD-system.
/*! \param hdl \input Asap3 Handle
 * \param fileName \input Content of the debug window is saved to this file.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3SaveDebugWindow(TAsap3Hdl hdl, const char *fileName);

//! Create a new module/device and attach an ASAP2-description file
/*! Returns a handle to be used for subsequent function calls
 *  \param hdl \input Asap3 Handle
 *  \param asap2Fname \input Name of the asap2 file to load.
 *  \param canChnl \input   CAN channel to select.
 *  \param module \output  After call, it contains handle to new created module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3AttachAsap2(TAsap3Hdl hdl,const char *asap2Fname, short canChnl, TModulHdl * module);

//! Create a new module/device and attach an description file (A2L,DB,DBC)
/*!  Returns a handle to be used for subsequent function calls
 * \see tDriverType
 * \param hdl \input Asap3 Handle
 * \param moduleName \input Name of module to create.
 * \param databaseFilename \input Name of description file to load
 * \param driverType \input Set driver type. Possible values see tDriverType
 * \param channelNo \input Logical communication channel to be used (like CCP:1-4 = CAN1-CAN4, 255 = TCP/IP, 256 = UDP))
 * \param module  \output After call, it contains handle to new created module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule(TAsap3Hdl hdl, const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, TModulHdl * module);

//! Create a new module/device and attach an description file (A2L,DB,DBC) and set it On/Off line
/*! Returns a handle to be used for subsequent function calls. If goOnline == false, 'some' API calls can be done
    even if the relevant ECU is not connected.
 * \see tDriverType
 * \param hdl \input Asap3 Handle
 * \param moduleName \input Name of module to create.
 * \param databaseFilename \input Name of description file to load
 * \param driverType \input Set driver type. Possible values see tDriverType
 * \param channelNo \input Logical communication channel to be used (like CCP:1-4 = CAN1-CAN4, 255 = TCP/IP, 256 = UDP)
 * \param goOnline \input indicates, that the new device need to switched ONLINE (allows to create OFFLINE devices).
 * \param module  \output After call, it contains handle to new created module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule2(TAsap3Hdl hdl, const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, bool goOnline, TModulHdl * module);

//! Create a new module/device and attach an description file (A2L,DB,DBC)
/*! Returns a handle to be used for subsequent function calls. If goOnline == false, 'some' API calls can be done
    even if the relevant ECU is not connected.
 * \see tDriverType
 * \param hdl \input Asap3 Handle
 * \param moduleName \input Name of module to create.
 * \param databaseFilename \input Name of description file to load
 * \param driverType \input Set driver type. Possible values see tDriverType
 * \param channelNo \input Logical communication channel to be used (like CCP:1-4 = CAN1-CAN4, 255 = TCP/IP, 256 = UDP)
 * \param goOnline \input indicates, that the new device need to switched ONLINE (allows to create OFFLINE devices).
 * \param enablecache \input enabled the cache (1) oder disables it (0) if this parameter should be ignored it has to be set to (-1)
 * \param module  \output After call, it contains handle to new created module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule3(TAsap3Hdl hdl,const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, bool goOnline, short enablecache, TModulHdl * module);

//! Create a new module/device and attach an description file (A2L,DB,DBC)
/*! Returns a handle to be used for subsequent function calls. If goOnline == false, 'some' API calls can be done
even if the relevant ECU is not connected.
* \see tDriverType
* \param hdl \input Asap3 Handle
* \param moduleName \input Name of module to create.
* \param databaseFilename \input Name of description file to load
* \param driverType \input Set driver type. Possible values see tDriverType
* \param channelNo \input Logical communication channel to be used (like CCP:1-4 = CAN1-CAN4, 255 = TCP/IP, 256 = UDP)
* \param interfaceName \input name of the interface to be used
* \param goOnline \input indicates, that the new device need to switched ONLINE (allows to create OFFLINE devices).
* \param enablecache \input enabled the cache (1) oder disables it (0) if this parameter should be ignored it has to be set to (-1)
* \param module  \output After call, it contains handle to new created module.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule4(TAsap3Hdl hdl, const char* moduleName, const char* databaseFname,
  short driverType, short channelNo, const char* interfaceName, bool goOnline, short enableCache, TModulHdl* module);

//! Create a new module/device and attach an description file (A2L,DB,DBC)
/*! Returns a handle to be used for subsequent function calls. If goOnline == false, 'some' API calls can be done
even if the relevant ECU is not connected.
* \see tDriverType
* \param hdl \input Asap3 Handle
* \param moduleName \input Name of module to create.
* \param databaseFilename \input Name of description file to load
* \param driverType \input Set driver type. Possible values see tDriverType
* \param channelNo \input Logical communication channel to be used (like CCP:1-4 = CAN1-CAN4, 255 = TCP/IP, 256 = UDP)
* \param interfaceName \input name of the interface to be used
* \param secProfileId \input security profile id (if != 0, activation of security on network will be done)
* \param securityRole \input given security role will be assigned to the module
* \param goOnline \input indicates, that the new device need to switched ONLINE (allows to create OFFLINE devices).
* \param enablecache \input enabled the cache (1) oder disables it (0) if this parameter should be ignored it has to be set to (-1)
* \param module  \output After call, it contains handle to new created module.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModuleSec(TAsap3Hdl hdl, const char* moduleName, const char* databaseFname,
  short driverType, short channelNo, const char* interfaceName, unsigned int secProfileId, const char* securityRole,
  bool goOnline, short enableCache, TModulHdl* module);

//! returns the name of the security job (role) of a module
/*! \param hdl \input Asap3 Handle
*   \param module \input module name
*   \param jobName \output Pointer to retrieve the security job name (role) string
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleSecJobName(TAsap3Hdl hdl, TModulHdl module, char* jobName, DWORD* sizeofBuffer);

//! Returns the count of instantiated Modules in the current Project
/*! \param hdl \input Asap3 Handle
 *  \param count \output  returns the count of modules
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleCount(TAsap3Hdl hdl,unsigned long *count);

//! Enables or disables the option "Restart measurement on Error"
/*! \param hdl \input Asap3 Handle
*  \param module \input  The handle of the module
*  \param restart \input  enables (true) the restart option or disables (false) it
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3RestartMeasurementOnError(TAsap3Hdl hdl,TModulHdl module,bool restart);

//! Retrieves information concerning the "Restart measurement on Error" option
/*! \param hdl \input Asap3 Handle
*  \param module \input  The handle of the module
*  \param restart \output  option is enables (true) or disables (false)
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRestartMeasurementOnErrorEnabled(TAsap3Hdl hdl,TModulHdl module,bool *restart);


//! Returns the activation state of specific module
/*! \param hdl \input Asap3 Handle
*  \param module \output Points to demanded module
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsModuleActive(TAsap3Hdl hdl,TModulHdl module,bool *activate);

//! Switches the module  activation state  activated (true) to deactivated (false) and vice versa
/*! \param hdl \input Asap3 Handle
*  \param module \input Points to demanded module
*  \param activate \output  Activation state

 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ModuleActivation(TAsap3Hdl hdl,TModulHdl module,bool activate);


//! Switches the modules cal page between RAM and ROM
/*! \param hdl \input Asap3 Handle
*  \param module \input Points to demanded module
*  \param activate \output  RamMode  e_TR_MODE_RAM=      0,e_TR_MODE_ROM=      1:
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3SwitchToMemoryPage(TAsap3Hdl hdl,TModulHdl module,e_RamMode mode);

//! Returns the active cal page
/*! \param hdl \input Asap3 Handle
*  \param module \input Points to demanded module
*  \param activate \output  RamMode  e_TR_MODE_RAM=      0,e_TR_MODE_ROM=      1:
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3GetMemoryPage(TAsap3Hdl hdl,TModulHdl module,e_RamMode *mode);


//! Get the Unit of a DB Object
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param DatabaseObjectName \input  name of the requested DBObject
 *  \param UnitName     \output   character array to retrieve the unit name
 *  \param Size      \input   size of the character array
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetDBObjectUnit(TAsap3Hdl hdl,TModulHdl module,char *DatabaseObjectName,char *UnitName,UINT *Size);
//! Get information of a database object
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param DatabaseObjectName \input  name of the requested DBObject
 *  \param Info     \output   DBObjectInfo Information structure
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetDBObjectInfo(TAsap3Hdl hdl,TModulHdl module,char *ObjectName,DBObjectInfo *Info);
//! Get objects of the attached ASAP2 file
/*! \param hdl \input Asap3 Handle
 *  \param module \output Points to demanded module
 *  \param DataObjects \output  Array of data objects to fill
 *  \param MaxSize     \input   Size of data objects array
 *  \param DbType      \input   type of the DB Object
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseObjects(TAsap3Hdl hdl,TModulHdl module,char *DataObjects,UINT *MaxSize,TAsap3DBOType DbType);

//! Get objects of the attached ASAP2 file
/*! \param hdl \input Asap3 Handle
 *  \param module \output Points to demanded module
 *  \param DataObjects \output  Array of data objects to fill
 *  \param MaxSize     \input   Size of data objects array
 *  \param DbType      \input   type of the DB Object
 *  \param TypeFilter  \input   type filter (map, curve ...)
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseObjectsByType(TAsap3Hdl hdl,TModulHdl module,char *DataObjects,UINT *MaxSize,TAsap3DBOType DbType,unsigned long TypeFilter);

//! Get name of attached ASAP2 file
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param asap2Fname \output Contains data description file name after call
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetAsap2(TAsap3Hdl hdl, TModulHdl module, char ** asap2Fname);

//! Get Info concerning the database file
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param Info \output DBFileInfo structure containing name, path an type of the database file
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseInfo(TAsap3Hdl hdl, TModulHdl module, DBFileInfo *Info) ;

//! Transmit file to remote PC
/*! \param hdl \input Asap3 Handle
 *  \param srcFname \input File name of the 'source file' saved at server PC
 *  \param dstFname \input File name of the 'destination file' on client PC, where the file shall be transfered to
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3TransmitFile2ClientPc(TAsap3Hdl hdl, char *srcFname, char *dstFname);

//! Get name of module
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param moduleName \output pointer to the modules name
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleName(TAsap3Hdl hdl, TModulHdl module, char **moduleName);

//! Get handle of an existing module (created by another application)
/*! \param hdl \input Asap3 Handle
 *  \param moduleName \input Name of module to get handle
 *  \param module \output Returned module handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleHandle(TAsap3Hdl hdl, const char *moduleName, TModulHdl * module);

//! Opposite of AttachAsap2()
/*! \param hdl \input Asap3 Handle
 *  \param module \input Handle of module to release
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseModule(TAsap3Hdl hdl, TModulHdl module);

//! Get current communication type (e.g. "CAN")
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param commType \output Contains communication type after call
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCommunicationType(TAsap3Hdl hdl, TModulHdl module, char ** commType);

//! Switches an ECU from online to offline and vice versa
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param State  \input state flag ( online - offline )
 *  \param download \input if this parameter is set to true CANape will execute an download in case of
 *                         TAsap3ECUState = TYPE_SWITCH_ONLINE
 */
bool ASAP3_EXPORT CALL_CONV Asap3ECUOnOffline(TAsap3Hdl hdl, TModulHdl module,TAsap3ECUState State,bool download);

//! Asks CANape whether a ECU is online or offline
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param State \output pointer on a state flag ( online - offline )
 */
bool ASAP3_EXPORT CALL_CONV Asap3IsECUOnline(TAsap3Hdl hdl, TModulHdl module,TAsap3ECUState *State);

/** @} end of initialization */


/** @defgroup Calibration Calibration Functions
 *  @ingroup ApiFunctions
 *  handles access to calibration ram by address or by calibration object
 */

/** @defgroup accessbyaddress Special Access by address functions
 *  @ingroup Calibration
 *  \attention Handle with care, normal data access is by object.
 *  @{
 */
// -----------------------------------------------------------------------------------------------------------------
// Calibration
// ~~~~~~~~~~~


//! Read ECU data from calibration RAM by address
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param addr  \input Address to read.
 *  \param addrExt \input Used by special multiprocessor ECU. If it's not required set it to 0.
 *  \param size  \input Size of data to read.
 *  \param data  \output Points to destination data block.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadByAddress(TAsap3Hdl hdl, TModulHdl module,
                   unsigned long addr, unsigned char addrExt,
                   unsigned long size, unsigned char * data);

//! Write ECU data to calibration RAM by address
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param addr \input Address to write
 *  \param addrExt \input Used by special multiprocessor ECU. If it's not required set it to 0.
 *  \param size \input Size of data to write.
 *  \param data \input Points to source data block.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteByAddress(TAsap3Hdl hdl, TModulHdl module,
                   unsigned long addr, unsigned char addrExt,
                   unsigned long size, unsigned char * data);

/** @} end of accessbyaddress */

/** @defgroup accessbyobject Standard Access Functions
 *  @ingroup Calibration
 *  handles access to calibration ram by address or by calibration object
 *  @{
 */

//! Read calibration object using record layout information from ASAP2
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param calibrationObjectName \input Name of the calibration object to read
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param value \output Value of the calibration object.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObject(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, TFormat format,
                   TCalibrationObjectValue * value);


//! Read calibration object using record layout information from ASAP2
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param calibrationObjectName \input Name of the calibration object to read
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param forceupload \input forces an upload of the calibration object
 *  \param value \output Value of the calibration object.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObject2(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                 TFormat format, bool forceupload,TCalibrationObjectValue *value);

//! Read calibration object using record layout information from ASAP2
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param calibrationObjectName \input Name of the calibration object to read
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param value \output Value of the calibration object.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObjectEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, TFormat format,
                   TCalibrationObjectValueEx * value);

//! Write calibration object using record layout information from ASAP2
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param calibrationObjectName \input Name of the calibration object to write
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param value \input Value of the calibration object.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteCalibrationObject(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, TFormat format,
                   TCalibrationObjectValue * value);

//! Write calibration object using record layout information from ASAP2
/*! \param hdl \input Asap3 Handle
 *  \param module \input points to demanded module
 *  \param calibrationObjectName \input Name of the calibration object to write
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param value \input Value of the calibration object.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteCalibrationObjectEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, TFormat format,
                   TCalibrationObjectValueEx * value);


//! Test, whether the name is a valid object of ASAP2 file
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module
 *  \param objectName \input Name of the calibration object to test
 *  \param type \output Selector to declare an object to be used for measurement or calibration.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3TestObject(TAsap3Hdl hdl, TModulHdl module,
                   const char * objectName, TObjectType * type);


//! Read calibration object using record layout information from ASAP2.
/*! Returns the dimensions of the given calibration object.
 *  \param hdl \input Asap3 Handle
 *  \param module \input  Points to demanded module
 *  \param calibrationObjectName \input  Name of the calibration object
 *  \param xDimension \output  X-axis of the calibration object
 *  \param yDimension \output  Y-axis of the calibration object
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectInfo(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                   short * xDimension, short * yDimension);

//! Read calibration object using record layout and type information from ASAP2.
/*! Returns the dimensions of the given calibration object.
 *  \param hdl \input Asap3 Handle
 *  \param module \input  Points to demanded module
 *  \param calibrationObjectName \input  Name of the calibration object
 *  \param xDimension \output  X-axis of the calibration object
 *  \param yDimension \output  Y-axis of the calibration object

 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectInfoEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                   short *xDimension, short *yDimension,TValueType *type);


//! Asap3CalibrationObjectRecordInfo
// ~~~~~~~~~~~~~~~~
/*! Returns information about the layout of a calibration Object
 *  \param hdl \input Asap3 Handle.
 *  \param module \input Module Handle
 *  \param calibrationObjectName \input Name of the calibration Object which should be queried.
 *  \param coeffs \output Axis information see #TLayoutCoeffs
 *  \param xDimension \output X-Dimension of the calibration Object
 *  \param yDimension \output Y-Dimension of the calibration Object
 *
 */


extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectRecordInfo(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, TLayoutCoeffs * coeffs,
                   short * xDimension, short * yDimension);

/** @} end of accessbyobject */

/** @defgroup DataAcquisition Data Acquisition Functions
 *  @ingroup ApiFunctions
 *  @{
 */

// -----------------------------------------------------------------------------------------------------------------
// Data Acquisition
// ~~~~~~~~~~~~~~~~

//! Get available data acquisition tasks.
/*! Returns an array of the following structure:
 *
 * typedef struct {
 *    char *description;
 *    unsigned short taskId;
 *    unsigned long taskCycle;
 *  } TTaskInfo;
 *
 * TaskInfo[i].description can be used to perform user selection<br>
 * TaskInfo[i].taskId is intended to be used in subsequent calls of
 * Asap3InitDataAcquisition() and Asap3GetNextSample().
 * \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 * \param taskInfo \output Available ECU tasks.
 * \param noTasks  \output Number of ECU task.
 * \param maxTaskInfo  \input Size of the given taskInfo.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuTasks(TAsap3Hdl hdl, TModulHdl module,
                   TTaskInfo * taskInfo, unsigned short * noTasks,
                   unsigned short maxTaskInfo);




//! Get available data acquisition tasks.
/*! Returns an array of the following structure:
 *
 * typedef struct {
 *    char *description;
 *    unsigned short taskId;
 *    unsigned long taskCycle;
 *    unsigned long eventChannel;
 *  } TTaskInfo2;
 *
 * TaskInfo[i].description can be used to perform user selection<br>
 * TaskInfo[i].taskId is intended to be used in subsequent calls of
 * Asap3InitDataAcquisition() and Asap3GetNextSample().
 * \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 * \param taskInfo2 \output Available ECU tasks.
 * \param noTasks  \output Number of ECU task.
 * \param maxTaskInfo  \input Size of the given taskInfo.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuTasks2(TAsap3Hdl hdl, TModulHdl module,
                   TTaskInfo2 * taskInfo2, unsigned short *noTasks,
                   unsigned short maxTaskInfo);


//! Creates a Logger configuration file (DBC)
/*! Creates a DBC file which describes the CCP or XCP can frames
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateLoggerConfiguration(TAsap3Hdl hdl,TModulHdl module);


//! Retrieves the drivertype of an ECU
/*! DriverType returns the value of the drivertype
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 * \param DriverType \output  Pointer to the DriverType Value.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuDriverType(TAsap3Hdl hdl, TModulHdl module,tDriverType *DriverType);

//! Information about the Resume mode
/*! Function returns true if the device supports resume mode
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 * \param possible \output  true if resume mode is supported.
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3HasResumeMode(TAsap3Hdl hdl,TModulHdl module,bool *possible);


//! Enables the Resume mode of the ECU
/*! if the function is successful it return s true
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetResumeMode(TAsap3Hdl hdl,TModulHdl module);


//! Determines if an ECU is in resume mode
/*! if the function is successful it return s true
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 * \param enabled \output  true if resume mode is enabled.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsResumeModeActive(TAsap3Hdl hdl,TModulHdl module,bool *enabled);

//! Disables if an ECU is in resume mode
/*! if the function is successful it return s true
 *  \param hdl \input Asap3 Handle
 * \param module \input  Points to demanded module.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ClearResumeMode(TAsap3Hdl hdl,TModulHdl module);


//! >Get measurement data info
/*  Retrieves the default raster and downsampling time of a requested measurement object
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param measurementObjectName \input Name of object to measure.
 *  \param taskId \output number of the default task id
 *  \param downSampling \output Value of the default downsampling time
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetChnlDefaultRaster(TAsap3Hdl hdl,  TModulHdl module,const char *measurementObjectName,unsigned short *taskId,unsigned short *downSampling);

//! Setup of ECU Task specific FIFO size (Default = fifoSize/23 per Task)
/*  Reconfigures the division of the Fifo Memory. Set the number of Fifo's and their size.
 *  \param hdl \input Asap3 Handle
 *  \param nFifoSize \input Size of the Array fifosize[].
 *  \param tFifoSize \input Struct with taskId, handle of module and SampleSize.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupFifo(TAsap3Hdl hdl,
                   unsigned short nFifoSize,
                   tFifoSize fifoSize[]);

//! Initialize data acquisition
/*! Add a measurement object to the data acquisition channel list
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param measurementObjectName \input Name of object to measure.
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param taskId \input Id of the task to query. Intends  the sampling rate at ECU and the rate that channel data samples are put into the FIFO buffer.
 *  \param pollingRate \input If acquisition mode is polling this specify the polling rate. Reduce the original sample rate of ECU data. Example: If the sample rate of the ECU is 1 per 10msec, but the CANapeAPI client is set to receive data only every 50msec, the option 'downsampling' must be set to 5.
 *  \param save2File \input Save this channel to measurement file. Therefore the currently selected Recorder will be used
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupDataAcquisitionChnl(TAsap3Hdl hdl,  TModulHdl module,
                   const char *measurementObjectName,
                   TFormat format, unsigned short taskId,
                   unsigned short pollingRate, bool save2File);

//! Initialize data acquisition
/*! Add a measurement object to the data acquisition channel list
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param measurementObjectName \input Name of object to measure.
 *  \param format \input Format of ECU measurement or calibration data.
 *  \param taskId \input Id of the task to query. Intends  the sampling rate at ECU and the rate that channel data samples are put into the FIFO buffer.
 *  \param pollingRate \input If accquisition mode is polling this specify the polling rate. Reduce the original sample rate of ECU data. Example: If the sample rate of the ECU is 1 per 10msec, but the CANapeAPI client is set to receive data only every 50msec, the option 'downsampling' must be set to 5.
 *  \param save2File \input Save this channel to measurement file. Therefore the currently selected Recorder will be used
 *  \param transfer_To_Client \input transfers the defined measurement object to the client
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupDataAcquisitionChnl2(TAsap3Hdl hdl,  TModulHdl module,
                   const char *measurementObjectName,
                   TFormat format, unsigned short taskId,
                   unsigned short pollingRate, bool save2File,bool transfer_To_Client);

//! returns the Entries, defined in the CANape Measurement list
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 * \param module \input Adress of a MeasurementListEntries pointer. This struct must not be deleted by the client
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMeasurementListEntries(TAsap3Hdl hdl,TModulHdl module,MeasurementListEntries **Items);

//! returns the current state of the measurement
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 * \param State  \output pointer to receive the measurement state
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMeasurementState(TAsap3Hdl hdl,tMeasurementState *State);



//! returns true if the MCD option is enabled
/*! \param hdl \input Asap3 Handle
 * \param State  \output pointer to receive the option state
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3HasMCD3License(TAsap3Hdl hdl,bool *available);



//! Creates a new Recorder
/*! \param hdl \input Asap3 Handle
 *  \param RecorderName \input the name of the new Recorder
 *  \param trecorder \output pointer to a recorder ID
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3DefineRecorder(TAsap3Hdl hdl,char *RecorderName,TRecorderID * trecorder,TRecorderType RecorderType=eTRecorderTypeMDF);


//! returns the type of a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param RecorderType \output RecorderType
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderType(TAsap3Hdl hdl, TRecorderID recorderID, TRecorderType *RecorderType);

//! returns the name of a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param recorderName \output character buffer to retrieve the Recorder name
 *  \param trecorder \output size of the recorderName buffer
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderName(TAsap3Hdl hdl,TRecorderID recorderID,char * recorderName, long *Size);

//! returns Count of defined Recorders
/*! \param hdl \input Asap3 Handle
 *  \param count \output Pointer to retrieve the count of defined Recorders, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderCount(TAsap3Hdl hdl, unsigned long *count);

//! returns a Recorder ID form the Recorder list
/*! \param hdl \input Asap3 Handle
 *  \param index \input Recorder index (0..Asap3GetRecorderCount()
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderByIndex(TAsap3Hdl hdl, unsigned long index, TRecorderID *recorderID);

//! returns a Recorder ID form the Recorder list
/*! \param hdl \input Asap3 Handle
 *  \param recordername \input the name of a Recorder
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderByName(TAsap3Hdl hdl,char * recordername,TRecorderID *recorderID);

//! Selects a defined Recorder (see Asap3SetupDataAcquisitionChnl)
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectRecorder(TAsap3Hdl hdl,TRecorderID recorderID);

//! Retrievs the currently selected Recorder, see Asap3SetupDataAcquisitionChnl()
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \output Pointer to the Recorder ID, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSelectedRecorder(TAsap3Hdl hdl,TRecorderID *recorderID);

//! Removes a Recorder Please note that the currently selected Recorder can not be removed
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \output Pointer to the Recorder ID, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3RemoveRecorder(TAsap3Hdl hdl,TRecorderID recorderID);

//! Retrieves the MDF Filename of a Recorder (see Asap3GetMdfFilename)
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param FileName \output character buffer to retrieve the Recorder name
 *  \param size \output size of the FileName buffer
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderMdfFileName(TAsap3Hdl hdl,TRecorderID recorderID,char *FileName,DWORD *size);

//! Sets the MDF Filename for a Recorder, see Asap3SetMdfFilename()
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param FileName \output character buffer to retrieve the Recorder name
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetRecorderMdfFileName(TAsap3Hdl hdl,TRecorderID recorderID,char *FileName);

//! Sets the Data Reduction parameter for a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param Reduction \input Reduction parameter (e.g Reduction=1 every value,Reduction=2 every second value, Reduction=n every n'th value )
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetRecorderDataReduction(TAsap3Hdl hdl,TRecorderID recorderID,int Reduction);

//! Returns the Data Reduction parameter for a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param Reduction \output Pointer to the Reduction parameter
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderDataReduction(TAsap3Hdl hdl,TRecorderID recorderID,int *Reduction);

//! Returns the state of a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param State \output Pointer to the EnRecorderState parameter
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderState(TAsap3Hdl hdl,TRecorderID recorderID,EnRecorderState *State);

//! Pauses recording into the mdf file
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param Pause \output if Pause = true the Recorder pauses recording, if Pause = false the Recorder continues recording
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3PauseRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool Pause);

//! Starts the recording into the mdf file
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StartRecorder(TAsap3Hdl hdl,TRecorderID recorderID);

//! Stops the recording and writes an MDF File
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param save2Mdf \input saves the mdf file
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StopRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool save2Mdf);

//! Enables or disables a Recorder
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param enable \input Enables a Recorder (enable=true) or activates it (enable=false)
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3EnableRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool enable);

//! Ask a Recorder whether it is enabled or disabled
/*! \param hdl \input Asap3 Handle
 *  \param recorderID \input the Recorder ID, see Asap3DefineRecorder()
 *  \param enabled \output returns true if the Recorder is enabled, otherwise it returns false
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRecorderEnabled(TAsap3Hdl hdl,TRecorderID recorderID,bool *enabled);

//! Clear the data acquisition channel list of a specific module.
/*! \param hdl \input Asap3 Handle
 *  \param hmod \input module Handle
*/
//! \note this function only clears these measurement objects from the API-Measurement-List
//! \note which are defined by API and the requested module

extern bool ASAP3_EXPORT CALL_CONV Asap3ResetDataAcquisitionChnlsByModule(TAsap3Hdl hdl, TModulHdl hmod);
//! Clear the data acquisition channel list.

//! \param hdl \input Asap3 Handle
//! \note this function only clears these measurement objects from the API-Measurement-List
//! \note which are defined by API

extern bool ASAP3_EXPORT CALL_CONV Asap3ResetDataAcquisitionChnls(TAsap3Hdl hdl);



//! Enables the SyncMode
/*! \param hdl \input Asap3 Handle
 *  \param enabled \input enables the CANape timesync option
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3TimeSync(TAsap3Hdl hdl,bool enabled);
//! Verifies if the SyncMode is enabled
/*! \param hdl \input Asap3 Handle
 *  \param enabled \input enables the CANape timesync option
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsTimeSyncEnabled(TAsap3Hdl hdl,bool *enabled);


//! Start data acquisition
/*! \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StartDataAcquisition(TAsap3Hdl hdl);

//! Connects to a already running measurement. This function is only in the InteractiveMode available
/*! \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ConnectDataAcquisition(TAsap3Hdl hdl);

//! Start data acquisition in Resume mode
/*! \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StartResumedDataAcquisition(TAsap3Hdl hdl);


//! Stop data acquisition
/*! \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StopDataAcquisition(TAsap3Hdl hdl);


//! Disconnects from a already running measurement. This function can only be used is Asap3ConnectDataAcquisition was called before
/*! \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3DisconnectDataAcquisition(TAsap3Hdl hdl);


//! Number of samples in FIFO
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param taskId \input Id of the task to query.
 *  \return number of samples in FIFO.
 */
extern long ASAP3_EXPORT CALL_CONV Asap3GetFifoLevel(TAsap3Hdl hdl, TModulHdl module, unsigned short taskId);

//! Check if data have been lost due to FIFO overrun.
/*! Asap3CheckOverrun doesn't have any impact to the FIFO data. All data are
 *  available excluding the data record which caused the overrun.
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param taskId \input Id of the task to query.
 *  \param resetOverrun \input Reset the overrun flag in CANape.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3CheckOverrun(TAsap3Hdl hdl, TModulHdl module, unsigned short taskId, bool resetOverrun);

//! Get next sample from FIFO.
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param taskId \input Id of the task to query.
 *  \param timeStamp \output Timestamp of the returned sample. The time stamps are generated by CANape.
 *  \param values \output Array of sampled values, the order is equivalent to the calls of Asap3SetupDataAcquisitionChnl().
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNextSample(TAsap3Hdl hdl,
                   TModulHdl module,       // Input !!!!neu, jetzt Input!!!
                   unsigned short taskId,  // Input !!!!neu, jetzt Input!!!
                   ::TTime * timeStamp,       // Output
                   double ** values);       // Output: array of sampled values,
                                           //   the order is equivalent to the
                                           //   calls of SetupDataAcquisitionChnl()

//! Get current values, returns the last received values, does neither use nor effect the FIFO.
/*! Use Asap3ResetDataAcquisitionChnls(), Asap3GetEcuTasks(), Asap3SetupDataAcquisitionChnl() and
 * Asap3StartDataAcquisition() to setup a data acquisition process. The work flow needs to call
 * Asap3GetNextSample() to get each acquired data.
 * Asap3GetNextSampleBlock(...) to get acquired data in blockmode
 * Asap3GetCurrentValues() does not require to setup the FIFO using Asap3SetupFifo()
 * because the FIFO is not used.
 * As well as CANape inserts all received values to the FIFO and the client is able to
 * asynchronously read this values form FIFO by Asap3GetNextSample(), Asap3GetCurrentValues()
 * returns the last values received from ECU.
 *  \param hdl \input Asap3 Handle
 *  \param _module \input Points to demanded module.
 *  \param _taskId \input Id of the task to query.
 *  \param timeStamp \output Timestamp of the returned sample. The time stamps are generated by CANape.
 *  \param values \output Array of sampled values, the order is equivalent to the calls of Asap3SetupDataAcquisitionChnl().
 *  \param maxValues \input Maximum number of values saved to 'values'
 */




extern bool ASAP3_EXPORT CALL_CONV Asap3GetCurrentValues(TAsap3Hdl hdl,
                                TModulHdl _module,      // Input !!!!neu, jetzt Input!!!
                                unsigned short taskId, // Input !!!!neu, jetzt Input!!!
                                ::TTime * timeStamp,      // Output
                                double * values,        // Output: array of sampled values,
                                                        //   the order is equivalent to the
                                                        //   calls of SetupDataAcquisitionChnl()
                                                        //   Note: the client has to allocate memory
                                unsigned short maxValues);  // max number of values saved to 'values'


//! Get next sample block from FIFO.
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param taskId \input Id of the task to query.
 *  \param count_of_Samples \input count of samples, the client wants to receive - if count_of_Samples is set to -1
 *  all samples stored in the FIFO buffer are transmitted
 *  \param **values \output tSampleBlockObject : this value carries the data
 */
bool ASAP3_EXPORT CALL_CONV Asap3GetNextSampleBlock(TAsap3Hdl hdl,
                                TModulHdl _module,                   // input Asap3 Handle
                                unsigned short taskId,              // input Points to demanded module.
                                long count_of_Samples ,              // input count of samples
                                tSampleBlockObject ** values);       // Output: this value carries the data


//! Switches the NAN identification on or off. The default value in CANape is 1. This switch has only an influence on monitoring devices
/*! \param hdl \input Asap3 Handle
 *  \param use \input switches the NAN on (1) or off (0)
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3UseNAN(TAsap3Hdl hdl,bool use);

//! Returns the value of the NAN identification. The default value in CANape is 1. This switch has only an influence on monitoring devices
/*! \param hdl \input Asap3 Handle
 *  \param use \output value of the NAN switch (1 = enabled (default)) or off (0= disabled)
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3IsNANUsed(TAsap3Hdl hdl,bool *use);


//! Set measurement data filename.
/*! \param hdl \input Asap3 Handle
 *  \param mdfFilename  \input Name of the used MDF file.
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3SetMdfFilename(TAsap3Hdl hdl, const char *mdfFilename);

//! Get measurement data filename.
/*! \param hdl \input Asap3 Handle
 *  \param mdfFilename \output Name of the used MDF file.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMdfFilename(TAsap3Hdl hdl, char ** mdfFilename);

//! Select a label list with stored measurement objects by name.
/*! \param hdl \input Asap3 Handle
*  \param Name \input Name of the used MDF file.
*  \param includeMeaMode \input set items active if existing in measurement list.
*  \param mode \input compares label list to the existing measurement list.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectLabelList(TAsap3Hdl hdl, char *Name, bool includeMeaMode = false, int mode = 1);


/** @} end of DataAcqusition */


/** @defgroup Converter Converter Functions
 *  @ingroup ApiFunctions
 *  @{
 */

//! Convert to Matlab (this function is deprecated - please use Asap3MDFConvert instead)
/*! Converts an existing MDF File in Matlab Format and saves it with the given matlabFilename.
 *  \param hdl \input Asap3 Handle
 *  \param mdfFilename \input Name of the source MDF file.
 *  \param matlabFilename \output Name of the destination Matlab file.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3MatlabConversion(TAsap3Hdl hdl, const char *mdfFilename, const char *matlabFilename);

//! Convert to Matlab (this function is deprecated - please use Asap3MDFConvert instead)
/*! Same function as Asap3MatlabConversion. The difference here is that Asap3MatlabConversionAsync runs asynchronous
 *  \param hdl \input Asap3 Handle
 *  \param mdfFilename \input Name of the source MDF file.
 *  \param matlabFilename \output Name of the destination Matlab file.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3MatlabConversionAsync(TAsap3Hdl hdl, const char *mdfFilename, const char *matlabFilename);


//! Determines the count of installed MDF Converters
/*!
 *  \param hdl \input Asap3 Handle
 *  \param count \output the cout of installed MDF converters
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConverterCount(TAsap3Hdl hdl,int *count);

//! Converts an MDF file into a different format
/*! Converts an existing MDF File into a different export Format and saves it with the given destFilename.
 *  \param hdl \input Asap3 Handle
 *  \param converterID \input Converter ID of an existing CANape MDF converter. The converter ID's can be determine with the function Asap3MDFConverterInfo
 *  \param mdfFilename \input Name of the source MDF file.
 *  \param destFilename \output Name of the destination Matlab file.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConvert(TAsap3Hdl hdl,char *converterID ,const char *mdfFilename,const char *destFilename,bool overwrite);

//! Information concerning a special MDF converter
/*!
 *  \param hdl \input Asap3 Handle
 *  \param index \input index of the converter
 *  \param item \output TConverterInfo containing information about the converter.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConverterInfo(TAsap3Hdl hdl,int index,TConverterInfo* item);


/** @} end of Converter */



// -----------------------------------------------------------------------------------------------------------------
// Misc
// ~~~~

/** @defgroup NetWork NetWork Functions
 *  @ingroup ApiFunctions
 *  @{
 */

// -----------------------------------------------------------------------------------------------------------------
// NetWork Functions
// ~~~~~~~~~~~~~~~~
//! Receives the name of the used network
/*!
 *  \param hdl \input Asap3 Handle
 *  \param module \input module handle of a device
 *  \param Name \output Buffer for the network name
 *  \param sizeofName \output size of the buffer
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNetworkName(TAsap3Hdl hdl,TModulHdl module,char *Name, unsigned int * sizeofName);
//! Receives the name devices which are mapped to the given network interface
/*!
 *  \param hdl \input Asap3 Handle
 *  \param Name \input name of the network
 *  \param ModuleArray \output Module array
 *  \param count \output size the module array
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNetworkDevices(TAsap3Hdl hdl,char *Name, TModulHdl * ModuleArray,unsigned int *count);
//! Activates or disactivates a given network interface
/*!
 *  \param hdl \input Asap3 Handle
 *  \param Name \input name of the network
 *  \param activate \output activates (true) the network or deactivates it (false)
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ActivateNetwork(TAsap3Hdl hdl,char *Name, bool activate);
//! Receives the state a given network interface
/*!
 *  \param hdl \input Asap3 Handle
 *  \param Name \input name of the network
 *  \param activated \output state of network (true=active) or  (false = deactivated)
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3IsNetworkActivated(TAsap3Hdl hdl,char *Name, bool *activated);


//! returns the number of security profiles
/*! \param hdl \input Asap3 Handle
*   \param count \output Pointer to retrieve the number of defined security profiles
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileCount(TAsap3Hdl hdl, unsigned int* count);

//! returns the identifiers of the security profiles
/*! \param hdl \input Asap3 Handle
*   \param identifiers \output Pointer to retrieve the concatenated string (delimiter ';') of available profile identifiers
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileIdentifier(TAsap3Hdl hdl, char* identifiers, DWORD* sizeofBuffer);

//! returns the identifier, name and description of certain security profile
/*! \param hdl \input Asap3 Handle
*   \param id  \input profile identifier
*   \param entry \output Pointer to security profile entry consists of id, name and description
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileInfo(TAsap3Hdl hdl, unsigned int id, SecProfileEntry* entry);

//! assign the profile identifier to a certain network
/*! \param hdl \input Asap3 Handle
*   \param profileId  \input profile identifier
*   \param networkName \input network name
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3AddSecProfileToNetwork(TAsap3Hdl hdl, unsigned int profileId, char* networkName);

/** @} end of NetWork Functions */
// -----------------------------------------------------------------------------------------------------------------
// NetWork Functions
// ~~~~




/** @defgroup Misc Miscellaneous Functions
 *  @ingroup ApiFunctions
 *  @{
 */
//! Send CCP request
// ~~~~~~~~~~~~~~~~
/*! ResponseTimeout = 0 indicates that no response is expected.
 *  Valid Range of RequestSize and ResponseSize = {1...8}.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3_CCP_Request(TAsap3Hdl hdl,
                         TModulHdl module,
                         const unsigned char *requestData,
                         unsigned long  requestSize,
                         unsigned long  responseTimeout,      // in milliseconds
                         unsigned char * responseData,
                         unsigned long  maxResponseSize,
                         unsigned long * responseSize);

//! Execute a script
// ~~~~~~~~~~~~~~~~~~
/*! Execute a script file or a single script command.
 * \param hdl \input Asap3 Handle
 * \param module \input assigns the script command to a certain module.
 * \param scriptFile \input declares interpretation of parameter script.
 * If 'scriptFile' is true, parameter 'script' is interpreted as the file name
 * of the script file to be executed. If 'scriptFile' is false, 'script' is
 * interpreted as a single script command.
 * \param *script \input a scriptfilename or an single script command
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ExecuteScript(TAsap3Hdl hdl,
                                                      TModulHdl module,
                                                      bool scriptFile,
                                                      const char * script);


//! ASAP2 Object Selection Dialog+
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/*! Select measurement or calibration objects using the database selection dialogs of CANape.
 * The selection list appears and a 2-step manual selection can be performed.
 * <br> 1. Select the folder.
 * <br> 2. Select one or more measurement or calibration objects.
 *
 * The result of selection is stored to file \<fname\>. The file contains the
 * identifiers of selected objects covered in quotation marks separated by \<CRLF\>.
 * Quotation marks inside identifiers must be indicated using double quotation
 * marks.
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param type \input selector to declare an object to be used for measurement or calibration.
 *  \param *fname \input  name of file where the selection has to be stored.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectObjects(TAsap3Hdl hdl, TModulHdl module,
                                       TObjectType type, const char *fname);
//! \if RESTORE_WND
/*! Maximize the CANape main window
 *  \param hdl \input Asap3 Handle
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3RestoreWndSize(TAsap3Hdl hdl);
//! \endif

//! \if RESTORE_WND
/*! Maximize the CANape main window
 *  \param hdl \input Asap3 Handle
 *  \param hdl \input Window params e.g. SW_HIDE,SW_MINIMIZE,SW_MAXIMIZE,SW_SHOWM,SW_RESTORE
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3RestoreWndSize2(TAsap3Hdl hdl, long params);
//! \endif


//! ASAP2 Asap3CopyBinaryFile
//
/*! Copies data from a given source to a given destination.
 * The started CANape operation depends on the given parameters.
 * The following table shows the CANape actions:
 *
 *  <table><tr><td>sourcetype/<br>dest.type</td><td>FILE</td><td>VIRTUAL</td><td>PHYSICAL</td></tr>
 *  <tr><td>FILE</td><td>NONE</td><td>save</td><td>upload & save</td></tr>
 *  <tr><td>VIRTUAL</td><td>load</td><td>NONE</td><td>upload</td></tr>
 *  <tr><td>PHYSICAL</td><td>load & download</td><td>download</td><td>NONE</td></tr>
 *  </table>
 *
 *  \attention The interface only works with devices which are online. This mode ensures that the physical and virtual memory contains the same data.
 *
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param sourcetype \input type of source
 *  \param desttype  \input  type of destination
 *  \param filename \input filename, if either of the input types is FILE.
 *
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3CopyBinaryFile(TAsap3Hdl hdl, TModulHdl module, TAsap3FileType sourcetype, TAsap3FileType desttype, const char *filename);



//! ASAP2 Asap3ReadObjectParameter
//
/*! Queries information of a object
 *  \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param objectName \input name of the object to query
 *  \param format     \input kind of representation of the data
 *  \param type       \output type of the queried object
 *  \param address    \output address of the queried object
 *  \param min        \output minimum value of the queried object
 *  \param max        \output maximum value of the queried object
 *  \param increment  \output increment of the queried object
 *
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadObjectParameter(TAsap3Hdl hdl, TModulHdl module, const char *objectName, TFormat format, TAsap3DataType * type, unsigned long * address, double * min, double * max, double * increment);

/** @} end of Misc */


/** @defgroup  Scripting Scripting Functions
 *  @ingroup ApiFunctions
 *  privides access to CANape scripts
 *  @{
 */
//! Extended Execute a script
// ~~~~~~~~~~~~~~~~~~
/*! Execute a script file or a single script command.
 * \param hdl \input Asap3 Handle
 * \param module \input assigns the script command to a certain module.
 * \param scriptFile \input declares interpretation of parameter script.
 * If 'scriptFile' is true, parameter 'script' is interpreted as the file name
 * of the script file to be executed. If 'scriptFile' is false, 'script' is
 * interpreted as a single script command.
 * \param *script \input a scriptfilename or an single script command
 * \param hScript \output Handle to script.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ExecuteScriptEx(TAsap3Hdl hdl,
                                                      TModulHdl module,
                                                      bool scriptFile,
                                                      const char * script,
                                                      TScriptHdl *hScript);

//! Returns the state of a script
// ~~~~~~~~~~~~~~~~~~
/*! Execute a script file or a single script command.
 * \param hdl \input Asap3 Handle
 * \param hScript \input Handle of the script returned by Asap3ExecuteScriptEx
 * \param TScriptStatus \output current state  of the script
 * \param textBuffer \output returns the state as text
 *  this parameter can be NULL.
 * \param sizeofbuffer \output returns the text length  this parameter can be NULL
 *  this parameter can be NULL.
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptState (TAsap3Hdl hdl,TScriptHdl hScript,TScriptStatus *scrstate,char *textBuffer,DWORD *sizeofbuffer);

//! Stops a running script
// ~~~~~~~~~~~~~~~~~~
/*!
 * \param hdl \input Asap3 Handle
 * \param hScript \input Handle of the script returned by Asap3ExecuteScriptEx
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StopScript     (TAsap3Hdl hdl,TScriptHdl hScript) ;


//! Starts a defined script
// ~~~~~~~~~~~~~~~~~~
/*!
 * \param hdl \input Asap3 Handle
 * \param scriptFile \input Handle of the script returned by Asap3ExecuteScriptEx
 * \param Commandline \input Set a commandline for the script
 * This parameter is optional
 * \param moduleHdl \input Set a module as current_device
 * This parameter is optional
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3StartScript    (TAsap3Hdl hdl,TScriptHdl hScript,char *Commandline = NULL,TModulHdl moduleHdl=ASAP3_INVALID_MODULE_HDL) ;

//! Returns the exitcode of a script
// ~~~~~~~~~~~~~~~~~~
/*! The type of the exitcode is always double
 * \param hdl \input Asap3 Handle
 * \param scriptFile \input Handle of the script returned by Asap3ExecuteScriptEx
 * \param Value \output Exitcode value of the script
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptResultValue(TAsap3Hdl hdl,TScriptHdl hScript,double *Value);

//! Returns a scriptresult
// ~~~~~~~~~~~~~~~~~~
/*! returns the result value of a script. The type of the exit code is always string
 * to receive the result you must use the script function "SetScriptResult"
 * \param hdl \input Asap3 Handle
 * \param hScript \input Handle of the script returned by Asap3ExecuteScriptEx
 * \param resultString \output result value of the script
 * \param sizeofBuffer \output size of the result
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptResultString(TAsap3Hdl hdl,TScriptHdl hScript,char*resultString,DWORD *sizeofBuffer);

//! Removes a script
// ~~~~~~~~~~~~~~~~~~
/*! removes a declared script from the Task list
 * to receive the result you must use the script function "SetScriptResult"
 * \param hdl \input Asap3 Handle
 * \param hScript \input Handle of the script returned by Asap3ExecuteScriptEx
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseScript(TAsap3Hdl hdl,TScriptHdl hScript) ;

/** @} end of Scripting */



/** @defgroup  Diag Diagnostic Functions
 *  @ingroup ApiFunctions
 *  privides diagnostic access to devices
 *  @{
 */


// -----------------------------------------------------------------------------------------------------------------
// Diagnostic access Functions
// ~~~~~~~~~~~~~~~~~~~~~~~~~


//! Enables or disables the Tester Present request
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param enable \input enables or disables the Tester Present request
 *
*/
extern bool ASAP3_EXPORT CALL_CONV  Asap3DiagEnableTesterPresent(TAsap3Hdl hdl, TModulHdl module,bool enable);

//! Returns information concerning the Tester Present request state
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param enabled \output status of the  Tester Present request
 *
*/
extern bool ASAP3_EXPORT CALL_CONV  Asap3DiagIsTesterPresentEnabled(TAsap3Hdl hdl, TModulHdl module, bool *enabled);

//!Executes a diagnostic Job
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param job \input name of the Job
 *  \param commandline \input optional commandline
 *  \param reserved\input reserved parameter
 *  \param jobResponse \output Handle of the Job
 *
*/

extern bool ASAP3_EXPORT CALL_CONV  Asap3DiagExecuteJob(TAsap3Hdl hdl, TModulHdl module,char *job,char *commandline,bool reserved,DiagJobResponse** jobResponse);

//! Creates a Raw Diagnostic request (Asap3DiagCreateRawRequest is deprecated - use Asap3DiagCreateRawRequest2 instead)
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param ServiceBytes \input name as a Byte Stream
 *  \param length \length of the Byte stream
 *  \param hDiag \output Handle of the Service
 *
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateRawRequest(TAsap3Hdl hdl, TModulHdl module,BYTE *ServiceBytes,unsigned int length,TAsap3DiagHdl *hDiag);



//! Creates a Raw Diagnostic request
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param ServiceBytes \input name as a Byte Stream
 *  \param length \length of the Byte stream
 *  \param hDiag \output Handle of the Service
 *
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateRawRequest2(TAsap3Hdl hdl, TModulHdl module,BYTE *Bytes,unsigned int length,TAsap3DiagHdl *hDiag);

//! Creates a Symbolic Diagnostic request
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param ServiceName \input name (CDD)Service name/path
 *  \param hDiag \output Handle of the Service
 *
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateSymbolicRequest(TAsap3Hdl hdl, TModulHdl module, char *ServiceName,TAsap3DiagHdl *hDiag);


//! Set Parameters for the ServiceNotification
/*! \param hDiag \input Handle of the Service
 *  \param CallbackFunction \input CallbackFunction for notification
 *  \param PrivateData \input Userdefined PrivateData
 *
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetNotificationParameters(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,FNCDIAGNOFIFICATION CallbackFunction,void *PrivateData);

//! Executes a Diagnostic request
/*! \param hdl \input Asap3 Handle
 *  \param hDiag \input Handle of the Service
 *  \param SupressPositiveResponse \input a positive response will not be sent by the ECU
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagExecute(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,BOOL SupressPositiveResponse);


//! Queries the state of a Request
/*!  \param hdl \input Asap3 Handle
 *  \param hDiag \input Handle of the Service
 *  \param hDiag \output Current service state
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetServiceState(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,eServiceStates *State);

//! Removes a service
/*! \param hdl \input Asap3 Handle
 *  \param hDiag \input Handle of the Service
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagReleaseService(TAsap3Hdl hdl,TAsap3DiagHdl hDiag);


//! Set a Symbolic Parameter Value
/*! \param hdl \input Asap3 Handle
 *  \param hDiag \input Handle of the Service
 *  \param ParameterName \input Name of the service parameter
 *  \param ParameterValue \input Symbolic string parameter value
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetStringParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,char* ParameterValue);

//! Set a Raw Parameter Value
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the Service
 *  \param ParameterName \input name of the service parameter
 *  \param ParameterValue \input RAW parameter value
 *  \param Size \input Size of the parameter Value in bytes
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetRawParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,BYTE* ParameterValue,DWORD Size);

//! Set a UNSIGNED Parameter Value
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param ParameterName \input name of the service parameter
 *  \param ParameterValue \input numeric parameter value
*/


extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetNumericParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,DiagNumericParameter *Parameter);

//! Returns the count of incoming responses
/*! \param hdl \input Asap3 Handle
 *  \param hDiag \input handle of the service
 *  \param Count \output count of responses
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseCount(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,unsigned int *Count);



//! Ask whether the response is positive or negative
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param ResponseID \input Index number of the response
 *  \param IsPositive\output true, if there was a positive response

*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagIsPositiveResponse(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,long ResponseID,BOOL *IsPositive);



//! Returns the Raw response byte stream
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param Stream \output ByteStream
 *  \param Size \output size of the byte stream
 *  \param ResponseID \input Index number of the response
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseStream(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,BYTE* Stream,DWORD *Size,long ResponseID);

//! Returns a symbolic response parameter
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the Service
 *  \param name \input parameter name
 *  \param ResponseID \input Index number of the response
 *  \param *Data \output response result as char array
 *  \param *Size \output  Size of the char array
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetStringResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *Data,DWORD *Size);

//! Returns a raw response parameter
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the Service
 *  \param name \input parameter name
 *  \param ResponseID \input Indexnumber of the response
 *  \param *Data \output response result as char array
 *  \param *Size \output  Size of the char array
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetRawResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,unsigned char *Data,DWORD *Size);

//! Returns a parameter value in numerical form
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param name \input parameter name
 *  \param ResponseID \input index number of the response
 *  \param DiagNumericParameter \output result of the response Paramter
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetNumericResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,DiagNumericParameter *);

//! Checks whether the response parameter is complex or not
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the Service
 *  \param name \input parameter name
 *  \param ResponseID \input index number of the response
 *  \param IsComplex \output for a complex parameter IsComplex is true
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagIsComplexResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,BOOL *IsComplex);

//! Returns the raw response byte stream
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the Service
 *  \param name \input parameter name
 *  \param ResponseID \input index number of the response
 *  \param SubParameter \input name of the SubParamater
 *  \param InterationIndex \input iteration index of the complex response
 *  \param *Parameter \output complex parameter item
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexNumericResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,DiagNumericParameter *Parameter);

//! Returns String response of complex parameter
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param name \input parameter name
 *  \param ResponseID \input index number of the response
 *  \param SubParameter \input name of the SubParamater
 *  \param InterationIndex \input iteration index of the complex response
 *  \param *Data \output response result as char array
 *  \param *Size \output Size of the char array
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexStringResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,char *Data,DWORD *Size);


//! Returns the raw response byte stream
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param name \input parameter name
 *  \param ResponseID \input index number of the response
 *  \param SubParameter \input name of the SubParamater
 *  \param InterationIndex \input iteration index of the complex response
 *  \param *Data \output response result as char array
 *  \param *Size \output size of the char array
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexRawResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,char *Data,DWORD *Size);


//! Returns the raw response byte stream
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param ResponseID \input index number of the response
 *  \param *Code \output response code
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseCode(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,long ResponseID,BYTE *Code);


//! Returns the count of iterations concerning a given parameter
/*! \param hdl \input Asap3 handle
 *  \param hDiag \input handle of the service
 *  \param ResponseID \input index number of the response
 *  \param *Iteration \input/output Number of possible iterations
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexIterationCount(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *Parameter,long ResponseID,unsigned long *Iteration);

/** @} end of Diag */



// -----------------------------------------------------------------------------------------------------------------
// Configuration functions
// -----------------------------------------------------------------------------------------------------------------


/** @defgroup  Configuration
 *  @ingroup ApiFunctions
 *  privides configuration file access
 *  @{
 */

//! Call this function to to load a configuration file (CNA)"
/*!  \param hdl \input Asap3 Handle
 *   \param FileName \input Name of the CNA file
 */

bool ASAP3_EXPORT CALL_CONV Asap3LoadCNAFile(TAsap3Hdl hdl,char* configFileName);

//! Call this function to get the current name of the used CNA file. This name is only available if CANape run in the nonmodal ASAP3 mode. If there is no CNA loaded (also in server mode) "CANAPE is returned"
/*!  \param hdl \input Asap3 Handle
 *   \param FileName \output Name of the current used CNA file
 *   \param Size     \output output size of the FileName buffer
 */

extern bool ASAP3_EXPORT CALL_CONV Asap3GetCNAFilename(TAsap3Hdl hdl,char *FileName,unsigned int *Size);


/** @} end of Configuration */

/** @defgroup  Patchfunctions
 *  @ingroup ApiFunctions
 *  Patches CANape project file
 *  @{
 */

 //! Call the function Asap3GetCanapeModuleParam to get access on the module section in the CANape Project file (CANape.ini) and reads a parameter
 /*! \param hdl \input Asap3 Handle
 *   \param module \input points to demanded module.
 *   \param param \input parameter name in the section
 *   \param value \output value of the requested parameter
 *   \param sizeofValue     \output  output size of the value buffer
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCanapeModuleParam(TAsap3Hdl hdl, TModulHdl module, char *param, char *value, unsigned int *sizeofValue);

//! Call the function Asap3GetCanapeModuleParam to get access on the module section in the CANape Project file (CANape.ini) and writes a parameter
 /*! \param hdl \input Asap3 Handle
 *   \param module \input points to demanded module.
 *   \param param \input parameter name in the section
 *   \param value \output value of the requested parameter

 */
extern bool ASAP3_EXPORT CALL_CONV Asap3SetCanapeModuleParam(TAsap3Hdl hdl, TModulHdl module, char* param, char *value);

 //! Call the function Asap3GetCanapeModuleParam to get access on the module section in the CANape Project file (CANape.ini) and reads a parameter
 /*! \param hdl \input Asap3 Handle
 *   \param section \input section of the requested parameter
 *   \param param \input parameter name in the section
 *   \param value \output value of the requested parameter
 *   \param sizeofValue     \output output size of the value buffer
 */
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCanapeProjectParam(TAsap3Hdl hdl, char *Section, char *param, char *value, unsigned int *sizeofValue);

//! Call the function Asap3SetCanapeModuleParam to get access on the module section in the CANape Project file (CANape.ini) and writes a parameter
/*! \param hdl \input Asap3 Handle
*   \param section \input section of the requested parameter
*   \param param \input parameter name in the section
*   \param value \output value of the requested parameter
*/

extern bool ASAP3_EXPORT CALL_CONV Asap3SetCanapeProjectParam(TAsap3Hdl hdl, char *Section, char *param, char* value);

/** @} end of Patchfunctions */

/** @defgroup  Flash Flash Functions
 *  @ingroup ApiFunctions
 *  privides diagnostic access to devices
 *  @{
 */



// -----------------------------------------------------------------------------------------------------------------
// Flash functions
// ~~~~~~~~~~~~~~~~~~~~~~~~~



//!  References an Flash ODX Container file
/*! \param hdl \input Asap3 Handle
 *  \param module \input Points to demanded module.
 *  \param OdxContainerfile \input Filename of the ODX container
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashSetODXContainer(TAsap3Hdl hdl,TModulHdl module,const char *ODXContainerfile);


//!  Returns the count of defined Sessions
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
 *  \param Count \output session count
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetSessionCount(TAsap3Hdl hdl,TModulHdl module,unsigned long *Count);


//!  Returns the name of a Session by index
/*! \param hdl \input Asap3 handle
 *  \param module \input Points to demanded module.
 *  \param index \input session count
 *  \param Name \output session name
 *  \param Name \output buffer size of the name parameter

*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetSessionName(TAsap3Hdl hdl,TModulHdl module,unsigned long index,char *Name,long *SizeOfName);



//!  Returns the count of defined jobs
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
 *  \param Count \output job count
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobCount(TAsap3Hdl hdl,TModulHdl module,unsigned long *Count);


//!  Returns the name of a job by index
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
 *  \param index \input job count
 *  \param Name \output job name
 *  \param Name \output buffer size of the paramter name

*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobName(TAsap3Hdl hdl,TModulHdl module,unsigned long index,char *Name,long *SizeOfName);



//!  Start the flash procedure
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
 *  \param SessionName \input name of the flash session
 *  \param JobName \input name of the job or a flashscript
 *  \param ConfigFileName \input name of a configuration file. If this parameter is set to NULL, the configuration file is ignored

*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashStartFlashJob(TAsap3Hdl hdl,TModulHdl module,const char *SessionName, const char *JobName, const char *ConfigFileName);


//!  Asks for a Flashjob's current state
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
 *  \param isRunning  \output isRunning  TRUE = yes FALSE = no
 *  \param Progress   \output progress of the flashjob in percent
 *  \param Info       \output text information
 *  \param SizeofInfo \output sizeof buffer

*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobState(TAsap3Hdl hdl,TModulHdl module,double *ScriptResult,BOOL *isRunning,long *Progress,char *Info,unsigned long *SizeofInfo);

//!  Stops a Flashjob
/*! \param hdl \input Asap3 handle
 *  \param module \input points to demanded module.
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashStopJob(TAsap3Hdl hdl,TModulHdl module);

/** @} end of Flash */

// CallBack Events -----------------------------------------------------------

/** @defgroup CallBack Events
 *  @ingroup ApiFunctions
 *  @{
 */



//!  Enables the Interactive mode of CANape.
/*! \param hdl \input Asap3 handle
 *  \param mode \input Set this parameter to true to enable the interactive mode, otherwise set this parameter to false
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3SetInteractiveMode(TAsap3Hdl hdl,bool mode);

//!  Returns information about the InteractiveMode.
/*! \param hdl \input Asap3 handle
 *  \param mode \input This parameter returns true if the interactive mode is enabled, otherwise false will be returned
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3GetInteractiveMode(TAsap3Hdl hdl,bool *mode);

//!  Registers a callback event.
/*! \param hdl \input Asap3 handle
 *  \param eventID\input Event type
 *  \param fnc\input  callback function pointer
 *  \param privateData \input optional usable for private data which will be returned in the fnc function parameter privateData
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3RegisterCallBack(TAsap3Hdl hdl,ASAP3_EVENT_CODE eventID,void *fnc,unsigned long privateData);

//!  Unregisters a callback event.
/*! \param hdl \input Asap3 handle
 *  \param eventID\input Event type
*/
extern bool ASAP3_EXPORT CALL_CONV Asap3UnRegisterCallBack(TAsap3Hdl hdl,ASAP3_EVENT_CODE eventID);

//!  Callbackfunction ONMEASUERMENT_START
/*! \param hdl \input Asap3 handle
 *  \param privateData \input private data defined in \link Asap3RegisterCallBack \endlink
*/
typedef long (CALLBACK* ONMEASUERMENT_START)        (TAsap3Hdl Hdl,unsigned long privateData);

//!  Callbackfunction ONMEASUERMENT_STOP
/*! \param hdl \input Asap3 handle
 *  \param privateData \input private data defined in \link Asap3RegisterCallBack \endlink
*/
typedef long (CALLBACK* ONMEASUERMENT_STOP)         (TAsap3Hdl Hdl,unsigned long privateData);

//!  Callbackfunction ONMEASUERMENT_BEFORE_START
/*! \param hdl \input Asap3 handle
 *  \param privateData \input private data defined in \link Asap3RegisterCallBack \endlink
*/
typedef long (CALLBACK* ONMEASUERMENT_BEFORE_START) (TAsap3Hdl Hdl,unsigned long privateData);

//!  Callbackfunction ON_EXIT
/*! \param hdl \input Asap3 handle
 *  \param privateData \input private data defined in \link Asap3RegisterCallBack \endlink
*/
typedef long (CALLBACK* ON_EXIT)                   (TAsap3Hdl Hdl,unsigned long privateData);


// End CallBack Events -----------------------------------------------------------
/** @} end of CallBack Events */



extern bool ASAP3_EXPORT CALL_CONV Asap3ConnectToCANape(TAsap3Hdl *hdl, const char *VillaRelease, const char *Directory, const char *language);


extern bool ASAP3_EXPORT CALL_CONV Asap3DisconnectFromCANape(TAsap3Hdl hdl);


extern bool ASAP3_EXPORT CALL_CONV Asap3OpenDisplayForFile(TAsap3Hdl hdl,const char *Patternfile);



extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseResultList(TAsap3Hdl hdl,const int CountResults, const char *ResultList[]);



extern bool ASAP3_EXPORT CALL_CONV Asap3OpenDisplay ( TAsap3Hdl hdl, const char *Title,
                                                       int         Editable,
                                                       int         Graphical,
                                                       int         CountParameterLabelsList,
                                                       const char *ParameterLabelList[],
                                                       const char *DataDescFile,
                                                       const char *DataVersFile,
                                                       int         CountAppHistList,
                                                       const char *AppHistLabelList[],
                                                       const char *AppHistTextList[],
                                                       const char *AppHistDefault,
                                                       int        *CountModified,
                                                       const char **ModifiedLabelList[],
                                                       int         *CountErrors,
                                                       const char **ErrorLabelList[],
                                                       int         *CountModAppList,
                                                       const char **ModAppHistLabelList[],
                                                       const char **ModAppHistTextList[]);
#ifndef MATLABAPI
}
#endif


// dummy function
extern void ASAP3_EXPORT dummy();

#include <poppack.h>
#endif //#ifndef MATLABAPI
