"""High-Level Diagnostic Interface.

This module provides a Pythonic, high-level interface for diagnostic operations,
wrapping the low-level ASAP3 diagnostic functions with clean naming.
"""

from typing import Any, Optional

from ..core.decorators import handle_errors, requires_initialization
from ..core.exceptions import CANapeDiagnosticError
from ..core.handle import Handle
from ..core.types import TModulHdl
from .jobs import DiagnosticJobs
from .requests import DiagnosticRequests
from .responses import DiagnosticResponses


class HighLevelDiagnosticInterface:
    """High-level diagnostic interface.

    Provides Pythonic methods for diagnostic operations with clean naming
    (removing "Asap3" prefix) and automatic error handling.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize high-level diagnostic interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        self._jobs = DiagnosticJobs(dll, handle)
        self._requests = DiagnosticRequests(dll, handle)
        self._responses = DiagnosticResponses(dll, handle)

    @requires_initialization
    @handle_errors("execute diagnostic job")
    def execute_job(
        self,
        module: TModulHdl,
        job_name: str,
        commandline: Optional[str] = None,
    ) -> Any:
        """Execute a diagnostic job.

        Pythonic wrapper around Asap3DiagExecuteJob.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        job_name : str
            Name of the diagnostic job to execute.
        commandline : Optional[str], optional
            Optional command line parameters, by default None.

        Returns
        -------
        Any
            Diagnostic job response handle.

        Raises
        ------
        CANapeDiagnosticError
            If job execution fails.

        Examples
        --------
        >>> response = canape.diagnostic.execute_job(module, "ReadDTCs")
        """
        return self._jobs.Asap3DiagExecuteJob(module, job_name, commandline)

    @requires_initialization
    @handle_errors("create diagnostic request")
    def create_request(
        self,
        module: TModulHdl,
        service: str,
        raw_bytes: Optional[bytes] = None,
    ) -> Any:
        """Create a diagnostic request.

        Pythonic wrapper around Asap3DiagCreateSymbolicRequest or
        Asap3DiagCreateRawRequest2.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        service : str
            Service name (for symbolic) or will be used as identifier.
        raw_bytes : Optional[bytes], optional
            If provided, creates a raw request with these bytes, by default None.

        Returns
        -------
        Any
            Diagnostic request handle.

        Raises
        ------
        CANapeDiagnosticError
            If request creation fails.

        Examples
        --------
        >>> # Symbolic request
        >>> request = canape.diagnostic.create_request(module, "ReadDataByIdentifier")
        >>> # Raw request
        >>> request = canape.diagnostic.create_request(
        ...     module, "RawService", raw_bytes=b"\\x22\\xF1\\x90"
        ... )
        """
        if raw_bytes is not None:
            return self._requests.Asap3DiagCreateRawRequest2(module, raw_bytes)
        else:
            return self._requests.Asap3DiagCreateSymbolicRequest(module, service)

    @requires_initialization
    @handle_errors("execute diagnostic request")
    def execute(
        self,
        request_handle: Any,
        suppress_positive_response: bool = False,
    ) -> bool:
        """Execute a diagnostic request.

        Pythonic wrapper around Asap3DiagExecute.

        Parameters
        ----------
        request_handle : Any
            Diagnostic request handle from create_request().
        suppress_positive_response : bool, optional
            If True, a positive response will not be sent by the ECU,
            by default False.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeDiagnosticError
            If request execution fails.

        Examples
        --------
        >>> request = canape.diagnostic.create_request(module, "ReadDataByIdentifier")
        >>> canape.diagnostic.execute(request)
        """
        return self._requests.Asap3DiagExecute(request_handle, suppress_positive_response)

    @requires_initialization
    @handle_errors("get diagnostic response")
    def get_response(
        self,
        request_handle: Any,
        response_id: int = 0,
    ) -> Any:
        """Get diagnostic response.

        Pythonic wrapper around diagnostic response functions.

        Parameters
        ----------
        request_handle : Any
            Diagnostic request handle.
        response_id : int, optional
            Response ID, by default 0.

        Returns
        -------
        Any
            Response data.

        Examples
        --------
        >>> response = canape.diagnostic.get_response(request_handle)
        """
        # This is a simplified interface - actual implementation would need
        # to handle different response types
        return self._responses

    @requires_initialization
    @handle_errors("enable tester present")
    def enable_tester_present(
        self,
        module: TModulHdl,
        enable: bool = True,
    ) -> bool:
        """Enable or disable tester present requests.

        Pythonic wrapper around Asap3DiagEnableTesterPresent.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        enable : bool, optional
            Enable tester present if True, by default True.

        Returns
        -------
        bool
            True if successful.

        Raises
        ------
        CANapeDiagnosticError
            If tester present cannot be configured.

        Examples
        --------
        >>> canape.diagnostic.enable_tester_present(module, enable=True)
        """
        return self._jobs.Asap3DiagEnableTesterPresent(module, enable)

    # Expose low-level interfaces for advanced usage
    @property
    def jobs(self) -> DiagnosticJobs:
        """Access to low-level job functions."""
        return self._jobs

    @property
    def requests(self) -> DiagnosticRequests:
        """Access to low-level request functions."""
        return self._requests

    @property
    def responses(self) -> DiagnosticResponses:
        """Access to low-level response functions."""
        return self._responses
