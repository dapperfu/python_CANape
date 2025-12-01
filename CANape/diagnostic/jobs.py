"""Diagnostic Job Functions.

This module provides functions for executing diagnostic jobs.
"""

import ctypes
from typing import Any, Optional

from ..core.exceptions import CANapeDiagnosticError
from ..core.handle import Handle
from ..core.structs import DiagJobResponse
from ..core.types import TModulHdl


class DiagnosticJobs:
    """Diagnostic Jobs interface.

    This class provides methods for executing diagnostic jobs.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize diagnostic jobs interface.

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
        if hasattr(self.dll, "Asap3DiagEnableTesterPresent"):
            self.dll.Asap3DiagEnableTesterPresent.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_bool,
            )
            self.dll.Asap3DiagEnableTesterPresent.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagIsTesterPresentEnabled"):
            self.dll.Asap3DiagIsTesterPresentEnabled.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3DiagIsTesterPresentEnabled.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagExecuteJob"):
            self.dll.Asap3DiagExecuteJob.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_bool,
                ctypes.POINTER(ctypes.POINTER(DiagJobResponse)),
            )
            self.dll.Asap3DiagExecuteJob.restype = ctypes.c_bool

    def Asap3DiagEnableTesterPresent(
        self, module: TModulHdl, enable: bool
    ) -> bool:
        """Enable or disable tester present.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        enable : bool
            Enable tester present if True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If tester present cannot be set.
        """
        if not hasattr(self.dll, "Asap3DiagEnableTesterPresent"):
            raise CANapeDiagnosticError(
                "Asap3DiagEnableTesterPresent not available in this DLL version"
            )

        result = self.dll.Asap3DiagEnableTesterPresent(
            self.handle.handle, module, ctypes.c_bool(enable)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to set tester present (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagIsTesterPresentEnabled(
        self, module: TModulHdl
    ) -> bool:
        """Check if tester present is enabled.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if tester present is enabled, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If tester present state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagIsTesterPresentEnabled"):
            raise CANapeDiagnosticError(
                "Asap3DiagIsTesterPresentEnabled not available in this DLL version"
            )

        enabled = ctypes.c_bool()
        result = self.dll.Asap3DiagIsTesterPresentEnabled(
            self.handle.handle, module, ctypes.byref(enabled)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to check tester present (Error Code: {error_code})",
                error_code=error_code,
            )
        return enabled.value

    def Asap3DiagExecuteJob(
        self,
        module: TModulHdl,
        job: str,
        commandline: str = "",
        reserved: bool = False,
    ) -> Optional[DiagJobResponse]:
        """Execute a diagnostic job.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        job : str
            Job name to execute.
        commandline : str, optional
            Command line parameters, by default "".
        reserved : bool, optional
            Reserved parameter, by default False.

        Returns
        -------
        Optional[DiagJobResponse]
            Job response structure, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If job execution fails.
        """
        if not hasattr(self.dll, "Asap3DiagExecuteJob"):
            raise CANapeDiagnosticError(
                "Asap3DiagExecuteJob not available in this DLL version"
            )

        c_job = ctypes.c_char_p(job.encode("UTF-8"))
        c_commandline = ctypes.c_char_p(commandline.encode("UTF-8"))
        job_response = ctypes.POINTER(DiagJobResponse)()

        result = self.dll.Asap3DiagExecuteJob(
            self.handle.handle,
            module,
            c_job,
            c_commandline,
            ctypes.c_bool(reserved),
            ctypes.byref(job_response),
        )
        if result and job_response:
            return job_response.contents
        return None

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

