"""Diagnostic Request Functions.

This module provides functions for creating and executing diagnostic requests.
"""

import ctypes
from typing import Any, Callable, Optional

from ..core.enums import eServiceStates
from ..core.exceptions import CANapeDiagnosticError
from ..core.handle import Handle
from ..core.structs import DiagNotificationStruct
from ..core.types import BYTE, DWORD, TAsap3DiagHdl, TModulHdl


class DiagnosticRequests:
    """Diagnostic Requests interface.

    This class provides methods for creating and executing diagnostic requests.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize diagnostic requests interface.

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
        # Request creation
        if hasattr(self.dll, "Asap3DiagCreateRawRequest"):
            self.dll.Asap3DiagCreateRawRequest.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(BYTE),
                ctypes.c_uint,
                ctypes.POINTER(TAsap3DiagHdl),
            )
            self.dll.Asap3DiagCreateRawRequest.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagCreateRawRequest2"):
            self.dll.Asap3DiagCreateRawRequest2.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(BYTE),
                ctypes.c_uint,
                ctypes.POINTER(TAsap3DiagHdl),
            )
            self.dll.Asap3DiagCreateRawRequest2.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagCreateSymbolicRequest"):
            self.dll.Asap3DiagCreateSymbolicRequest.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(TAsap3DiagHdl),
            )
            self.dll.Asap3DiagCreateSymbolicRequest.restype = (
                ctypes.c_bool
            )

        # Notification
        if hasattr(self.dll, "Asap3DiagSetNotificationParameters"):
            # Note: Callback function type is complex - using c_void_p for now
            self.dll.Asap3DiagSetNotificationParameters.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_void_p,  # Callback function
                ctypes.c_void_p,  # Private data
            )
            self.dll.Asap3DiagSetNotificationParameters.restype = (
                ctypes.c_bool
            )

        # Execution
        if hasattr(self.dll, "Asap3DiagExecute"):
            self.dll.Asap3DiagExecute.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_int,  # BOOL
            )
            self.dll.Asap3DiagExecute.restype = ctypes.c_bool

        # State and release
        if hasattr(self.dll, "Asap3DiagGetServiceState"):
            self.dll.Asap3DiagGetServiceState.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3DiagGetServiceState.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagReleaseService"):
            self.dll.Asap3DiagReleaseService.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
            )
            self.dll.Asap3DiagReleaseService.restype = ctypes.c_bool

    def Asap3DiagCreateRawRequest(
        self, module: TModulHdl, service_bytes: bytes
    ) -> TAsap3DiagHdl:
        """Create a raw diagnostic request (deprecated).

        Note: This function is deprecated. Use Asap3DiagCreateRawRequest2 instead.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        service_bytes : bytes
            Service bytes for the request.

        Returns
        -------
        TAsap3DiagHdl
            Diagnostic handle.

        Raises
        ------
        CANapeDiagnosticError
            If request creation fails.
        """
        if not hasattr(self.dll, "Asap3DiagCreateRawRequest"):
            raise CANapeDiagnosticError(
                "Asap3DiagCreateRawRequest not available in this DLL version"
            )

        length = len(service_bytes)
        bytes_array = (BYTE * length).from_buffer_copy(service_bytes)
        h_diag = TAsap3DiagHdl()

        result = self.dll.Asap3DiagCreateRawRequest(
            self.handle.handle,
            module,
            bytes_array,
            ctypes.c_uint(length),
            ctypes.byref(h_diag),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to create raw request (Error Code: {error_code})",
                error_code=error_code,
            )
        return h_diag

    def Asap3DiagCreateRawRequest2(
        self, module: TModulHdl, bytes_data: bytes
    ) -> TAsap3DiagHdl:
        """Create a raw diagnostic request (version 2).

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        bytes_data : bytes
            Bytes for the request.

        Returns
        -------
        TAsap3DiagHdl
            Diagnostic handle.

        Raises
        ------
        CANapeDiagnosticError
            If request creation fails.
        """
        if not hasattr(self.dll, "Asap3DiagCreateRawRequest2"):
            raise CANapeDiagnosticError(
                "Asap3DiagCreateRawRequest2 not available in this DLL version"
            )

        length = len(bytes_data)
        bytes_array = (BYTE * length).from_buffer_copy(bytes_data)
        h_diag = TAsap3DiagHdl()

        result = self.dll.Asap3DiagCreateRawRequest2(
            self.handle.handle,
            module,
            bytes_array,
            ctypes.c_uint(length),
            ctypes.byref(h_diag),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to create raw request (Error Code: {error_code})",
                error_code=error_code,
            )
        return h_diag

    def Asap3DiagCreateSymbolicRequest(
        self, module: TModulHdl, service_name: str
    ) -> TAsap3DiagHdl:
        """Create a symbolic diagnostic request.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        service_name : str
            Name of the service.

        Returns
        -------
        TAsap3DiagHdl
            Diagnostic handle.

        Raises
        ------
        CANapeDiagnosticError
            If request creation fails.
        """
        if not hasattr(self.dll, "Asap3DiagCreateSymbolicRequest"):
            raise CANapeDiagnosticError(
                "Asap3DiagCreateSymbolicRequest not available in this DLL version"
            )

        c_service_name = ctypes.c_char_p(service_name.encode("UTF-8"))
        h_diag = TAsap3DiagHdl()

        result = self.dll.Asap3DiagCreateSymbolicRequest(
            self.handle.handle,
            module,
            c_service_name,
            ctypes.byref(h_diag),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to create symbolic request (Error Code: {error_code})",
                error_code=error_code,
            )
        return h_diag

    def Asap3DiagSetNotificationParameters(
        self,
        h_diag: TAsap3DiagHdl,
        callback_function: Optional[Callable] = None,
        private_data: Optional[Any] = None,
    ) -> bool:
        """Set notification parameters for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        callback_function : Optional[Callable], optional
            Callback function to call on notification, by default None.
        private_data : Optional[Any], optional
            Private data to pass to callback, by default None.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If notification parameters cannot be set.
        """
        if not hasattr(self.dll, "Asap3DiagSetNotificationParameters"):
            raise CANapeDiagnosticError(
                "Asap3DiagSetNotificationParameters not available in this DLL version"
            )

        # Convert callback to ctypes function pointer if provided
        callback_ptr = None
        if callback_function:
            # Define callback type: void (*)(DiagNotificationStruct*)
            CALLBACK = ctypes.CFUNCTYPE(
                None, ctypes.POINTER(DiagNotificationStruct)
            )
            callback_ptr = CALLBACK(callback_function)

        private_ptr = ctypes.c_void_p()
        if private_data:
            private_ptr = ctypes.cast(
                id(private_data), ctypes.POINTER(ctypes.c_void_p)
            )

        result = self.dll.Asap3DiagSetNotificationParameters(
            self.handle.handle, h_diag, callback_ptr, private_ptr
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to set notification parameters (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagExecute(
        self, h_diag: TAsap3DiagHdl, suppress_positive_response: bool = False
    ) -> bool:
        """Execute a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        suppress_positive_response : bool, optional
            Suppress positive response, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If execution fails.
        """
        if not hasattr(self.dll, "Asap3DiagExecute"):
            raise CANapeDiagnosticError(
                "Asap3DiagExecute not available in this DLL version"
            )

        result = self.dll.Asap3DiagExecute(
            self.handle.handle,
            h_diag,
            ctypes.c_int(1 if suppress_positive_response else 0),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to execute diagnostic request (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagGetServiceState(
        self, h_diag: TAsap3DiagHdl
    ) -> int:
        """Get the service state of a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.

        Returns
        -------
        int
            Service state (see eServiceStates enum).

        Raises
        ------
        CANapeDiagnosticError
            If service state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetServiceState"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetServiceState not available in this DLL version"
            )

        state = ctypes.c_int()
        result = self.dll.Asap3DiagGetServiceState(
            self.handle.handle, h_diag, ctypes.byref(state)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get service state (Error Code: {error_code})",
                error_code=error_code,
            )
        return state.value

    def Asap3DiagReleaseService(
        self, h_diag: TAsap3DiagHdl
    ) -> bool:
        """Release a diagnostic service.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If service release fails.
        """
        if not hasattr(self.dll, "Asap3DiagReleaseService"):
            raise CANapeDiagnosticError(
                "Asap3DiagReleaseService not available in this DLL version"
            )

        result = self.dll.Asap3DiagReleaseService(
            self.handle.handle, h_diag
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to release service (Error Code: {error_code})",
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

