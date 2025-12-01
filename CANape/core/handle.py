"""Handle management for CANape API.

This module provides functionality for managing CANape handles with
proper validation and lifecycle management.
"""

import ctypes
from typing import Optional

from .exceptions import CANapeHandleError
from .types import TAsap3Hdl


class Handle:
    """CANape handle wrapper with validation.

    Parameters
    ----------
    handle : Optional[TAsap3Hdl], optional
        Existing handle, by default None (creates new).

    Attributes
    ----------
    handle : TAsap3Hdl
        The underlying CANape handle.
    valid : bool
        Whether the handle is valid.
    """

    def __init__(self, handle: Optional[TAsap3Hdl] = None) -> None:
        """Initialize handle.

        Parameters
        ----------
        handle : Optional[TAsap3Hdl], optional
            Existing handle, by default None.
        """
        if handle is None:
            self.handle = TAsap3Hdl()
        else:
            self.handle = handle
        self.valid = True

    @property
    def byref(self) -> ctypes._Pointer:
        """Get byref pointer to handle.

        Returns
        -------
        ctypes._Pointer
            Pointer to handle.
        """
        if not self.valid:
            raise CANapeHandleError("Handle is no longer valid")
        return ctypes.byref(self.handle)

    def invalidate(self) -> None:
        """Invalidate the handle."""
        self.valid = False

    def __repr__(self) -> str:
        """Return string representation."""
        status = "valid" if self.valid else "invalid"
        return f"Handle<{status}>"

    def __bool__(self) -> bool:
        """Check if handle is valid."""
        return self.valid
