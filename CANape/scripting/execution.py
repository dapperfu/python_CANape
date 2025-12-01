"""Scripting Execution Functions.

This module provides functions for executing and managing CANape scripts.
"""

import ctypes
from typing import Any, Optional, Tuple

from ..core.enums import TScriptStatus
from ..core.exceptions import CANapeScriptingError
from ..core.handle import Handle
from ..core.types import DWORD, TModulHdl, TScriptHdl


class ScriptExecution:
    """Script Execution interface.

    This class provides methods for executing and managing scripts.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize script execution interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._assign_types()

    def _assign_types(self) -> None:
        """Assign DLL function types."""
        if hasattr(self.dll, "Asap3ExecuteScript"):
            self.dll.Asap3ExecuteScript.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3ExecuteScript.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ExecuteScriptEx"):
            self.dll.Asap3ExecuteScriptEx.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.POINTER(TScriptHdl),
            )
            self.dll.Asap3ExecuteScriptEx.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetScriptState"):
            self.dll.Asap3GetScriptState.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
                ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3GetScriptState.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3StopScript"):
            self.dll.Asap3StopScript.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
            )
            self.dll.Asap3StopScript.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3StartScript"):
            self.dll.Asap3StartScript.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
                ctypes.c_char_p,
                TModulHdl,
            )
            self.dll.Asap3StartScript.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetScriptResultValue"):
            self.dll.Asap3GetScriptResultValue.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
                ctypes.POINTER(ctypes.c_double),
            )
            self.dll.Asap3GetScriptResultValue.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetScriptResultString"):
            self.dll.Asap3GetScriptResultString.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3GetScriptResultString.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ReleaseScript"):
            self.dll.Asap3ReleaseScript.argtypes = (
                ctypes.c_void_p,
                TScriptHdl,
            )
            self.dll.Asap3ReleaseScript.restype = ctypes.c_bool

    def Asap3ExecuteScript(
        self, script_file: str, commandline: str = ""
    ) -> bool:
        """Execute a script file.

        Parameters
        ----------
        script_file : str
            Path to the script file.
        commandline : str, optional
            Command line parameters, by default "".

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeScriptingError
            If script execution fails.
        """
        if not hasattr(self.dll, "Asap3ExecuteScript"):
            raise CANapeScriptingError(
                "Asap3ExecuteScript not available in this DLL version"
            )

        c_script_file = ctypes.c_char_p(script_file.encode("UTF-8"))
        c_commandline = ctypes.c_char_p(commandline.encode("UTF-8"))

        result = self.dll.Asap3ExecuteScript(
            self.handle.handle, c_script_file, c_commandline
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to execute script (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3ExecuteScriptEx(
        self, script_file: str, commandline: str = ""
    ) -> TScriptHdl:
        """Execute a script file (extended version).

        Returns a script handle for further operations.

        Parameters
        ----------
        script_file : str
            Path to the script file.
        commandline : str, optional
            Command line parameters, by default "".

        Returns
        -------
        TScriptHdl
            Script handle.

        Raises
        ------
        CANapeScriptingError
            If script execution fails.
        """
        if not hasattr(self.dll, "Asap3ExecuteScriptEx"):
            raise CANapeScriptingError(
                "Asap3ExecuteScriptEx not available in this DLL version"
            )

        c_script_file = ctypes.c_char_p(script_file.encode("UTF-8"))
        c_commandline = ctypes.c_char_p(commandline.encode("UTF-8"))
        h_script = TScriptHdl()

        result = self.dll.Asap3ExecuteScriptEx(
            self.handle.handle,
            c_script_file,
            c_commandline,
            ctypes.byref(h_script),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to execute script (Error Code: {error_code})",
                error_code=error_code,
            )
        return h_script

    def Asap3GetScriptState(
        self, h_script: TScriptHdl, max_text_size: int = 256
    ) -> Optional[Tuple[int, str]]:
        """Get the state of a script.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.
        max_text_size : int, optional
            Maximum size of text buffer, by default 256.

        Returns
        -------
        Optional[Tuple[int, str]]
            Tuple of (status, text), or None if failed. Status is from
            TScriptStatus enum.

        Raises
        ------
        CANapeScriptingError
            If script state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetScriptState"):
            raise CANapeScriptingError(
                "Asap3GetScriptState not available in this DLL version"
            )

        status = ctypes.c_int()
        text_buffer = ctypes.create_string_buffer(max_text_size)
        size = DWORD(max_text_size)

        result = self.dll.Asap3GetScriptState(
            self.handle.handle,
            h_script,
            ctypes.byref(status),
            text_buffer,
            ctypes.byref(size),
        )
        if result:
            return (status.value, text_buffer.value.decode("UTF-8"))
        return None

    def Asap3StopScript(self, h_script: TScriptHdl) -> bool:
        """Stop a running script.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeScriptingError
            If script cannot be stopped.
        """
        if not hasattr(self.dll, "Asap3StopScript"):
            raise CANapeScriptingError(
                "Asap3StopScript not available in this DLL version"
            )

        result = self.dll.Asap3StopScript(self.handle.handle, h_script)
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to stop script (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3StartScript(
        self,
        h_script: TScriptHdl,
        commandline: Optional[str] = None,
        module: Optional[TModulHdl] = None,
    ) -> bool:
        """Start a script.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.
        commandline : Optional[str], optional
            Command line parameters, by default None.
        module : Optional[TModulHdl], optional
            Module handle, by default None.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeScriptingError
            If script cannot be started.
        """
        if not hasattr(self.dll, "Asap3StartScript"):
            raise CANapeScriptingError(
                "Asap3StartScript not available in this DLL version"
            )

        c_commandline = None
        if commandline:
            c_commandline = ctypes.c_char_p(commandline.encode("UTF-8"))

        # Use invalid module handle if not provided
        if module is None:
            from ..core.types import ASAP3_INVALID_MODULE_HDL

            module = ASAP3_INVALID_MODULE_HDL

        result = self.dll.Asap3StartScript(
            self.handle.handle, h_script, c_commandline, module
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to start script (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetScriptResultValue(
        self, h_script: TScriptHdl
    ) -> Optional[float]:
        """Get the result value of a script.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.

        Returns
        -------
        Optional[float]
            Script result value, or None if failed.

        Raises
        ------
        CANapeScriptingError
            If result value cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetScriptResultValue"):
            raise CANapeScriptingError(
                "Asap3GetScriptResultValue not available in this DLL version"
            )

        value = ctypes.c_double()
        result = self.dll.Asap3GetScriptResultValue(
            self.handle.handle, h_script, ctypes.byref(value)
        )
        if result:
            return value.value
        return None

    def Asap3GetScriptResultString(
        self, h_script: TScriptHdl, max_size: int = 256
    ) -> Optional[str]:
        """Get the result string of a script.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.
        max_size : int, optional
            Maximum size of result buffer, by default 256.

        Returns
        -------
        Optional[str]
            Script result string, or None if failed.

        Raises
        ------
        CANapeScriptingError
            If result string cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetScriptResultString"):
            raise CANapeScriptingError(
                "Asap3GetScriptResultString not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        result_string = None

        # Query size
        result = self.dll.Asap3GetScriptResultString(
            self.handle.handle, h_script, result_string, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to get result string size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get string
        buffer_size = min(size.value + 1, max_size)
        result_string = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetScriptResultString(
            self.handle.handle, h_script, result_string, ctypes.byref(size)
        )
        if result:
            return result_string.value.decode("UTF-8")
        return None

    def Asap3ReleaseScript(self, h_script: TScriptHdl) -> bool:
        """Release a script handle.

        Parameters
        ----------
        h_script : TScriptHdl
            Script handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeScriptingError
            If script cannot be released.
        """
        if not hasattr(self.dll, "Asap3ReleaseScript"):
            raise CANapeScriptingError(
                "Asap3ReleaseScript not available in this DLL version"
            )

        result = self.dll.Asap3ReleaseScript(
            self.handle.handle, h_script
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeScriptingError(
                f"Failed to release script (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def _get_last_error(self) -> int:
        """Get last error code from CANape.

        Returns
        -------
        int
            Error code.
        """
        if hasattr(self.dll, "Asap3GetLastError"):
            return self.dll.Asap3GetLastError(self.handle.handle)
        return 0

