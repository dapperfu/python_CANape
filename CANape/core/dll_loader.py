"""DLL loader with configurable path and error handling.

This module provides functionality for loading the CANapAPI64.dll with
support for environment variables, registry lookup, and configurable paths.
"""

import ctypes
import os
import sys
from typing import Optional

from .exceptions import CANapeDLLError

# Default DLL name
DEFAULT_DLL_NAME = "CANapAPI64.dll"


def find_canape_dll(dll_path: Optional[str] = None) -> str:
    """Find CANape DLL using multiple strategies.

    Parameters
    ----------
    dll_path : Optional[str], optional
        Explicit DLL path, by default None.

    Returns
    -------
    str
        Path to the CANape DLL.

    Raises
    ------
    CANapeDLLError
        If DLL cannot be found.
    """
    # Strategy 1: Use explicit path if provided
    if dll_path:
        if os.path.exists(dll_path):
            return os.path.abspath(dll_path)
        raise CANapeDLLError(f"DLL not found at specified path: {dll_path}")

    # Strategy 2: Check environment variable
    env_path = os.environ.get("CANAPE_DLL_PATH")
    if env_path and os.path.exists(env_path):
        return os.path.abspath(env_path)

    # Strategy 3: Check Windows registry (Windows only)
    if sys.platform == "win32":
        try:
            import winreg

            try:
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\VECTOR\CANape",
                )
                reg_path, _ = winreg.QueryValueEx(key, "Path")
                winreg.CloseKey(key)

                dll_path = os.path.join(reg_path, "CANapeAPI", DEFAULT_DLL_NAME)
                if os.path.exists(dll_path):
                    return os.path.abspath(dll_path)
            except (OSError, FileNotFoundError):
                pass
        except ImportError:
            pass

    # Strategy 4: Check common installation paths
    common_paths = [
        r"C:\Program Files\Vector CANape 17\CANapeAPI\CANapAPI64.dll",
        r"C:\Program Files\Vector CANape 18\CANapeAPI\CANapAPI64.dll",
        r"C:\Program Files\Vector CANape 19\CANapeAPI\CANapAPI64.dll",
        r"C:\Program Files (x86)\Vector CANape 17\CANapeAPI\CANapAPI64.dll",
        r"C:\Program Files (x86)\Vector CANape 18\CANapeAPI\CANapAPI64.dll",
        r"C:\Program Files (x86)\Vector CANape 19\CANapeAPI\CANapAPI64.dll",
    ]

    for path in common_paths:
        if os.path.exists(path):
            return os.path.abspath(path)

    # Strategy 5: Check current directory and PATH
    if os.path.exists(DEFAULT_DLL_NAME):
        return os.path.abspath(DEFAULT_DLL_NAME)

    # If all strategies fail, raise error
    raise CANapeDLLError(
        f"Could not find {DEFAULT_DLL_NAME}. "
        "Please set CANAPE_DLL_PATH environment variable or provide dll_path parameter."
    )


def load_dll(dll_path: Optional[str] = None) -> ctypes.WinDLL:
    """Load CANape DLL.

    Parameters
    ----------
    dll_path : Optional[str], optional
        Explicit DLL path, by default None (will search automatically).

    Returns
    -------
    ctypes.WinDLL
        Loaded DLL object.

    Raises
    ------
    CANapeDLLError
        If DLL cannot be loaded.
    """
    if sys.platform != "win32":
        raise CANapeDLLError("CANape DLL is only available on Windows")

    try:
        resolved_path = find_canape_dll(dll_path)
        dll = ctypes.windll.LoadLibrary(resolved_path)
        return dll
    except OSError as e:
        raise CANapeDLLError(f"Failed to load DLL: {e}") from e

