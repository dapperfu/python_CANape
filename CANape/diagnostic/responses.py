"""Diagnostic Response Functions.

This module provides functions for retrieving diagnostic response parameters.
"""

import ctypes
from typing import Any, Optional, Tuple

from ..core.exceptions import CANapeDiagnosticError
from ..core.handle import Handle
from ..core.structs import DiagNumericParamater
from ..core.types import BYTE, DWORD, TAsap3DiagHdl


class DiagnosticResponses:
    """Diagnostic Responses interface.

    This class provides methods for retrieving diagnostic response parameters.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize diagnostic responses interface.

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
        # Parameter setting
        if hasattr(self.dll, "Asap3DiagSetStringParameter"):
            self.dll.Asap3DiagSetStringParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3DiagSetStringParameter.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagSetRawParameter"):
            self.dll.Asap3DiagSetRawParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.POINTER(BYTE),
                DWORD,
            )
            self.dll.Asap3DiagSetRawParameter.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagSetNumericParameter"):
            self.dll.Asap3DiagSetNumericParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.POINTER(DiagNumericParamater),
            )
            self.dll.Asap3DiagSetNumericParameter.restype = ctypes.c_bool

        # Response info
        if hasattr(self.dll, "Asap3DiagGetResponseCount"):
            self.dll.Asap3DiagGetResponseCount.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.POINTER(ctypes.c_uint),
            )
            self.dll.Asap3DiagGetResponseCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagIsPositiveResponse"):
            self.dll.Asap3DiagIsPositiveResponse.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_long,
                ctypes.POINTER(ctypes.c_int),  # BOOL
            )
            self.dll.Asap3DiagIsPositiveResponse.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagGetResponseStream"):
            self.dll.Asap3DiagGetResponseStream.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.POINTER(BYTE),
                ctypes.POINTER(DWORD),
                ctypes.c_long,
            )
            self.dll.Asap3DiagGetResponseStream.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3DiagGetResponseCode"):
            self.dll.Asap3DiagGetResponseCode.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_long,
                ctypes.POINTER(BYTE),
            )
            self.dll.Asap3DiagGetResponseCode.restype = ctypes.c_bool

        # Response parameters
        if hasattr(self.dll, "Asap3DiagGetStringResponseParameter"):
            self.dll.Asap3DiagGetStringResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3DiagGetStringResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetRawResponseParameter"):
            self.dll.Asap3DiagGetRawResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3DiagGetRawResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetNumericResponseParameter"):
            self.dll.Asap3DiagGetNumericResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.POINTER(DiagNumericParamater),
            )
            self.dll.Asap3DiagGetNumericResponseParameter.restype = (
                ctypes.c_bool
            )

        # Complex parameters
        if hasattr(self.dll, "Asap3DiagIsComplexResponseParameter"):
            self.dll.Asap3DiagIsComplexResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.POINTER(ctypes.c_int),  # BOOL
            )
            self.dll.Asap3DiagIsComplexResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetComplexNumericResponseParameter"):
            self.dll.Asap3DiagGetComplexNumericResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.c_char_p,
                ctypes.c_ulong,
                ctypes.POINTER(DiagNumericParamater),
            )
            self.dll.Asap3DiagGetComplexNumericResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetComplexStringResponseParameter"):
            self.dll.Asap3DiagGetComplexStringResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.c_char_p,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3DiagGetComplexStringResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetComplexRawResponseParameter"):
            self.dll.Asap3DiagGetComplexRawResponseParameter.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.c_char_p,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3DiagGetComplexRawResponseParameter.restype = (
                ctypes.c_bool
            )

        if hasattr(self.dll, "Asap3DiagGetComplexIterationCount"):
            self.dll.Asap3DiagGetComplexIterationCount.argtypes = (
                ctypes.c_void_p,
                TAsap3DiagHdl,
                ctypes.c_char_p,
                ctypes.c_long,
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3DiagGetComplexIterationCount.restype = (
                ctypes.c_bool
            )

    def Asap3DiagSetStringParameter(
        self, h_diag: TAsap3DiagHdl, parameter_name: str, parameter_value: str
    ) -> bool:
        """Set a string parameter for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        parameter_name : str
            Name of the parameter.
        parameter_value : str
            Value of the parameter.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be set.
        """
        if not hasattr(self.dll, "Asap3DiagSetStringParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagSetStringParameter not available in this DLL version"
            )

        c_param_name = ctypes.c_char_p(parameter_name.encode("UTF-8"))
        c_param_value = ctypes.c_char_p(parameter_value.encode("UTF-8"))

        result = self.dll.Asap3DiagSetStringParameter(
            self.handle.handle, h_diag, c_param_name, c_param_value
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to set string parameter (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagSetRawParameter(
        self,
        h_diag: TAsap3DiagHdl,
        parameter_name: str,
        parameter_value: bytes,
    ) -> bool:
        """Set a raw parameter for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        parameter_name : str
            Name of the parameter.
        parameter_value : bytes
            Raw value of the parameter.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be set.
        """
        if not hasattr(self.dll, "Asap3DiagSetRawParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagSetRawParameter not available in this DLL version"
            )

        c_param_name = ctypes.c_char_p(parameter_name.encode("UTF-8"))
        size = len(parameter_value)
        bytes_array = (BYTE * size).from_buffer_copy(parameter_value)

        result = self.dll.Asap3DiagSetRawParameter(
            self.handle.handle,
            h_diag,
            c_param_name,
            bytes_array,
            DWORD(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to set raw parameter (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagSetNumericParameter(
        self,
        h_diag: TAsap3DiagHdl,
        parameter_name: str,
        parameter: DiagNumericParamater,
    ) -> bool:
        """Set a numeric parameter for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        parameter_name : str
            Name of the parameter.
        parameter : DiagNumericParamater
            Numeric parameter structure.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be set.
        """
        if not hasattr(self.dll, "Asap3DiagSetNumericParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagSetNumericParameter not available in this DLL version"
            )

        c_param_name = ctypes.c_char_p(parameter_name.encode("UTF-8"))

        result = self.dll.Asap3DiagSetNumericParameter(
            self.handle.handle, h_diag, c_param_name, ctypes.byref(parameter)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to set numeric parameter (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3DiagGetResponseCount(
        self, h_diag: TAsap3DiagHdl
    ) -> int:
        """Get the count of responses for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.

        Returns
        -------
        int
            Count of responses.

        Raises
        ------
        CANapeDiagnosticError
            If response count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetResponseCount"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetResponseCount not available in this DLL version"
            )

        count = ctypes.c_uint()
        result = self.dll.Asap3DiagGetResponseCount(
            self.handle.handle, h_diag, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get response count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3DiagIsPositiveResponse(
        self, h_diag: TAsap3DiagHdl, response_id: int
    ) -> bool:
        """Check if a response is positive.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        response_id : int
            Response ID.

        Returns
        -------
        bool
            True if response is positive, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If response check fails.
        """
        if not hasattr(self.dll, "Asap3DiagIsPositiveResponse"):
            raise CANapeDiagnosticError(
                "Asap3DiagIsPositiveResponse not available in this DLL version"
            )

        is_positive = ctypes.c_int()
        result = self.dll.Asap3DiagIsPositiveResponse(
            self.handle.handle,
            h_diag,
            ctypes.c_long(response_id),
            ctypes.byref(is_positive),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to check positive response (Error Code: {error_code})",
                error_code=error_code,
            )
        return bool(is_positive.value)

    def Asap3DiagGetResponseStream(
        self, h_diag: TAsap3DiagHdl, response_id: int, max_size: int = 4096
    ) -> Optional[bytes]:
        """Get response stream for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        response_id : int
            Response ID.
        max_size : int, optional
            Maximum size of stream to retrieve, by default 4096.

        Returns
        -------
        Optional[bytes]
            Response stream data, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If response stream cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetResponseStream"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetResponseStream not available in this DLL version"
            )

        stream = (BYTE * max_size)()
        size = DWORD(max_size)

        result = self.dll.Asap3DiagGetResponseStream(
            self.handle.handle,
            h_diag,
            stream,
            ctypes.byref(size),
            ctypes.c_long(response_id),
        )
        if result:
            return bytes(stream[: size.value])
        return None

    def Asap3DiagGetResponseCode(
        self, h_diag: TAsap3DiagHdl, response_id: int
    ) -> int:
        """Get response code for a diagnostic request.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        response_id : int
            Response ID.

        Returns
        -------
        int
            Response code.

        Raises
        ------
        CANapeDiagnosticError
            If response code cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetResponseCode"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetResponseCode not available in this DLL version"
            )

        code = BYTE()
        result = self.dll.Asap3DiagGetResponseCode(
            self.handle.handle,
            h_diag,
            ctypes.c_long(response_id),
            ctypes.byref(code),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get response code (Error Code: {error_code})",
                error_code=error_code,
            )
        return code.value

    def Asap3DiagGetStringResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
        max_size: int = 256,
    ) -> Optional[str]:
        """Get a string response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.
        max_size : int, optional
            Maximum size of string buffer, by default 256.

        Returns
        -------
        Optional[str]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetStringResponseParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetStringResponseParameter not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        data = None

        # Query size
        result = self.dll.Asap3DiagGetStringResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            data,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get string parameter size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get data
        buffer_size = size.value + 1
        data = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3DiagGetStringResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            data,
            ctypes.byref(size),
        )
        if result:
            return data.value.decode("UTF-8")
        return None

    def Asap3DiagGetRawResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
        max_size: int = 4096,
    ) -> Optional[bytes]:
        """Get a raw response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.
        max_size : int, optional
            Maximum size of data buffer, by default 4096.

        Returns
        -------
        Optional[bytes]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetRawResponseParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetRawResponseParameter not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        data = None

        # Query size
        result = self.dll.Asap3DiagGetRawResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            data,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get raw parameter size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get data
        buffer_size = min(size.value + 1, max_size)
        data = (ctypes.c_ubyte * buffer_size)()
        result = self.dll.Asap3DiagGetRawResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            data,
            ctypes.byref(size),
        )
        if result:
            return bytes(data[: size.value])
        return None

    def Asap3DiagGetNumericResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
    ) -> Optional[DiagNumericParamater]:
        """Get a numeric response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.

        Returns
        -------
        Optional[DiagNumericParamater]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetNumericResponseParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetNumericResponseParameter not available in this DLL version"
            )

        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        parameter = DiagNumericParamater()

        result = self.dll.Asap3DiagGetNumericResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            ctypes.byref(parameter),
        )
        if result:
            return parameter
        return None

    def Asap3DiagIsComplexResponseParameter(
        self, h_diag: TAsap3DiagHdl, name: str, response_id: int
    ) -> bool:
        """Check if a response parameter is complex.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.

        Returns
        -------
        bool
            True if parameter is complex, False otherwise.

        Raises
        ------
        CANapeDiagnosticError
            If check fails.
        """
        if not hasattr(self.dll, "Asap3DiagIsComplexResponseParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagIsComplexResponseParameter not available in this DLL version"
            )

        is_complex = ctypes.c_int()
        c_name = ctypes.c_char_p(name.encode("UTF-8"))

        result = self.dll.Asap3DiagIsComplexResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            ctypes.byref(is_complex),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to check complex parameter (Error Code: {error_code})",
                error_code=error_code,
            )
        return bool(is_complex.value)

    def Asap3DiagGetComplexNumericResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
        sub_parameter: str,
        iteration_index: int,
    ) -> Optional[DiagNumericParamater]:
        """Get a complex numeric response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.
        sub_parameter : str
            Sub-parameter name.
        iteration_index : int
            Iteration index.

        Returns
        -------
        Optional[DiagNumericParamater]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(
            self.dll, "Asap3DiagGetComplexNumericResponseParameter"
        ):
            raise CANapeDiagnosticError(
                "Asap3DiagGetComplexNumericResponseParameter not available in this DLL version"
            )

        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        c_sub_param = ctypes.c_char_p(sub_parameter.encode("UTF-8"))
        parameter = DiagNumericParamater()

        result = self.dll.Asap3DiagGetComplexNumericResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            c_sub_param,
            ctypes.c_ulong(iteration_index),
            ctypes.byref(parameter),
        )
        if result:
            return parameter
        return None

    def Asap3DiagGetComplexStringResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
        sub_parameter: str,
        iteration_index: int,
        max_size: int = 256,
    ) -> Optional[str]:
        """Get a complex string response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.
        sub_parameter : str
            Sub-parameter name.
        iteration_index : int
            Iteration index.
        max_size : int, optional
            Maximum size of string buffer, by default 256.

        Returns
        -------
        Optional[str]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(
            self.dll, "Asap3DiagGetComplexStringResponseParameter"
        ):
            raise CANapeDiagnosticError(
                "Asap3DiagGetComplexStringResponseParameter not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        c_sub_param = ctypes.c_char_p(sub_parameter.encode("UTF-8"))
        data = None

        # Query size
        result = self.dll.Asap3DiagGetComplexStringResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            c_sub_param,
            ctypes.c_ulong(iteration_index),
            data,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get complex string parameter size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get data
        buffer_size = min(size.value + 1, max_size)
        data = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3DiagGetComplexStringResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            c_sub_param,
            ctypes.c_ulong(iteration_index),
            data,
            ctypes.byref(size),
        )
        if result:
            return data.value.decode("UTF-8")
        return None

    def Asap3DiagGetComplexRawResponseParameter(
        self,
        h_diag: TAsap3DiagHdl,
        name: str,
        response_id: int,
        sub_parameter: str,
        iteration_index: int,
        max_size: int = 4096,
    ) -> Optional[bytes]:
        """Get a complex raw response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        name : str
            Parameter name.
        response_id : int
            Response ID.
        sub_parameter : str
            Sub-parameter name.
        iteration_index : int
            Iteration index.
        max_size : int, optional
            Maximum size of data buffer, by default 4096.

        Returns
        -------
        Optional[bytes]
            Parameter value, or None if failed.

        Raises
        ------
        CANapeDiagnosticError
            If parameter cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetComplexRawResponseParameter"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetComplexRawResponseParameter not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        c_sub_param = ctypes.c_char_p(sub_parameter.encode("UTF-8"))
        data = None

        # Query size
        result = self.dll.Asap3DiagGetComplexRawResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            c_sub_param,
            ctypes.c_ulong(iteration_index),
            data,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get complex raw parameter size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get data
        buffer_size = min(size.value + 1, max_size)
        data = (ctypes.c_char * buffer_size)()
        result = self.dll.Asap3DiagGetComplexRawResponseParameter(
            self.handle.handle,
            h_diag,
            c_name,
            ctypes.c_long(response_id),
            c_sub_param,
            ctypes.c_ulong(iteration_index),
            data,
            ctypes.byref(size),
        )
        if result:
            return bytes(data[: size.value])
        return None

    def Asap3DiagGetComplexIterationCount(
        self, h_diag: TAsap3DiagHdl, parameter: str, response_id: int
    ) -> int:
        """Get the iteration count for a complex response parameter.

        Parameters
        ----------
        h_diag : TAsap3DiagHdl
            Diagnostic handle.
        parameter : str
            Parameter name.
        response_id : int
            Response ID.

        Returns
        -------
        int
            Iteration count.

        Raises
        ------
        CANapeDiagnosticError
            If iteration count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3DiagGetComplexIterationCount"):
            raise CANapeDiagnosticError(
                "Asap3DiagGetComplexIterationCount not available in this DLL version"
            )

        iteration = ctypes.c_ulong()
        c_param = ctypes.c_char_p(parameter.encode("UTF-8"))

        result = self.dll.Asap3DiagGetComplexIterationCount(
            self.handle.handle,
            h_diag,
            c_param,
            ctypes.c_long(response_id),
            ctypes.byref(iteration),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDiagnosticError(
                f"Failed to get iteration count (Error Code: {error_code})",
                error_code=error_code,
            )
        return iteration.value

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

