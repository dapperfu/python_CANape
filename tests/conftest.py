import pytest
import uuid
import ctypes
import os

# Install CANape. Not included for copyright reasons.
header_file = r"C:\Program Files\Vector CANape 17\CANapeAPI\CANapAPI.h"
assert os.path.exists(header_file)
CANapAPI_dll= r"C:\Program Files\Vector CANape 17\CANapeAPI\CANapAPI64.dll"
assert os.path.exists(CANapAPI_dll)

# Figuring out Pytest fixtures, ignore.
@pytest.fixture(scope="session")
def uuid_session():
    """UUID with a session scope."""
    print("Session!")
    yield str(uuid.uuid4())

@pytest.fixture(scope="module")
def uuid_module():
    """UUID with a module scope."""
    print("Module!")
    yield str(uuid.uuid4())

@pytest.fixture(scope="function")
def uuid_function():
    """UUID with a function scope."""
    print("Function!")
    yield str(uuid.uuid4())

@pytest.fixture(scope="session")
def dll():
    dll = ctypes.windll.LoadLibrary(CANapAPI_dll)
    yield dll
        

