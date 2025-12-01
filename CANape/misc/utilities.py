"""Miscellaneous Utility Functions.

This module provides various utility functions for CCP requests, object selection,
and window management.
"""

import ctypes
from typing import Any, Optional, Tuple

from ..core.enums import TAsap3DataType, TAsap3FileType, TFormat, TObjectType
from ..core.exceptions import CANapeError
from ..core.handle import Handle
from ..core.types import TModulHdl


class Utilities:
    """Utilities interface.

    This class provides various utility functions.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize utilities interface.

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
        if hasattr(self.dll, "Asap3_CCP_Request"):
            self.dll.Asap3_CCP_Request.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ubyte,
                ctypes.c_ubyte,
                ctypes.c_ubyte,
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.POINTER(ctypes.c_ubyte),
            )
            self.dll.Asap3_CCP_Request.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SelectObjects"):
            self.dll.Asap3SelectObjects.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_int,  # TObjectType
                ctypes.c_char_p,
            )
            self.dll.Asap3SelectObjects.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3RestoreWndSize"):
            self.dll.Asap3RestoreWndSize.argtypes = (ctypes.c_void_p,)
            self.dll.Asap3RestoreWndSize.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3RestoreWndSize2"):
            self.dll.Asap3RestoreWndSize2.argtypes = (
                ctypes.c_void_p,
                ctypes.c_long,
            )
            self.dll.Asap3RestoreWndSize2.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3CopyBinaryFile"):
            self.dll.Asap3CopyBinaryFile.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_int,  # TAsap3FileType
                ctypes.c_int,  # TAsap3FileType
                ctypes.c_char_p,
            )
            self.dll.Asap3CopyBinaryFile.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3ReadObjectParameter"):
            self.dll.Asap3ReadObjectParameter.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_int,  # TFormat
                ctypes.POINTER(ctypes.c_int),  # TAsap3DataType
                ctypes.POINTER(ctypes.c_ulong),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double),
            )
            self.dll.Asap3ReadObjectParameter.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SelectLabelList"):
            self.dll.Asap3SelectLabelList.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_bool,
                ctypes.c_int,
            )
            self.dll.Asap3SelectLabelList.restype = ctypes.c_bool

    def Asap3_CCP_Request(
        self,
        module: TModulHdl,
        command: int,
        cto: int,
        dto: int,
        data: Optional[bytes] = None,
    ) -> Optional[bytes]:
        """Execute a CCP request.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        command : int
            CCP command byte.
        cto : int
            CTO (Command Transfer Object) parameter.
        dto : int
            DTO (Data Transfer Object) parameter.
        data : Optional[bytes], optional
            Data bytes for the request, by default None.

        Returns
        -------
        Optional[bytes]
            Response data, or None if failed.

        Raises
        ------
        CANapeError
            If CCP request fails.
        """
        if not hasattr(self.dll, "Asap3_CCP_Request"):
            raise CANapeError(
                "Asap3_CCP_Request not available in this DLL version"
            )

        data_size = len(data) if data else 0
        data_array = None
        if data:
            data_array = (ctypes.c_ubyte * data_size).from_buffer_copy(data)

        response_size = ctypes.c_ubyte(256)
        response = (ctypes.c_ubyte * 256)()

        result = self.dll.Asap3_CCP_Request(
            self.handle.handle,
            module,
            ctypes.c_ubyte(command),
            ctypes.c_ubyte(cto),
            ctypes.c_ubyte(dto),
            data_array,
            response,
        )
        if result:
            return bytes(response[: response_size.value])
        return None

    def Asap3SelectObjects(
        self,
        module: TModulHdl,
        object_type: int,
        filename: str,
    ) -> bool:
        """Select measurement or calibration objects using database selection dialogs.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_type : int
            Object type selector (see TObjectType enum).
        filename : str
            Name of file where the selection will be stored.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If object selection fails.
        """
        if not hasattr(self.dll, "Asap3SelectObjects"):
            raise CANapeError(
                "Asap3SelectObjects not available in this DLL version"
            )

        c_filename = ctypes.c_char_p(filename.encode("UTF-8"))
        result = self.dll.Asap3SelectObjects(
            self.handle.handle, module, ctypes.c_int(object_type), c_filename
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to select objects (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3RestoreWndSize(self) -> bool:
        """Restore the CANape main window size.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If window restore fails.
        """
        if not hasattr(self.dll, "Asap3RestoreWndSize"):
            raise CANapeError(
                "Asap3RestoreWndSize not available in this DLL version"
            )

        result = self.dll.Asap3RestoreWndSize(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to restore window size (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3RestoreWndSize2(self, params: int) -> bool:
        """Restore the CANape main window size with parameters.

        Parameters
        ----------
        params : int
            Window parameters (e.g., SW_HIDE, SW_MINIMIZE, SW_MAXIMIZE,
            SW_SHOW, SW_RESTORE).

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If window restore fails.
        """
        if not hasattr(self.dll, "Asap3RestoreWndSize2"):
            raise CANapeError(
                "Asap3RestoreWndSize2 not available in this DLL version"
            )

        result = self.dll.Asap3RestoreWndSize2(
            self.handle.handle, ctypes.c_long(params)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to restore window size (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3CopyBinaryFile(
        self,
        module: TModulHdl,
        source_type: int,
        dest_type: int,
        filename: str,
    ) -> bool:
        """Copy binary file between different memory types.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        source_type : int
            Type of source (see TAsap3FileType enum).
        dest_type : int
            Type of destination (see TAsap3FileType enum).
        filename : str
            Filename, if either source or destination type is FILE.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If file copy fails.
        """
        if not hasattr(self.dll, "Asap3CopyBinaryFile"):
            raise CANapeError(
                "Asap3CopyBinaryFile not available in this DLL version"
            )

        c_filename = ctypes.c_char_p(filename.encode("UTF-8"))
        result = self.dll.Asap3CopyBinaryFile(
            self.handle.handle,
            module,
            ctypes.c_int(source_type),
            ctypes.c_int(dest_type),
            c_filename,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to copy binary file (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3ReadObjectParameter(
        self,
        module: TModulHdl,
        object_name: str,
        format_type: int = 0,
    ) -> Optional[Tuple[int, int, float, float, float]]:
        """Query information about an object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the object to query.
        format_type : int, optional
            Kind of representation of the data (see TFormat enum),
            by default 0.

        Returns
        -------
        Optional[Tuple[int, int, float, float, float]]
            Tuple of (type, address, min, max, increment), or None if failed.

        Raises
        ------
        CANapeError
            If object parameter cannot be read.
        """
        if not hasattr(self.dll, "Asap3ReadObjectParameter"):
            raise CANapeError(
                "Asap3ReadObjectParameter not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(object_name.encode("UTF-8"))
        obj_type = ctypes.c_int()
        address = ctypes.c_ulong()
        min_val = ctypes.c_double()
        max_val = ctypes.c_double()
        increment = ctypes.c_double()

        result = self.dll.Asap3ReadObjectParameter(
            self.handle.handle,
            module,
            c_object_name,
            ctypes.c_int(format_type),
            ctypes.byref(obj_type),
            ctypes.byref(address),
            ctypes.byref(min_val),
            ctypes.byref(max_val),
            ctypes.byref(increment),
        )
        if result:
            return (
                obj_type.value,
                address.value,
                min_val.value,
                max_val.value,
                increment.value,
            )
        return None

    def Asap3SelectLabelList(
        self,
        name: str,
        include_mea_mode: bool = False,
        mode: int = 1,
    ) -> bool:
        """Select a label list with stored measurement objects by name.

        Parameters
        ----------
        name : str
            Name of the label list.
        include_mea_mode : bool, optional
            Include measurement mode, by default False.
        mode : int, optional
            Mode parameter, by default 1.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeError
            If label list selection fails.
        """
        if not hasattr(self.dll, "Asap3SelectLabelList"):
            raise CANapeError(
                "Asap3SelectLabelList not available in this DLL version"
            )

        c_name = ctypes.c_char_p(name.encode("UTF-8"))
        result = self.dll.Asap3SelectLabelList(
            self.handle.handle,
            c_name,
            ctypes.c_bool(include_mea_mode),
            ctypes.c_int(mode),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeError(
                f"Failed to select label list (Error Code: {error_code})",
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

