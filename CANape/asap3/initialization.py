"""ASAP3 Initialization Functions.

This module provides functions for initializing and shutting down the ASAP3
connection to CANape.
"""

import ctypes
import os
from typing import Any, Optional

from ..core.exceptions import CANapeInitializationError
from ..core.handle import Handle
from ..core.structs import TApplicationID
from ..core.type_assignments import (
    assign_exit_functions,
    assign_init_functions,
)


class ASAP3Initialization:
    """ASAP3 Initialization interface.

    This class provides methods for initializing and managing the ASAP3
    connection to CANape.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize ASAP3 initialization interface.

        Parameters
        ----------
        dll : Any
            The loaded DLL object.
        handle : Handle
            The CANape handle.
        """
        self.dll = dll
        self.handle = handle
        # Assign function types
        assign_init_functions(self.dll)
        assign_exit_functions(self.dll)

    def Asap3SetTCPOptions(self, ip_address: str, port_number: int) -> bool:
        """Configure ASAP3 TCP connection.

        This function must be called before any of the Asap3Init calls.
        It prepares the ASAP3 module for connection to the ASAP3 CANape server.
        This function is only available in the Ethernet version of CANapeAPI.

        Parameters
        ----------
        ip_address : str
            IP address in form (123.2.3.14) of the PC where CANape is running
            in ASAP3 TCP mode.
        port_number : int
            Port number of the CANape ASAP3 TCP Server.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If TCP options cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetTCPOptions"):
            raise CANapeInitializationError("Asap3SetTCPOptions not available in this DLL version")

        c_ip_address = ctypes.c_char_p(ip_address.encode("UTF-8"))
        c_port_number = ctypes.c_ulong(port_number)

        result = self.dll.Asap3SetTCPOptions(c_ip_address, c_port_number)
        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to set TCP options (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        debug_mode: bool = True,
    ) -> bool:
        """Initialize ASAP3 connection (basic version).

        Returns a handle to be used in subsequent function calls.
        CANape will be started if not already running.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory. By default the project file CANape.INI
            is saved at the working directory. To load a different project file,
            append the project file name to 'working_dir', by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition (number of FIFO entries
            which can be read out using Asap3GetNextSample()). Each FIFO entry
            includes at most ACQ_MAX_VALUES=128 measurement values, by default 8192.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size instead of 'minimized'.
            If False, call CANape in 'minimized' mode, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        working_dir = os.path.abspath(working_dir)
        os.makedirs(working_dir, exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_working_dir = ctypes.c_char_p(working_dir.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_debug_mode = ctypes.c_bool(debug_mode)

        result = self.dll.Asap3Init(
            self.handle.byref,
            c_response_timeout,
            c_working_dir,
            c_fifo_size,
            c_debug_mode,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init2(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        sample_size: int = 256,
        debug_mode: bool = True,
    ) -> bool:
        """Initialize ASAP3 connection (with sample size).

        In addition to Asap3Init(), the maximum number of measurement values
        per FIFO entry can be set.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        sample_size : int, optional
            The maximum number of measurement values per FIFO entry is 256,
            by default 256.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        working_dir = os.path.abspath(working_dir)
        os.makedirs(working_dir, exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_working_dir = ctypes.c_char_p(working_dir.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_sample_size = ctypes.c_ulong(sample_size)
        c_debug_mode = ctypes.c_bool(debug_mode)

        result = self.dll.Asap3Init2(
            self.handle.byref,
            c_response_timeout,
            c_working_dir,
            c_fifo_size,
            c_sample_size,
            c_debug_mode,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init3(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        sample_size: int = 256,
        debug_mode: bool = True,
        clear_device_list: bool = True,
    ) -> bool:
        """Initialize ASAP3 connection (with device list control).

        In addition to Asap3Init2(), the device list of CANape is only cleared
        if the value of clear_device_list is True.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        sample_size : int, optional
            Maximum number of measurement values per FIFO entry, by default 256.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.
        clear_device_list : bool, optional
            If True, the CANape device list will be cleared, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        working_dir = os.path.abspath(working_dir)
        os.makedirs(working_dir, exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_working_dir = ctypes.c_char_p(working_dir.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_sample_size = ctypes.c_ulong(sample_size)
        c_debug_mode = ctypes.c_bool(debug_mode)
        c_clear_device_list = ctypes.c_bool(clear_device_list)

        result = self.dll.Asap3Init3(
            self.handle.byref,
            c_response_timeout,
            c_working_dir,
            c_fifo_size,
            c_sample_size,
            c_debug_mode,
            c_clear_device_list,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init4(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        sample_size: int = 256,
        debug_mode: bool = True,
        clear_device_list: bool = True,
        hex_mode: bool = False,
    ) -> bool:
        """Initialize ASAP3 connection (with hex mode).

        In addition to Asap3Init3(), CANape is started in Hex mode if
        hex_mode is True. Hex is a special CANape mode to view databases
        or hex files without a device. In this mode data acquisition is
        impossible.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        sample_size : int, optional
            Maximum number of measurement values per FIFO entry, by default 256.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.
        clear_device_list : bool, optional
            If True, the CANape device list will be cleared, by default True.
        hex_mode : bool, optional
            If True, CANape will be started in HexMode, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        working_dir = os.path.abspath(working_dir)
        os.makedirs(working_dir, exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_working_dir = ctypes.c_char_p(working_dir.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_sample_size = ctypes.c_ulong(sample_size)
        c_debug_mode = ctypes.c_bool(debug_mode)
        c_clear_device_list = ctypes.c_bool(clear_device_list)
        c_hex_mode = ctypes.c_bool(hex_mode)

        result = self.dll.Asap3Init4(
            self.handle.byref,
            c_response_timeout,
            c_working_dir,
            c_fifo_size,
            c_sample_size,
            c_debug_mode,
            c_clear_device_list,
            c_hex_mode,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init5(
        self,
        response_timeout: int = 10000,
        working_dir: str = "canape_tmp",
        fifo_size: int = 8192,
        sample_size: int = 256,
        debug_mode: bool = True,
        clear_device_list: bool = True,
        hex_mode: bool = False,
        modal_mode: bool = False,
    ) -> bool:
        """Initialize ASAP3 connection (with modal mode).

        In addition to Asap3Init4(), CANape is started in non-modal mode
        if modal_mode is False.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        working_dir : str, optional
            Sets CANape working directory, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        sample_size : int, optional
            Maximum number of measurement values per FIFO entry, by default 256.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.
        clear_device_list : bool, optional
            If True, the CANape device list will be cleared, by default True.
        hex_mode : bool, optional
            If True, CANape will be started in HexMode, by default False.
        modal_mode : bool, optional
            If True, CANape will be started in NON MODAL mode, by default False.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        working_dir = os.path.abspath(working_dir)
        os.makedirs(working_dir, exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_working_dir = ctypes.c_char_p(working_dir.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_sample_size = ctypes.c_ulong(sample_size)
        c_debug_mode = ctypes.c_bool(debug_mode)
        c_clear_device_list = ctypes.c_bool(clear_device_list)
        c_hex_mode = ctypes.c_bool(hex_mode)
        c_modal_mode = ctypes.c_bool(modal_mode)

        result = self.dll.Asap3Init5(
            self.handle.byref,
            c_response_timeout,
            c_working_dir,
            c_fifo_size,
            c_sample_size,
            c_debug_mode,
            c_clear_device_list,
            c_hex_mode,
            c_modal_mode,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Init6(
        self,
        response_timeout: int = 10000,
        project_file: str = "canape_tmp",
        fifo_size: int = 8192,
        sample_size: int = 256,
        debug_mode: bool = True,
        clear_device_list: bool = True,
        hex_mode: bool = False,
        modal_mode: bool = False,
        application_type: Optional[int] = None,
        application_path: Optional[str] = None,
    ) -> bool:
        """Initialize ASAP3 connection (with application type).

        In addition to Asap3Init5(), this function allows specifying the
        application type and path.

        Parameters
        ----------
        response_timeout : int, optional
            Maximum response time in milliseconds, by default 10000.
        project_file : str, optional
            Sets CANape project file, by default "canape_tmp".
        fifo_size : int, optional
            Total size of FIFO used for data acquisition, by default 8192.
        sample_size : int, optional
            Maximum number of measurement values per FIFO entry, by default 256.
        debug_mode : bool, optional
            If True, call CANape in 'normal' screen size, by default True.
        clear_device_list : bool, optional
            If True, the CANape device list will be cleared, by default True.
        hex_mode : bool, optional
            If True, CANape will be started in HexMode, by default False.
        modal_mode : bool, optional
            If True, CANape will be started in NON MODAL mode, by default False.
        application_type : Optional[int], optional
            Application type (0=UNDEFINED, 1=CANAPE, 3=APPLOCATION),
            by default None.
        application_path : Optional[str], optional
            Application path if application_type is APPLOCATION, by default None.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If initialization fails.
        """
        project_file = os.path.abspath(project_file)
        os.makedirs(os.path.dirname(project_file) or ".", exist_ok=True)

        c_response_timeout = ctypes.c_ulong(response_timeout)
        c_project_file = ctypes.c_char_p(project_file.encode("UTF-8"))
        c_fifo_size = ctypes.c_ulong(fifo_size)
        c_sample_size = ctypes.c_ulong(sample_size)
        c_debug_mode = ctypes.c_bool(debug_mode)
        c_clear_device_list = ctypes.c_bool(clear_device_list)
        c_hex_mode = ctypes.c_bool(hex_mode)
        c_modal_mode = ctypes.c_bool(modal_mode)

        # Create application ID if provided
        app_id = None
        if application_type is not None:
            app_id = TApplicationID()
            app_id.tApplicationType = application_type
            if application_path:
                app_id.tApplicationPath = ctypes.c_char_p(application_path.encode("UTF-8"))

        c_app_id = ctypes.POINTER(TApplicationID)(app_id) if app_id else None

        result = self.dll.Asap3Init6(
            self.handle.byref,
            c_response_timeout,
            c_project_file,
            c_fifo_size,
            c_sample_size,
            c_debug_mode,
            c_clear_device_list,
            c_hex_mode,
            c_modal_mode,
            c_app_id,
        )

        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to initialize CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3Exit(self) -> bool:
        """Shut down ASAP3 connection to CANape (terminates CANape).

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If exit fails.
        """
        result = self.dll.Asap3Exit(self.handle.handle)
        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to exit CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        self.handle.invalidate()
        return result

    def Asap3Exit2(self, close_canape: bool = True) -> bool:
        """Shut down ASAP3 connection with optional CANape termination.

        Parameters
        ----------
        close_canape : bool, optional
            If True, CANape will be shut down. If False, CANape will remain
            running, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeInitializationError
            If exit fails.
        """
        c_close_canape = ctypes.c_bool(close_canape)
        result = self.dll.Asap3Exit2(self.handle.handle, c_close_canape)
        if not result:
            error_code = self._get_last_error()
            raise CANapeInitializationError(
                f"Failed to exit CANape (Error Code: {error_code})",
                error_code=error_code,
            )
        if close_canape:
            self.handle.invalidate()
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
