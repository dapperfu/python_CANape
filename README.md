# PyCANape
Pythonic CFFI wrapper for [CANape](https://vector.com/vi_canape_en.html). This is a full Pythonic wrapper on the CANape ASAM-MCD3 Interface (CANapeAPI), based on the [CANape ASAM-MCD3 Interface](http://vector.com/portal/medien/cmc/application_notes/AN-AMC-1-103_CANape_ASAM_MCD3_Interface.pdf). It has an identical feature set to the [CANape® and MATLAB® interface.](http://vector.com/portal/medien/cmc/application_notes/AN-IMC-1-004_Interface_Programming_between_CANape_and_MATLAB.pdf)

Compatible with:

- Python 2.7-3.6.
- x32 & 64-bit.
- CANape 6.1-15.
- Windows XP - 10.

# Why?

Python is easier to train other engineers to use compared to the C interface in CANapeDLL or the WIN32 COM interface. Exposes all of CANape's features to the Python ecosystem. Write CANape scripts in Python rather than C.

# Examples

    import CANape
    canape = CANape.CANape()
    
CANape can be initialized via the init(), init2(), init3(), init4(), or init5() functions.  Any one of these functions can be used to initialize CANape depending upon need. Each function requires a different set of parameters that need to be passed in. If init5 is being used, the function can be called like this: 

    canape.init5(timeout = 20000,
                 m_WorkingDir = r"C:\Vector\Data\Experiment1",
                 fifo_size = 1000, 
                 sample_size = 1,
                 debug = True,
                 clear_device_list)
                 
After initializing the ASAP3 connection, a new module/device has to be created and a database file has to be attached. If a connection is being made to a CCP device and an ASAP2 description file is available, the AttachAsap2() function is used. 

    canape.attach_asap(a2l=r"C:\Vector\Data\Experiment1\TopSecret.a2l",
                        channel = 2);
                     
To create a connection to a CAN device, the module can to be created like this: 

    canape.create_module (name = "CAN", 
                          database= r"C:\Vector\Data\Experiment1\TopSecret.dbc",,
                          driverType=CANape(CCP, 
                          channel = 1);
    
To use a MDF file in Python or Matlab. 

    canape.matlab_conversion(mdf = r"C:\Vector\Data\Experiment1\NDA_Data.mdf",
                             mat = r"C:\Vector\Data\Experiment1\NDA_Data.mat)
                            
To list all devices currently connected to CANape:

    devices = canape.get_devices()
    for device in devices:
        print(device)

Create a new module, add a measurement channel, record data, process it with numpy.

    import numpy as np
    canape.attach_asap(a2l=r"C:\Vector\Data\Experiment1\TopSecret.a2l",
                       channel = 2);
    canape.module[0].add_measurement(name='channel2',
                                     task_index =3,
                                     save=0)
    canape.start_measurement()
    while True:
        data = canape.get_fifo_data(0, 2)
        if np.magic(data):
            print("Eureka!")
            break
        

To close the CANape connection, the exit() function is used: 

    canape.exit()

# Code

Where's the code? I can't show you. If you are interested in a Python interface for CANape, I've already done it once. http://www.linkedin.com/in/jed-frey.
