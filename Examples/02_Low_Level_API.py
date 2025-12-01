"""Low-Level CANape API Example - Direct DLL Function Calls.

This example demonstrates direct usage of the CANape DLL functions with ctypes,
showing manual initialization, error handling, and type conversions.

This is the "raw" approach - you have full control but must handle all the
details yourself.
"""

import ctypes
from pathlib import Path

from CANape import CANape
from CANape.core.types import TModulHdl


def main() -> None:
    """Demonstrate low-level direct DLL access."""
    print("=" * 60)
    print("Low-Level CANape API Example - Direct DLL Function Calls")
    print("=" * 60)

    # Create CANape instance
    canape = CANape()

    # Low-level initialization - direct DLL call
    print("\n1. Initializing CANape (low-level)...")
    try:
        result = canape.init.Asap3Init(
            response_timeout=10000,
            working_dir="./canape_tmp",
            fifo_size=8192,
            debug_mode=True,
        )
        if not result:
            # Manual error handling - get error code
            error_code = canape.error.Asap3GetLastError()
            print(f"   Initialization failed with error code: {error_code}")
            # Manual error text retrieval
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   Error message: {error_text}")
            return
        print("   ✓ CANape initialized successfully")
    except Exception as e:
        print(f"   ✗ Exception during initialization: {e}")
        return

    # Low-level module creation - direct DLL call
    print("\n2. Creating module (low-level)...")
    try:
        # Direct call to Asap3CreateModule
        module = canape.module.create.Asap3CreateModule(
            module_name="MyModule",
            database_filename="database.a2l",  # This would be a real file path
            driver_type=1,  # ASAP3_DRIVER_CCP
            channel_no=1,
        )
        print(f"   ✓ Module created with handle: {module}")
    except Exception as e:
        print(f"   ✗ Module creation failed: {e}")
        # Manual error code retrieval
        error_code = canape.error.Asap3GetLastError()
        print(f"   Error code: {error_code}")

    # Low-level data acquisition setup - direct DLL call
    print("\n3. Setting up data acquisition channel (low-level)...")
    try:
        result = canape.data_acquisition.setup.Asap3SetupDataAcquisitionChnl(
            module=module,
            measurement_object_name="EngineSpeed",
            format_type=0,  # ECU_INTERNAL
            task_id=0,
            polling_rate=1,
            save_to_file=False,
        )
        if not result:
            error_code = canape.error.Asap3GetLastError()
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   ✗ Channel setup failed: {error_text} (code: {error_code})")
        else:
            print("   ✓ Channel setup successful")
    except Exception as e:
        print(f"   ✗ Exception: {e}")

    # Low-level data acquisition start - direct DLL call
    print("\n4. Starting data acquisition (low-level)...")
    try:
        result = canape.data_acquisition.control.Asap3StartDataAcquisition()
        if not result:
            error_code = canape.error.Asap3GetLastError()
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   ✗ Start failed: {error_text} (code: {error_code})")
        else:
            print("   ✓ Data acquisition started")
    except Exception as e:
        print(f"   ✗ Exception: {e}")

    # Low-level diagnostic job execution - direct DLL call
    print("\n5. Executing diagnostic job (low-level)...")
    try:
        response = canape.diagnostic.jobs.Asap3DiagExecuteJob(
            module=module,
            job="ReadDTCs",
            commandline=None,
        )
        if response:
            print(f"   ✓ Diagnostic job executed, response handle: {response}")
        else:
            error_code = canape.error.Asap3GetLastError()
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   ✗ Job execution failed: {error_text} (code: {error_code})")
    except Exception as e:
        print(f"   ✗ Exception: {e}")

    # Low-level calibration read - direct DLL call
    print("\n6. Reading calibration object (low-level)...")
    try:
        value = canape.calibration.read_write.Asap3ReadCalibrationObject(
            module=module,
            object_name="MyCalibrationObject",
            format_type=0,
        )
        print(f"   ✓ Calibration value read: {value}")
    except Exception as e:
        print(f"   ✗ Exception: {e}")
        error_code = canape.error.Asap3GetLastError()
        print(f"   Error code: {error_code}")

    # Low-level cleanup - direct DLL call
    print("\n7. Stopping and cleaning up (low-level)...")
    try:
        # Stop data acquisition first
        canape.data_acquisition.control.Asap3StopDataAcquisition()
        # Exit CANape
        result = canape.init.Asap3Exit()
        if result:
            print("   ✓ CANape exited successfully")
        else:
            error_code = canape.error.Asap3GetLastError()
            print(f"   ✗ Exit failed with error code: {error_code}")
    except Exception as e:
        print(f"   ✗ Exception during cleanup: {e}")

    print("\n" + "=" * 60)
    print("Low-level example completed")
    print("=" * 60)
    print("\nNote: This example shows manual error handling and direct DLL calls.")
    print("For easier usage, see the high-level example (03_High_Level_API.py)")


if __name__ == "__main__":
    main()

