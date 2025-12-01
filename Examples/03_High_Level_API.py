"""High-Level CANape API Example - Pythonic Interface.

This example demonstrates the high-level Pythonic interface with clean naming,
automatic error handling, and context manager usage.

This is the "easy" approach - the library handles all the details for you.
"""

from CANape import CANape
from CANape.core.types import TModulHdl


def main() -> None:
    """Demonstrate high-level Pythonic interface."""
    print("=" * 60)
    print("High-Level CANape API Example - Pythonic Interface")
    print("=" * 60)

    # High-level usage with context manager - automatic cleanup
    print("\nUsing context manager for automatic cleanup...")
    with CANape() as canape:
        # High-level initialization - clean method name (no "Asap3" prefix)
        print("\n1. Starting CANape (high-level)...")
        try:
            canape.start(
                response_timeout=10000,
                working_dir="./canape_tmp",
                fifo_size=8192,
                debug_mode=True,
            )
            print("   ✓ CANape started successfully")
        except Exception as e:
            # Automatic error decoding - Pythonic error messages!
            print(f"   ✗ Failed to start: {e}")
            return

        # High-level module creation - clean method name
        print("\n2. Creating module (high-level)...")
        try:
            module = canape.module.create(
                module_name="MyModule",
                database_filename="database.a2l",  # This would be a real file path
                driver_type=1,  # ASAP3_DRIVER_CCP
                channel_no=1,
            )
            print(f"   ✓ Module created: {module}")
        except Exception as e:
            # Automatic error decoding with context
            print(f"   ✗ Failed to create module: {e}")
            return

        # High-level data acquisition setup - clean method name
        print("\n3. Adding measurement channel (high-level)...")
        try:
            canape.data_acquisition.add_channel(
                module=module,
                measurement_object_name="EngineSpeed",
                format_type=0,  # ECU_INTERNAL
                task_id=0,
                polling_rate=1,
                save_to_file=False,
            )
            print("   ✓ Channel added successfully")
        except Exception as e:
            # Pythonic error message with operation context
            print(f"   ✗ Failed to add channel: {e}")

        # High-level data acquisition start - clean method name
        print("\n4. Starting data acquisition (high-level)...")
        try:
            canape.data_acquisition.start()
            print("   ✓ Data acquisition started")
        except Exception as e:
            # Error automatically decoded to: "Failed to start data acquisition: Data acquisition already running (Error Code: 24)"
            print(f"   ✗ Failed to start acquisition: {e}")

        # High-level diagnostic job execution - clean method name
        print("\n5. Executing diagnostic job (high-level)...")
        try:
            response = canape.diagnostic.execute_job(
                module=module,
                job_name="ReadDTCs",
            )
            print(f"   ✓ Diagnostic job executed: {response}")
        except Exception as e:
            # Automatic error decoding
            print(f"   ✗ Failed to execute diagnostic job: {e}")

        # High-level calibration read - clean method name
        print("\n6. Reading calibration object (high-level)...")
        try:
            value = canape.calibration.read(
                module=module,
                object_name="MyCalibrationObject",
                format_type=0,
            )
            print(f"   ✓ Calibration value: {value}")
        except Exception as e:
            # Automatic error decoding
            print(f"   ✗ Failed to read calibration: {e}")

        # High-level property access
        print("\n7. Accessing project directory (high-level)...")
        try:
            project_dir = canape.project_directory
            print(f"   ✓ Project directory: {project_dir}")
        except Exception as e:
            print(f"   ✗ Failed to get project directory: {e}")

        # High-level data acquisition stop - clean method name
        print("\n8. Stopping data acquisition (high-level)...")
        try:
            canape.data_acquisition.stop()
            print("   ✓ Data acquisition stopped")
        except Exception as e:
            print(f"   ✗ Failed to stop acquisition: {e}")

        # Context manager automatically calls stop() on exit
        print("\n9. Exiting (automatic via context manager)...")
        # No need to call stop() manually - context manager handles it!

    print("\n" + "=" * 60)
    print("High-level example completed")
    print("=" * 60)
    print("\nKey advantages of high-level interface:")
    print("  • Clean method names (no 'Asap3' prefix)")
    print("  • Automatic error decoding to Pythonic messages")
    print("  • Context manager for automatic cleanup")
    print("  • Type-safe operations")
    print("  • Easy to read and maintain")


if __name__ == "__main__":
    main()

