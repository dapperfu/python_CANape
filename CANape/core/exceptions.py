"""Custom exception hierarchy for CANape API errors.

This module defines a comprehensive exception hierarchy for handling
CANape API errors with proper error codes and messages.
"""

from typing import Optional


class CANapeError(Exception):
    """Base exception for all CANape errors.

    Parameters
    ----------
    message : str
        Error message describing the error.
    error_code : int, optional
        CANape error code (AEC_* constant), by default None.

    Attributes
    ----------
    error_code : Optional[int]
        CANape error code if available.
    """

    def __init__(self, message: str, error_code: Optional[int] = None) -> None:
        """Initialize CANape error.

        Parameters
        ----------
        message : str
            Error message.
        error_code : Optional[int], optional
            Error code, by default None.
        """
        super().__init__(message)
        self.error_code = error_code
        self.message = message

    def __str__(self) -> str:
        """Return string representation of error."""
        if self.error_code is not None:
            return f"{self.message} (Error Code: {self.error_code})"
        return self.message


class CANapeDLLError(CANapeError):
    """Error loading or accessing the CANape DLL."""

    pass


class CANapeInitializationError(CANapeError):
    """Error during CANape initialization."""

    pass


class CANapeModuleError(CANapeError):
    """Error related to module operations."""

    pass


class CANapeCalibrationError(CANapeError):
    """Error during calibration operations."""

    pass


class CANapeDataAcquisitionError(CANapeError):
    """Error during data acquisition operations."""

    pass


class CANapeDiagnosticError(CANapeError):
    """Error during diagnostic operations."""

    pass


class CANapeScriptingError(CANapeError):
    """Error during scripting operations."""

    pass


class CANapeFlashError(CANapeError):
    """Error during flash operations."""

    pass


class CANapeNetworkError(CANapeError):
    """Error during network operations."""

    pass


class CANapeConfigurationError(CANapeError):
    """Error during configuration operations."""

    pass


class CANapeHandleError(CANapeError):
    """Error with handle operations."""

    pass


class CANapeTimeoutError(CANapeError):
    """Timeout error."""

    pass


class CANapeVersionError(CANapeError):
    """Version compatibility error."""

    pass

