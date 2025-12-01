# Python CANape Module Unification Plan

## Executive Summary

This document outlines the plan to unify and restructure the Python CANape wrapper module with a modern, maintainable architecture that implements all functions from CANapAPI.h.

## 1. Technology Decision: .py vs .pyx (2025)

### Research Findings

**Recommendation: Use `.py` files with `ctypes`**

**Rationale:**
- **ctypes is sufficient**: Since we're wrapping a Windows DLL (CANapAPI64.dll), ctypes provides direct access without compilation overhead
- **Maintainability**: `.py` files are easier to maintain, debug, and work with standard Python tooling
- **No performance benefit**: Cython (.pyx) would only help if we were writing performance-critical Python code, but we're just calling DLL functions
- **Cross-platform considerations**: While CANape is Windows-only, using ctypes keeps the code simpler
- **2025 Best Practice**: Modern Python projects favor simplicity unless profiling shows bottlenecks

**Exception**: Keep the existing `cython_api/` directory for potential future Cython optimizations if needed, but primary implementation will be in `.py` files.

## 2. Proposed Module Structure

```
CANape/
├── __init__.py                 # Main package initialization, high-level API
├── _version.py                 # Version management (existing)
├── asap3/                      # ASAP3 Interface Core
│   ├── __init__.py
│   ├── initialization.py      # Asap3Init, Asap3Init2-6, Asap3Exit, etc.
│   ├── version.py              # Version and application info functions
│   ├── error_handling.py       # Error codes, error text, debug window
│   └── project.py              # Project directory, application name
├── module/                     # Module Management
│   ├── __init__.py
│   ├── creation.py             # CreateModule, AttachAsap2, etc.
│   ├── management.py           # Module activation, memory pages, etc.
│   └── database.py             # Database info, object queries
├── calibration/                # Calibration Functions
│   ├── __init__.py
│   ├── read_write.py           # Read/Write calibration objects
│   ├── address_access.py       # ReadByAddress, WriteByAddress
│   └── object_info.py          # Calibration object info functions
├── data_acquisition/           # Data Acquisition
│   ├── __init__.py
│   ├── setup.py                # Setup channels, FIFO, tasks
│   ├── control.py              # Start/Stop acquisition
│   ├── reading.py               # GetNextSample, GetCurrentValues, etc.
│   └── recorder.py              # Recorder management
├── converter/                  # File Conversion
│   ├── __init__.py
│   └── mdf.py                  # MDF conversion functions
├── diagnostic/                 # Diagnostic Functions
│   ├── __init__.py
│   ├── jobs.py                 # Diagnostic job execution
│   ├── requests.py             # Create and execute requests
│   └── responses.py            # Response parameter retrieval
├── scripting/                  # Scripting Functions
│   ├── __init__.py
│   └── execution.py            # Script execution and management
├── flash/                      # Flash Functions
│   ├── __init__.py
│   └── management.py           # Flash job management
├── network/                    # Network Functions
│   ├── __init__.py
│   └── management.py           # Network activation, security profiles
├── configuration/              # Configuration Functions
│   ├── __init__.py
│   └── project.py              # CNA file loading, project parameters
├── callbacks/                  # Callback Events
│   ├── __init__.py
│   └── events.py                # Event registration and callbacks
├── core/                       # Core Types and Utilities
│   ├── __init__.py
│   ├── types.py                # C type definitions (from existing)
│   ├── structs.py              # C structure definitions (from existing)
│   ├── enums.py                # Enum definitions (from existing)
│   ├── const.py                # Error constants (from existing)
│   ├── dll_loader.py           # DLL loading and type assignment
│   └── handle.py               # Handle management
└── exceptions.py               # Custom exceptions

tests/
├── __init__.py
├── test_initialization.py
├── test_calibration.py
├── test_data_acquisition.py
├── test_module.py
└── ...

docs/
├── api/
└── examples/

```

## 3. Function Implementation Plan

### Function Categories (from CANapAPI.h analysis: ~180 functions)

#### 3.1 Initialization & Control (15 functions)
- Asap3GetVersion
- Asap3SetTCPOptions
- Asap3Init, Asap3Init2-6
- Asap3GetProjectDirectory
- Asap3Exit, Asap3Exit2
- Asap3SetApplicationName, Asap3GetApplicationName
- Asap3GetApplicationVersion
- Asap3ErrorText
- Asap3PopupDebugWindow, Asap3SaveDebugWindow
- Asap3GetLastError (implicit)

