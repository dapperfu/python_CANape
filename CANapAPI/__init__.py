"""1:1 mapping to CANapAPI64.dll. 'Low Level' python driver for Vector CANape."""


"""
Adapted from CANapAPI.h <Copyright (c) by Vector Informatik GmbH.  All rights reserved, where applicable>

The Python:

MIT License
-----------

Copyright (c) 2019 Jed Frey (https://github.com/jed-frey/)
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import ctypes
from .structs import version_t
from .types import TAsap3Hdl
from .defaults import CANapAPI_dll
from .utilities import assign_dll_types
from cached_property import cached_property
import os


class CANapAPI(object):
    def __init__(
        self, dll_path=CANapAPI_dll, *args, **kwargs
    ):
        # Set the dll path, to lazy load later.
        self.dll_path = dll_path

    @cached_property
    def dll(self):
        """Lazy load the dll."""
        dll = ctypes.windll.LoadLibrary(self.dll_path)
        dll = assign_dll_types(dll)
        return dll

    @cached_property
    def handle(self):
        return TAsap3Hdl()

    @property
    def handle_ref(self):
        return self.handle.byref

    def Asap3SetInteractiveMode(
        self, interactive_mode=False
    ):
        c_interactive_mode = ctypes.c_bool(interactive_mode)
        result = self.dll.Asap3SetInteractiveMode(
            self.handle, c_interactive_mode
        )

    def Asap3GetInteractiveMode(self):
        interactive_mode = ctypes.c_bool()
        result = self.dll.Asap3GetInteractiveMode(
            self.handle, ctypes.byref(interactive_mode)
        )
        if result:
            return interactive_mode
        else:
            return None

    def Asap3GetVersion(self):
        version = version_t()
        result = dll.Asap3GetVersion(ctypes.byref(version))
        if result:
            return version
        else:
            return None

    def Asap3Init5(
        self,
        responseTimeout: int = 10000,
        workingDir: str = os.path.abspath("canape_tmp"),
        fifoSize: int = 8192,
        sampleSize: int = 256,
        debugMode: bool = True,
        clearDeviceList: bool = True,
        bHexmode: bool = False,
        bModalMode: bool = False,
    ):
        """Asap3Init5 Function: Modality
        
        Parameters
        ----------
        responseTimeout : int (ms)
        workingDir: str
        fifoSize: int
        sampleSize: int
        debugMode : bool
        clearDeviceList : bool
        bHexmode : bool
        bModalMode : bool
        
        Returns
        -------
        bool
            Function call success
        """
        workingDir = os.path.abspath(workingDir)
        os.makedirs(workingDir, exist_ok=True)

        # Convert to ctypes.
        c_responseTimeout = ctypes.c_ulong()
        c_workingDir = ctypes.c_char_p(
            workingDir.encode("UTF-8")
        )
        c_fifoSize = ctypes.c_ulong(fifoSize)
        c_sampleSize = ctypes.c_ulong(sampleSize)
        c_debugMode = ctypes.c_bool(debugMode)
        c_clearDeviceList = ctypes.c_bool(clearDeviceList)
        c_bHexmode = ctypes.c_bool(bHexmode)
        c_bModalMode = ctypes.c_bool(bModalMode)

        result = self.dll.Asap3Init5(
            self.handle.byref,
            c_responseTimeout,
            c_workingDir,
            c_fifoSize,
            c_sampleSize,
            c_debugMode,
            c_clearDeviceList,
            c_bHexmode,
            c_bModalMode,
        )
        return result

    def Asap3Exit(self):
        return self.dll.Asap3Exit(self.handle)

    def Asap3Exit2(self, close_CANape: bool = True):
        c_close_CANape = ctypes.c_bool(close_CANape)
        return self.dll.Asap3Exit2(
            self.handle, c_close_CANape
        )

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
