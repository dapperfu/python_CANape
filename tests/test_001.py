"""Figuring out Pytest fixtures, ignore."""
def test_000001_a(uuid_session, uuid_module, uuid_function):
    print("Session UUID: "+uuid_session)
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)

def test_000001_b(uuid_session, uuid_module, uuid_function):
    print("Session UUID: "+uuid_session)
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)

def test_000001_c(uuid_session, uuid_module, uuid_function):
    print(f"Session UUID: {uuid_session}")
    print("Module UUID: "+uuid_module)
    print("Function UUID: "+uuid_function)

import ctypes
def test_canape_version(dll):

    # TODO: move this to where it belongs.
    # Define version_t as a Python ctypes-structure.
    class version_t(ctypes.Structure):
        _fields_ = [
            ('dllMainVersion', ctypes.c_int),
            ('dllSubVersion', ctypes.c_int),
            ('dllRelease', ctypes.c_int),
            ('osVersion', ctypes.c_char * 50),
            ('osRelease', ctypes.c_int),
        ]
        
        def __eq__(self, other):
            if isinstance(other, type(self)):
                return str(other)==str(self)
            if isinstance(other, str):
                return str(other)==str(self)
            raise Exception(f"Unsupported class comparison {type(other)}")
        
        def __repr__(self):
            return f"API_VERSION<{self.dllMainVersion}.{self.dllSubVersion}.{self.dllRelease}>"

        def __str__(self):
            return "{}.{}.{}".format(self.dllMainVersion, self.dllSubVersion, self.dllRelease)
    ## Set the argument and return types.
    # Pass by reference.
    dll.Asap3GetVersion.argtypes = (ctypes.POINTER(version_t),)
    # Return a success bool.
    dll.Asap3GetVersion.restype = ctypes.c_bool
    
    #def get_version():
    version = version_t()
    result = dll.Asap3GetVersion(ctypes.byref(version))
    assert version==version
    assert version=="2.3.1"
    assert version.osRelease==0
    assert version.osVersion==b'Windows95/WindowsNT'

 