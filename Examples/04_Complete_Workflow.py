"""Complete Workflow Example - Both Low-Level and High-Level Approaches.

This example demonstrates the same workflow using both:
1. Low-level direct DLL function calls
2. High-level Pythonic interface

This allows you to see the differences and choose the approach that fits your needs.
"""

from CANape import CANape
from CANape.core.types import TModulHdl


def workflow_low_level() -> None:
    """Complete workflow using low-level direct DLL calls."""
    print("\n" + "=" * 60)
    print("WORKFLOW 1: Low-Level Direct DLL Calls")
    print("=" * 60)

    canape = CANape()

    try:
        # 1. Initialize - direct DLL call
        print("\n[1] Initializing CANape...")
        result = canape.init.Asap3Init(
            response_timeout=10000,
            working_dir="./canape_tmp",
            fifo_size=8192,
            debug_mode=True,
        )
        if not result:
            error_code = canape.error.Asap3GetLastError()
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   ✗ Failed: {error_text} (code: {error_code})")
            return
        print("   ✓ Initialized")

        # 2. Create module - direct DLL call
        print("\n[2] Creating module...")
        module = canape.module.create.Asap3CreateModule(
            module_name="MyModule",
            database_filename="database.a2l",
            driver_type=1,
            channel_no=1,
        )
        print(f"   ✓ Module created: {module}")

        # 3. Add measurement channel - direct DLL call
        print("\n[3] Adding measurement channel...")
        result = canape.data_acquisition.setup.Asap3SetupDataAcquisitionChnl(
            module=module,
            measurement_object_name="EngineSpeed",
            format_type=0,
            task_id=0,
            polling_rate=1,
            save_to_file=False,
        )
        if not result:
            error_code = canape.error.Asap3GetLastError()
            print(f"   ✗ Failed: Error code {error_code}")
        else:
            print("   ✓ Channel added")

        # 4. Start data acquisition - direct DLL call
        print("\n[4] Starting data acquisition...")
        result = canape.data_acquisition.control.Asap3StartDataAcquisition()
        if not result:
            error_code = canape.error.Asap3GetLastError()
            error_text = canape.error.Asap3ErrorText(error_code)
            print(f"   ✗ Failed: {error_text} (code: {error_code})")
        else:
            print("   ✓ Acquisition started")

        # 5. Execute diagnostic job - direct DLL call
        print("\n[5] Executing diagnostic job...")
        response = canape.diagnostic.jobs.Asap3DiagExecuteJob(
            module=module,
            job="ReadDTCs",
            commandline=None,
        )
        if response:
            print(f"   ✓ Job executed: {response}")
        else:
            error_code = canape.error.Asap3GetLastError()
            print(f"   ✗ Failed: Error code {error_code}")

        # 6. Read calibration - direct DLL call
        print("\n[6] Reading calibration object...")
        try:
            value = canape.calibration.read_write.Asap3ReadCalibrationObject(
                module=module,
                object_name="MyCalibrationObject",
                format_type=0,
            )
            print(f"   ✓ Value read: {value}")
        except Exception as e:
            error_code = canape.error.Asap3GetLastError()
            print(f"   ✗ Failed: {e} (code: {error_code})")

        # 7. Cleanup - direct DLL calls
        print("\n[7] Cleaning up...")
        canape.data_acquisition.control.Asap3StopDataAcquisition()
        canape.init.Asap3Exit()
        print("   ✓ Cleanup complete")

    except Exception as e:
        print(f"\n   ✗ Exception: {e}")
        try:
            canape.init.Asap3Exit()
        except Exception:
            pass


def workflow_high_level() -> None:
    """Complete workflow using high-level Pythonic interface."""
    print("\n" + "=" * 60)
    print("WORKFLOW 2: High-Level Pythonic Interface")
    print("=" * 60)

    # Context manager handles cleanup automatically
    with CANape() as canape:
        try:
            # 1. Initialize - Pythonic method name
            print("\n[1] Starting CANape...")
            canape.start(
                response_timeout=10000,
                working_dir="./canape_tmp",
                fifo_size=8192,
                debug_mode=True,
            )
            print("   ✓ Started")

            # 2. Create module - Pythonic method name
            print("\n[2] Creating module...")
            module = canape.module.create(
                module_name="MyModule",
                database_filename="database.a2l",
                driver_type=1,
                channel_no=1,
            )
            print(f"   ✓ Module created: {module}")

            # 3. Add measurement channel - Pythonic method name
            print("\n[3] Adding measurement channel...")
            canape.data_acquisition.add_channel(
                module=module,
                measurement_object_name="EngineSpeed",
                format_type=0,
                task_id=0,
                polling_rate=1,
                save_to_file=False,
            )
            print("   ✓ Channel added")

            # 4. Start data acquisition - Pythonic method name
            print("\n[4] Starting data acquisition...")
            canape.data_acquisition.start()
            print("   ✓ Acquisition started")

            # 5. Execute diagnostic job - Pythonic method name
            print("\n[5] Executing diagnostic job...")
            response = canape.diagnostic.execute_job(
                module=module,
                job_name="ReadDTCs",
            )
            print(f"   ✓ Job executed: {response}")

            # 6. Read calibration - Pythonic method name
            print("\n[6] Reading calibration object...")
            value = canape.calibration.read(
                module=module,
                object_name="MyCalibrationObject",
                format_type=0,
            )
            print(f"   ✓ Value read: {value}")

            # 7. Cleanup - automatic via context manager
            print("\n[7] Stopping acquisition...")
            canape.data_acquisition.stop()
            print("   ✓ Stopped")
            # Context manager will call stop() automatically on exit

        except Exception as e:
            # All errors automatically decoded to Pythonic messages!
            print(f"\n   ✗ Error: {e}")
            # Error message format: "Failed to <operation>: <decoded_message> (Error Code: <code>)"


def main() -> None:
    """Run both workflow examples."""
    print("=" * 60)
    print("Complete Workflow Comparison")
    print("=" * 60)
    print("\nThis example shows the same workflow using both approaches:")
    print("  • Low-level: Direct DLL calls with manual error handling")
    print("  • High-level: Pythonic interface with automatic error decoding")

    # Run low-level workflow
    workflow_low_level()

    # Run high-level workflow
    workflow_high_level()

    print("\n" + "=" * 60)
    print("Comparison Summary")
    print("=" * 60)
    print("\nLow-Level Approach:")
    print("  ✓ Full control over every detail")
    print("  ✓ Direct access to all DLL functions")
    print("  ✗ Manual error code handling")
    print("  ✗ Manual error text retrieval")
    print("  ✗ More verbose code")
    print("\nHigh-Level Approach:")
    print("  ✓ Clean, Pythonic method names")
    print("  ✓ Automatic error decoding to readable messages")
    print("  ✓ Context manager for automatic cleanup")
    print("  ✓ Less code, easier to read")
    print("  ✗ Slightly less control (but low-level still accessible)")
    print("\nBoth approaches are available - choose what fits your needs!")


if __name__ == "__main__":
    main()

