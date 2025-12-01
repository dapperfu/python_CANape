"""Database Functions.

This module provides functions for querying database information and objects.
"""

import ctypes
from typing import Any, List, Optional

from ..core.enums import TAsap3DBOType
from ..core.exceptions import CANapeModuleError
from ..core.handle import Handle
from ..core.structs import DBFileInfo, DBObjectInfo
from ..core.types import TModulHdl, UINT


class ModuleDatabase:
    """Module Database interface.

    This class provides methods for querying database information.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize module database interface.

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
        # Database object info
        if hasattr(self.dll, "Asap3GetDBObjectUnit"):
            self.dll.Asap3GetDBObjectUnit.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(UINT),
            )
            self.dll.Asap3GetDBObjectUnit.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetDBObjectInfo"):
            self.dll.Asap3GetDBObjectInfo.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.POINTER(DBObjectInfo),
            )
            self.dll.Asap3GetDBObjectInfo.restype = ctypes.c_bool

        # Database objects
        if hasattr(self.dll, "Asap3GetDatabaseObjects"):
            self.dll.Asap3GetDatabaseObjects.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(UINT),
                ctypes.c_int,
            )
            self.dll.Asap3GetDatabaseObjects.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetDatabaseObjectsByType"):
            self.dll.Asap3GetDatabaseObjectsByType.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(UINT),
                ctypes.c_int,
                ctypes.c_ulong,
            )
            self.dll.Asap3GetDatabaseObjectsByType.restype = ctypes.c_bool

        # ASAP2 and database info
        if hasattr(self.dll, "Asap3GetAsap2"):
            self.dll.Asap3GetAsap2.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char_p),
            )
            self.dll.Asap3GetAsap2.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetDatabaseInfo"):
            self.dll.Asap3GetDatabaseInfo.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(DBFileInfo),
            )
            self.dll.Asap3GetDatabaseInfo.restype = ctypes.c_bool

        # File transmission
        if hasattr(self.dll, "Asap3TransmitFile2ClientPc"):
            self.dll.Asap3TransmitFile2ClientPc.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3TransmitFile2ClientPc.restype = ctypes.c_bool

        # Security
        if hasattr(self.dll, "Asap3GetModuleSecJobName"):
            self.dll.Asap3GetModuleSecJobName.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3GetModuleSecJobName.restype = ctypes.c_bool

    def Asap3GetDBObjectUnit(
        self, module: TModulHdl, database_object_name: str
    ) -> Optional[str]:
        """Get the unit of a database object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        database_object_name : str
            Name of the requested database object.

        Returns
        -------
        Optional[str]
            Unit name, or None if failed.

        Raises
        ------
        CANapeModuleError
            If unit cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetDBObjectUnit"):
            raise CANapeModuleError(
                "Asap3GetDBObjectUnit not available in this DLL version"
            )

        # First call to get required buffer size
        size = UINT(0)
        c_object_name = ctypes.c_char_p(
            database_object_name.encode("UTF-8")
        )

        # Query size
        result = self.dll.Asap3GetDBObjectUnit(
            self.handle.handle,
            module,
            c_object_name,
            None,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get unit size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get unit
        buffer_size = size.value + 1
        unit_name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetDBObjectUnit(
            self.handle.handle,
            module,
            c_object_name,
            unit_name,
            ctypes.byref(size),
        )
        if result:
            return unit_name.value.decode("UTF-8")
        return None

    def Asap3GetDBObjectInfo(
        self, module: TModulHdl, object_name: str
    ) -> Optional[DBObjectInfo]:
        """Get information of a database object.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        object_name : str
            Name of the requested database object.

        Returns
        -------
        Optional[DBObjectInfo]
            Database object information structure, or None if failed.

        Raises
        ------
        CANapeModuleError
            If object info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetDBObjectInfo"):
            raise CANapeModuleError(
                "Asap3GetDBObjectInfo not available in this DLL version"
            )

        c_object_name = ctypes.c_char_p(object_name.encode("UTF-8"))
        info = DBObjectInfo()

        result = self.dll.Asap3GetDBObjectInfo(
            self.handle.handle, module, c_object_name, ctypes.byref(info)
        )
        if result:
            return info
        return None

    def Asap3GetDatabaseObjects(
        self, module: TModulHdl, db_type: int, max_size: int = 10000
    ) -> List[str]:
        """Get objects of the attached ASAP2 file.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        db_type : int
            Type of the DB object (see TAsap3DBOType enum).
        max_size : int, optional
            Maximum size of data objects array, by default 10000.

        Returns
        -------
        List[str]
            List of database object names.

        Raises
        ------
        CANapeModuleError
            If database objects cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetDatabaseObjects"):
            raise CANapeModuleError(
                "Asap3GetDatabaseObjects not available in this DLL version"
            )

        # Allocate buffer
        buffer = ctypes.create_string_buffer(max_size)
        size = UINT(max_size)

        result = self.dll.Asap3GetDatabaseObjects(
            self.handle.handle,
            module,
            buffer,
            ctypes.byref(size),
            db_type,
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get database objects (Error Code: {error_code})",
                error_code=error_code,
            )

        # Parse null-separated string list
        objects_str = buffer.value.decode("UTF-8")
        return [obj for obj in objects_str.split("\x00") if obj]

    def Asap3GetDatabaseObjectsByType(
        self,
        module: TModulHdl,
        db_type: int,
        type_filter: int,
        max_size: int = 10000,
    ) -> List[str]:
        """Get objects of the attached ASAP2 file with type filter.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        db_type : int
            Type of the DB object (see TAsap3DBOType enum).
        type_filter : int
            Type filter (map, curve, etc.) - see TDBE_VALUE_* constants.
        max_size : int, optional
            Maximum size of data objects array, by default 10000.

        Returns
        -------
        List[str]
            List of database object names matching the filter.

        Raises
        ------
        CANapeModuleError
            If database objects cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetDatabaseObjectsByType"):
            raise CANapeModuleError(
                "Asap3GetDatabaseObjectsByType not available in this DLL version"
            )

        # Allocate buffer
        buffer = ctypes.create_string_buffer(max_size)
        size = UINT(max_size)

        result = self.dll.Asap3GetDatabaseObjectsByType(
            self.handle.handle,
            module,
            buffer,
            ctypes.byref(size),
            db_type,
            ctypes.c_ulong(type_filter),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get database objects (Error Code: {error_code})",
                error_code=error_code,
            )

        # Parse null-separated string list
        objects_str = buffer.value.decode("UTF-8")
        return [obj for obj in objects_str.split("\x00") if obj]

    def Asap3GetAsap2(self, module: TModulHdl) -> Optional[str]:
        """Get name of attached ASAP2 file.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[str]
            ASAP2 file name, or None if failed.

        Raises
        ------
        CANapeModuleError
            If ASAP2 file name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetAsap2"):
            raise CANapeModuleError(
                "Asap3GetAsap2 not available in this DLL version"
            )

        asap2_fname = ctypes.POINTER(ctypes.c_char_p)()
        result = self.dll.Asap3GetAsap2(
            self.handle.handle, module, ctypes.byref(asap2_fname)
        )
        if result and asap2_fname:
            return asap2_fname.contents.value.decode("UTF-8")
        return None

    def Asap3GetDatabaseInfo(
        self, module: TModulHdl
    ) -> Optional[DBFileInfo]:
        """Get information concerning the database file.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[DBFileInfo]
            Database file information structure, or None if failed.

        Raises
        ------
        CANapeModuleError
            If database info cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetDatabaseInfo"):
            raise CANapeModuleError(
                "Asap3GetDatabaseInfo not available in this DLL version"
            )

        info = DBFileInfo()
        result = self.dll.Asap3GetDatabaseInfo(
            self.handle.handle, module, ctypes.byref(info)
        )
        if result:
            return info
        return None

    def Asap3TransmitFile2ClientPc(
        self, src_filename: str, dst_filename: str
    ) -> bool:
        """Transmit file to remote PC.

        Parameters
        ----------
        src_filename : str
            File name of the 'source file' saved at server PC.
        dst_filename : str
            File name of the 'destination file' on client PC.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeModuleError
            If file transmission fails.
        """
        if not hasattr(self.dll, "Asap3TransmitFile2ClientPc"):
            raise CANapeModuleError(
                "Asap3TransmitFile2ClientPc not available in this DLL version"
            )

        c_src_filename = ctypes.c_char_p(src_filename.encode("UTF-8"))
        c_dst_filename = ctypes.c_char_p(dst_filename.encode("UTF-8"))

        result = self.dll.Asap3TransmitFile2ClientPc(
            self.handle.handle, c_src_filename, c_dst_filename
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to transmit file (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetModuleSecJobName(
        self, module: TModulHdl
    ) -> Optional[str]:
        """Get the name of the security job (role) of a module.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        Optional[str]
            Security job name (role), or None if failed.

        Raises
        ------
        CANapeModuleError
            If security job name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetModuleSecJobName"):
            raise CANapeModuleError(
                "Asap3GetModuleSecJobName not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_ulong(0)

        # Query size
        result = self.dll.Asap3GetModuleSecJobName(
            self.handle.handle, module, None, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeModuleError(
                f"Failed to get job name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = size.value + 1
        job_name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetModuleSecJobName(
            self.handle.handle, module, job_name, ctypes.byref(size)
        )
        if result:
            return job_name.value.decode("UTF-8")
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

