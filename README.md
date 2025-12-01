# Feb 2023 Update. 

If you want a working Python CANape tool check out [pycanape](https://github.com/zariiii9003/pycanape) by zariiii9003.

This project was a light proof of concept for my resume and to hopefully inspire others to show it's possible. It started as an unsupported side project at Eaton and Caterpillar. The bits on Github had to be re-created without a licensed version of CANape and therefore is very light.

# 2025 Update - High-Level Pythonic Interface

This project has been significantly enhanced with a comprehensive high-level Pythonic interface that wraps all common CANape ASAP3 functions. The new interface provides:

- **Clean Pythonic naming** - Removed "Asap3" prefix from all high-level methods
- **Automatic error decoding** - DLL error codes are converted to readable Pythonic error messages
- **Decorator-based patterns** - Common operations use Python decorators for validation, error handling, and retry logic
- **Dual access patterns** - Both high-level (Pythonic) and low-level (direct DLL) interfaces are available
- **Context manager support** - Automatic cleanup with `with` statements
- **Complete examples** - See `Examples/` directory for low-level, high-level, and side-by-side comparison examples

The high-level interface makes CANape automation much more accessible while still providing full access to the low-level DLL functions when needed.

# Da Liegt der Hund beraben

## Entwicklungsgeschichte

Unternehmen, die CANape (einschließlich Vector) verwenden, sind mit Open Source sehr konservativ.

Bei Caterpillar (ca. 2015-2016) wurde eine Alpha-Version entwickelt. Es war gut. Es automatisierte Stunden des dSpace HIL-Testens! Es befindet sich in der Firewall von Caterpillar.

Bei Eaton (ca. 2017) wurde eine Beta-Version entwickelt. Es war gut gut. Es befindet sich in der Firewall von Eaton.

Code hier wurde mit der Demo-Version von Vector entwickelt. Es hat Einschränkungen. Ich kann mir keine Vector-Hardware leisten.

## Zukunft

Python ist die Zukunft. ADAS5 benötigt viele Tests. Python ist gut in Tests. CANape braucht Python.

- Vector könnte dies entwickeln. Hören Sie auf Ingenieure, nicht auf Management. Niemand mag COM.
- Jemand spendet eine CANape-Lizenz für die Entwicklung.
- Jemand gabelt und setzt diese Arbeit fort.

## Die Auferstehung des Hundes (2025)

Der Hund wurde von den Toten auferweckt mit Vibe Coding, um weiter an diesem Projekt zu arbeiten. Die Arbeit an der hochwertigen Pythonic-Schnittstelle wurde abgeschlossen, aber wir warten noch auf eine CANape-Maschine zum Testen. Sobald wir Zugang zu einer CANape-Installation haben, werden wir die Implementierung vollständig validieren und testen.


# PyCANape


Pythonic CFFI wrapper for [CANape](https://vector.com/vi_canape_en.html). This is a full Pythonic wrapper using the [CANape ASAM-MCD3 Interface (CANapeAPI)](http://vector.com/portal/medien/cmc/application_notes/AN-AMC-1-103_CANape_ASAM_MCD3_Interface.pdf). It has an identical feature set to the [CANape® and MATLAB® interface.](http://vector.com/portal/medien/cmc/application_notes/AN-IMC-1-004_Interface_Programming_between_CANape_and_MATLAB.pdf)

# Examples

## High-Level Pythonic Interface (Recommended)

The new high-level interface provides clean, Pythonic method names with automatic error handling:

    from CANape import CANape

    # Use context manager for automatic cleanup
    with CANape() as canape:
        # Start CANape (clean method name, no "Asap3" prefix)
        canape.start(
            response_timeout=10000,
            working_dir="./canape_tmp",
            fifo_size=8192,
            debug_mode=True
        )
        
        # Create module (Pythonic interface)
        module = canape.module.create(
            module_name="MyModule",
            database_filename="database.a2l",
            driver_type=1,  # ASAP3_DRIVER_CCP
            channel_no=1
        )
        
        # Add measurement channel
        canape.data_acquisition.add_channel(
            module=module,
            measurement_object_name="EngineSpeed"
        )
        
        # Start data acquisition
        canape.data_acquisition.start()
        
        # Read calibration object
        value = canape.calibration.read(
            module=module,
            object_name="MyCalibrationObject"
        )
        
        # Execute diagnostic job
        response = canape.diagnostic.execute_job(
            module=module,
            job_name="ReadDTCs"
        )
        
        # Stop acquisition
        canape.data_acquisition.stop()
        # Context manager automatically calls stop() on exit

## Low-Level Direct DLL Access

For full control, you can still access the low-level DLL functions directly:

    from CANape import CANape

    canape = CANape()
    
    # Direct DLL function calls
    canape.init.Asap3Init(
        response_timeout=10000,
        working_dir="./canape_tmp",
        fifo_size=8192,
        debug_mode=True
    )
    
    # Direct module creation
    module = canape.module.create.Asap3CreateModule(
        module_name="MyModule",
        database_filename="database.a2l",
        driver_type=1,
        channel_no=1
    )
    
    # Manual error handling
    if not canape.data_acquisition.control.Asap3StartDataAcquisition():
        error_code = canape.error.Asap3GetLastError()
        error_text = canape.error.Asap3ErrorText(error_code)
        print(f"Error: {error_text} (code: {error_code})")
    
    canape.init.Asap3Exit()

See the `Examples/` directory for complete working examples:
- `02_Low_Level_API.py` - Direct DLL function calls
- `03_High_Level_API.py` - Pythonic interface
- `04_Complete_Workflow.py` - Side-by-side comparison


# Why?
Exposes all of CANape's features to the Python ecosystem.

- Use [Jenkins'](https://jenkins.io) Python integration to do continuous integration of flash file builds and unit tests.
- Embed CANape testing in [Jupyter Notebooks](http://jupyter.org) for [interactive exploratory data analysis](https://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/) or generating PDF Reports.
- Integrate CANape data with Deep Neural Nets such as [Tensorflow](https://www.tensorflow.org), [Keras](https://keras.io), and [Theano](http://deeplearning.net/software/theano/).
- Use the [Python Data Analysis Library ``pandas``](http://pandas.pydata.org) to create [beautiful data visualizations](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/) of CANape data.


### Motivation

- Me: "So are you guys going to ever release a Python interface?"
- Vector Sales Rep: "Everyone *loves* our COM interface? Is the COM interface not good enough? Why would anyone want to use Python when there is a COM interface? I can give you the e-mail address of an engineer if you need help with our COM interface."
- Me:
  ![Shocked Pikachu](shocked.png)
