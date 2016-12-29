# PyCANape
Python CFFI wrapper for CANape using CANapAPI/CANapAPI64.dll. This is a full Pythonic wrapper on the CANape ASAM-MCD3 Interface (CANapeAPI), based on the [CANape ASAM-MCD3 Interface](http://vector.com/portal/medien/cmc/application_notes/AN-AMC-1-103_CANape_ASAM_MCD3_Interface.pdf).

Compatible with:

- Python 2.7-3.6.
- x32 & 64-bit.
- Windows XP - 10.

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

    canape.atttach_asap(a2l=r"C:\Vector\Data\Experiment1\TopSecret.a2l",
                        channel = 2);
                     
To create a connection to a CAN device, the module can to be created like this: 

    canape.create_module (name = "CAN", 
                          database= r"C:\Vector\Data\Experiment1\TopSecret.dbc",,
                          driverType=CANape(CCP, 
                          channel = 1); 
    
To close the CANape connection, the exit() function is used: 

    canape.exit()

# Code

Where's the code? I can't show you. If you are interested in a Python interface for CANape, I've already done it once. http://www.linkedin.com/in/jed-frey.