#### 3.2 Module Management (25 functions)
- Asap3AttachAsap2
- Asap3CreateModule, Asap3CreateModule2-4, Asap3CreateModuleSec
- Asap3GetModuleSecJobName
- Asap3GetModuleCount
- Asap3RestartMeasurementOnError, Asap3IsRestartMeasurementOnErrorEnabled
- Asap3IsModuleActive, Asap3ModuleActivation
- Asap3SwitchToMemoryPage, Asap3GetMemoryPage
- Asap3GetDBObjectUnit, Asap3GetDBObjectInfo
- Asap3GetDatabaseObjects, Asap3GetDatabaseObjectsByType
- Asap3GetAsap2, Asap3GetDatabaseInfo
- Asap3TransmitFile2ClientPc
- Asap3GetModuleName, Asap3GetModuleHandle
- Asap3ReleaseModule
- Asap3GetCommunicationType
- Asap3ECUOnOffline, Asap3IsECUOnline

#### 3.3 Calibration (12 functions)
- Asap3ReadByAddress, Asap3WriteByAddress
- Asap3ReadCalibrationObject, Asap3ReadCalibrationObject2, Asap3ReadCalibrationObjectEx
- Asap3WriteCalibrationObject, Asap3WriteCalibrationObjectEx
- Asap3TestObject
- Asap3CalibrationObjectInfo, Asap3CalibrationObjectInfoEx
- Asap3CalibrationObjectRecordInfo
- Asap3ReadObjectParameter

#### 3.4 Data Acquisition (35 functions)
- Asap3GetEcuTasks, Asap3GetEcuTasks2
- Asap3CreateLoggerConfiguration
- Asap3GetEcuDriverType
- Asap3HasResumeMode, Asap3SetResumeMode, Asap3IsResumeModeActive, Asap3ClearResumeMode
- Asap3GetChnlDefaultRaster
- Asap3SetupFifo
- Asap3SetupDataAcquisitionChnl, Asap3SetupDataAcquisitionChnl2
- Asap3GetMeasurementListEntries
- Asap3GetMeasurementState
- Asap3HasMCD3License
- Recorder functions (15): Define, GetType, GetName, GetCount, GetByIndex, GetByName, Select, GetSelected, Remove, GetMdfFileName, SetMdfFileName, SetDataReduction, GetDataReduction, GetState, Pause, Start, Stop, Enable, IsEnabled
- Asap3ResetDataAcquisitionChnlsByModule, Asap3ResetDataAcquisitionChnls
- Asap3TimeSync, Asap3IsTimeSyncEnabled
- Asap3StartDataAcquisition, Asap3ConnectDataAcquisition, Asap3StartResumedDataAcquisition
- Asap3StopDataAcquisition, Asap3DisconnectDataAcquisition
- Asap3GetFifoLevel, Asap3CheckOverrun
- Asap3GetNextSample, Asap3GetCurrentValues, Asap3GetNextSampleBlock
- Asap3UseNAN, Asap3IsNANUsed
- Asap3SetMdfFilename, Asap3GetMdfFilename
- Asap3SelectLabelList

#### 3.5 Converter (5 functions)
- Asap3MatlabConversion, Asap3MatlabConversionAsync
- Asap3MDFConverterCount
- Asap3MDFConvert
- Asap3MDFConverterInfo

#### 3.6 Network (8 functions)
- Asap3GetNetworkName
- Asap3GetNetworkDevices
- Asap3ActivateNetwork, Asap3IsNetworkActivated
- Asap3GetSecProfileCount
- Asap3GetSecProfileIdentifier
- Asap3GetSecProfileInfo
- Asap3AddSecProfileToNetwork

#### 3.7 Diagnostic (25 functions)
- Asap3DiagEnableTesterPresent, Asap3DiagIsTesterPresentEnabled
- Asap3DiagExecuteJob
- Asap3DiagCreateRawRequest, Asap3DiagCreateRawRequest2
- Asap3DiagCreateSymbolicRequest
- Asap3DiagSetNotificationParameters
- Asap3DiagExecute
- Asap3DiagGetServiceState
- Asap3DiagReleaseService
- Asap3DiagSetStringParameter, Asap3DiagSetRawParameter, Asap3DiagSetNumericParameter
- Asap3DiagGetResponseCount
- Asap3DiagIsPositiveResponse
- Asap3DiagGetResponseStream
- Asap3DiagGetStringResponseParameter, Asap3DiagGetRawResponseParameter, Asap3DiagGetNumericResponseParameter
- Asap3DiagIsComplexResponseParameter
- Asap3DiagGetComplexNumericResponseParameter, Asap3DiagGetComplexStringResponseParameter, Asap3DiagGetComplexRawResponseParameter
- Asap3DiagGetResponseCode
- Asap3DiagGetComplexIterationCount

