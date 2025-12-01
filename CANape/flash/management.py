"""Flash Management Functions.

This module provides functions for managing flash operations.
"""

import ctypes
from typing import Any, List, Optional, Tuple

from ..core.exceptions import CANapeFlashError
from ..core.handle import Handle
from ..core.types import BOOL, DWORD, TModulHdl


class FlashManagement:
    """Flash Management interface.

    This class provides methods for managing flash operations.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize flash management interface.

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
        if hasattr(self.dll, "Asap3FlashSetODXContainer"):
            self.dll.Asap3FlashSetODXContainer.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
            )
            self.dll.Asap3FlashSetODXContainer.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashGetSessionCount"):
            self.dll.Asap3FlashGetSessionCount.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3FlashGetSessionCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashGetSessionName"):
            self.dll.Asap3FlashGetSessionName.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_long),
            )
            self.dll.Asap3FlashGetSessionName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashGetJobCount"):
            self.dll.Asap3FlashGetJobCount.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3FlashGetJobCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashGetJobName"):
            self.dll.Asap3FlashGetJobName.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_long),
            )
            self.dll.Asap3FlashGetJobName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashStartFlashJob"):
            self.dll.Asap3FlashStartFlashJob.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.c_char_p,
                ctypes.c_char_p,
                ctypes.c_char_p,
            )
            self.dll.Asap3FlashStartFlashJob.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashGetJobState"):
            self.dll.Asap3FlashGetJobState.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(BOOL),
                ctypes.POINTER(ctypes.c_long),
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3FlashGetJobState.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3FlashStopJob"):
            self.dll.Asap3FlashStopJob.argtypes = (
                ctypes.c_void_p,
                TModulHdl,
            )
            self.dll.Asap3FlashStopJob.restype = ctypes.c_bool

    def Asap3FlashSetODXContainer(
        self, module: TModulHdl, odx_container_file: str
    ) -> bool:
        """Set the ODX container file for flash operations.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        odx_container_file : str
            Filename of the ODX container.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeFlashError
            If ODX container cannot be set.
        """
        if not hasattr(self.dll, "Asap3FlashSetODXContainer"):
            raise CANapeFlashError(
                "Asap3FlashSetODXContainer not available in this DLL version"
            )

        c_file = ctypes.c_char_p(odx_container_file.encode("UTF-8"))
        result = self.dll.Asap3FlashSetODXContainer(
            self.handle.handle, module, c_file
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to set ODX container (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3FlashGetSessionCount(self, module: TModulHdl) -> int:
        """Get the count of defined flash sessions.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        int
            Session count.

        Raises
        ------
        CANapeFlashError
            If session count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3FlashGetSessionCount"):
            raise CANapeFlashError(
                "Asap3FlashGetSessionCount not available in this DLL version"
            )

        count = ctypes.c_ulong()
        result = self.dll.Asap3FlashGetSessionCount(
            self.handle.handle, module, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to get session count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3FlashGetSessionName(
        self, module: TModulHdl, index: int, max_size: int = 256
    ) -> Optional[str]:
        """Get the name of a flash session by index.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        index : int
            Session index.
        max_size : int, optional
            Maximum size of name buffer, by default 256.

        Returns
        -------
        Optional[str]
            Session name, or None if failed.

        Raises
        ------
        CANapeFlashError
            If session name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3FlashGetSessionName"):
            raise CANapeFlashError(
                "Asap3FlashGetSessionName not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_long(0)
        name = None

        # Query size
        result = self.dll.Asap3FlashGetSessionName(
            self.handle.handle,
            module,
            ctypes.c_ulong(index),
            name,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to get session name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = min(size.value + 1, max_size)
        name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3FlashGetSessionName(
            self.handle.handle,
            module,
            ctypes.c_ulong(index),
            name,
            ctypes.byref(size),
        )
        if result:
            return name.value.decode("UTF-8")
        return None

    def Asap3FlashGetJobCount(self, module: TModulHdl) -> int:
        """Get the count of defined flash jobs.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        int
            Job count.

        Raises
        ------
        CANapeFlashError
            If job count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3FlashGetJobCount"):
            raise CANapeFlashError(
                "Asap3FlashGetJobCount not available in this DLL version"
            )

        count = ctypes.c_ulong()
        result = self.dll.Asap3FlashGetJobCount(
            self.handle.handle, module, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to get job count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3FlashGetJobName(
        self, module: TModulHdl, index: int, max_size: int = 256
    ) -> Optional[str]:
        """Get the name of a flash job by index.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        index : int
            Job index.
        max_size : int, optional
            Maximum size of name buffer, by default 256.

        Returns
        -------
        Optional[str]
            Job name, or None if failed.

        Raises
        ------
        CANapeFlashError
            If job name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3FlashGetJobName"):
            raise CANapeFlashError(
                "Asap3FlashGetJobName not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_long(0)
        name = None

        # Query size
        result = self.dll.Asap3FlashGetJobName(
            self.handle.handle,
            module,
            ctypes.c_ulong(index),
            name,
            ctypes.byref(size),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to get job name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = min(size.value + 1, max_size)
        name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3FlashGetJobName(
            self.handle.handle,
            module,
            ctypes.c_ulong(index),
            name,
            ctypes.byref(size),
        )
        if result:
            return name.value.decode("UTF-8")
        return None

    def Asap3FlashStartFlashJob(
        self,
        module: TModulHdl,
        session_name: str,
        job_name: str,
        config_file_name: Optional[str] = None,
    ) -> bool:
        """Start a flash procedure.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        session_name : str
            Name of the flash session.
        job_name : str
            Name of the job or a flash script.
        config_file_name : Optional[str], optional
            Name of a configuration file. If None, the configuration file
            is ignored, by default None.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeFlashError
            If flash job cannot be started.
        """
        if not hasattr(self.dll, "Asap3FlashStartFlashJob"):
            raise CANapeFlashError(
                "Asap3FlashStartFlashJob not available in this DLL version"
            )

        c_session = ctypes.c_char_p(session_name.encode("UTF-8"))
        c_job = ctypes.c_char_p(job_name.encode("UTF-8"))
        c_config = None
        if config_file_name:
            c_config = ctypes.c_char_p(config_file_name.encode("UTF-8"))

        result = self.dll.Asap3FlashStartFlashJob(
            self.handle.handle, module, c_session, c_job, c_config
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to start flash job (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3FlashGetJobState(
        self, module: TModulHdl, max_info_size: int = 256
    ) -> Optional[Tuple[float, bool, int, str]]:
        """Get the current state of a flash job.

        Parameters
        ----------
        module : TModulHdl
            Module handle.
        max_info_size : int, optional
            Maximum size of info buffer, by default 256.

        Returns
        -------
        Optional[Tuple[float, bool, int, str]]
            Tuple of (script_result, is_running, progress, info), or None
            if failed.

        Raises
        ------
        CANapeFlashError
            If job state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3FlashGetJobState"):
            raise CANapeFlashError(
                "Asap3FlashGetJobState not available in this DLL version"
            )

        script_result = ctypes.c_double()
        is_running = BOOL()
        progress = ctypes.c_long()
        info = ctypes.create_string_buffer(max_info_size)
        size = ctypes.c_ulong(max_info_size)

        result = self.dll.Asap3FlashGetJobState(
            self.handle.handle,
            module,
            ctypes.byref(script_result),
            ctypes.byref(is_running),
            ctypes.byref(progress),
            info,
            ctypes.byref(size),
        )
        if result:
            return (
                script_result.value,
                bool(is_running.value),
                progress.value,
                info.value.decode("UTF-8"),
            )
        return None

    def Asap3FlashStopJob(self, module: TModulHdl) -> bool:
        """Stop a flash job.

        Parameters
        ----------
        module : TModulHdl
            Module handle.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeFlashError
            If flash job cannot be stopped.
        """
        if not hasattr(self.dll, "Asap3FlashStopJob"):
            raise CANapeFlashError(
                "Asap3FlashStopJob not available in this DLL version"
            )

        result = self.dll.Asap3FlashStopJob(self.handle.handle, module)
        if not result:
            error_code = self._get_last_error()
            raise CANapeFlashError(
                f"Failed to stop flash job (Error Code: {error_code})",
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