#### 3.8 Scripting (8 functions)
- Asap3ExecuteScript
- Asap3ExecuteScriptEx
- Asap3GetScriptState
- Asap3StopScript
- Asap3StartScript
- Asap3GetScriptResultValue
- Asap3GetScriptResultString
- Asap3ReleaseScript

#### 3.9 Flash (8 functions)
- Asap3FlashSetODXContainer
- Asap3FlashGetSessionCount
- Asap3FlashGetSessionName
- Asap3FlashGetJobCount
- Asap3FlashGetJobName
- Asap3FlashStartFlashJob
- Asap3FlashGetJobState
- Asap3FlashStopJob

#### 3.10 Configuration (6 functions)
- Asap3LoadCNAFile
- Asap3GetCNAFilename
- Asap3GetCanapeModuleParam, Asap3SetCanapeModuleParam
- Asap3GetCanapeProjectParam, Asap3SetCanapeProjectParam

#### 3.11 Callbacks (4 functions)
- Asap3SetInteractiveMode, Asap3GetInteractiveMode
- Asap3RegisterCallBack
- Asap3UnRegisterCallBack

#### 3.12 Miscellaneous (9 functions)
- Asap3_CCP_Request
- Asap3SelectObjects
- Asap3RestoreWndSize, Asap3RestoreWndSize2
- Asap3CopyBinaryFile
- Asap3ConnectToCANape
- Asap3DisconnectFromCANape
- Asap3OpenDisplayForFile
- Asap3OpenDisplay
- Asap3ReleaseResultList

## 4. Implementation Standards

### 4.1 Code Quality Requirements
- **Type Hints**: All functions must have complete type hints (mypy strict mode)
- **Documentation**: NumPy-style docstrings for all public functions
- **Error Handling**: Custom exceptions for CANape errors
- **Testing**: Unit tests for all functions (aim for 80%+ coverage)

### 4.2 Naming Conventions
- **Functions**: Match C API names exactly (e.g., `Asap3Init`)
- **Pythonic wrappers**: Add Pythonic convenience methods (e.g., `init()`, `init5()`)
- **Classes**: PascalCase for classes, snake_case for functions
- **Private**: Prefix with `_` for internal functions

### 4.3 File Organization
- **Maximum file size**: ~500 lines per file
- **Logical grouping**: Functions grouped by functionality, not alphabetically
- **Import organization**: Standard library, third-party, local imports

## 5. Migration Strategy

### Phase 1: Foundation (Current)
- ✅ Create branch
- ✅ Develop plan
- ✅ Set up pyproject.toml
- ⏳ Fix existing bugs

### Phase 2: Core Infrastructure
- Refactor existing CANapAPI code into new structure
- Create core types, structs, enums modules
- Implement DLL loader with proper error handling
- Create custom exception hierarchy

### Phase 3: Initialization & Module Management
- Implement all initialization functions
- Implement module creation and management
- Add comprehensive tests

### Phase 4: Calibration & Data Acquisition
- Implement calibration functions
- Implement data acquisition functions
- Add recorder management

### Phase 5: Advanced Features
- Implement diagnostic functions
- Implement scripting functions
- Implement flash functions
- Implement network functions

### Phase 6: Polish & Documentation
- Complete all remaining functions
- Add comprehensive documentation
- Create examples
- Performance optimization if needed

## 6. Dependencies

### Required
- Python >= 3.8, < 3.12 (based on existing setup.py)
- ctypes (stdlib)
- typing (stdlib)
- cached-property (for lazy loading)

### Optional
- numpy (for data handling)
- pytest (for testing)
- mypy (for type checking)
- sphinx (for documentation)

## 7. Build System

### pyproject.toml
- Modern Python packaging standard
- PEP 517/518 compliant
- Supports editable installs
- Version management via versioneer

## 8. Testing Strategy

### Unit Tests
- Test each function with mock DLL calls
- Test error handling
- Test type conversions

### Integration Tests
- Test with actual CANape DLL (if available)
- Test end-to-end workflows

## 9. Documentation

### API Documentation
- Auto-generated from docstrings
- Examples for each major feature group
- Migration guide from old API

### User Documentation
- Installation instructions
- Quick start guide
- Common use cases

## 10. Success Criteria

- ✅ All 180 functions from CANapAPI.h implemented
- ✅ Full type hints throughout
- ✅ NumPy-style docstrings for all functions
- ✅ Comprehensive test coverage
- ✅ Modern project structure
- ✅ pyproject.toml setup
- ✅ No breaking changes to existing API (backward compatibility)
- ✅ All existing bugs fixed

## Timeline Estimate

- Phase 1: 1 day
- Phase 2: 2-3 days
- Phase 3: 3-4 days
- Phase 4: 4-5 days
- Phase 5: 3-4 days
- Phase 6: 2-3 days

**Total: ~15-20 days of focused development**

