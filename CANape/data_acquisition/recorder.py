"""Recorder Management Functions.

This module provides functions for managing MDF recorders.
"""

import ctypes
from typing import Any, List, Optional

from ..core.enums import EnRecorderState, TRecorderType
from ..core.exceptions import CANapeDataAcquisitionError
from ..core.handle import Handle
from ..core.types import DWORD, TModulHdl, TRecorderID


class RecorderManagement:
    """Recorder Management interface.

    This class provides methods for managing recorders.

    Parameters
    ----------
    dll : Any
        The loaded CANape DLL object.
    handle : Handle
        The CANape handle object.
    """

    def __init__(self, dll: Any, handle: Handle) -> None:
        """Initialize recorder management interface.

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
        if hasattr(self.dll, "Asap3DefineRecorder"):
            self.dll.Asap3DefineRecorder.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(TRecorderID),
                ctypes.c_int,
            )
            self.dll.Asap3DefineRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderType"):
            self.dll.Asap3GetRecorderType.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetRecorderType.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderName"):
            self.dll.Asap3GetRecorderName.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(ctypes.c_long),
            )
            self.dll.Asap3GetRecorderName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderCount"):
            self.dll.Asap3GetRecorderCount.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(ctypes.c_ulong),
            )
            self.dll.Asap3GetRecorderCount.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderByIndex"):
            self.dll.Asap3GetRecorderByIndex.argtypes = (
                ctypes.c_void_p,
                ctypes.c_ulong,
                ctypes.POINTER(TRecorderID),
            )
            self.dll.Asap3GetRecorderByIndex.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderByName"):
            self.dll.Asap3GetRecorderByName.argtypes = (
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(TRecorderID),
            )
            self.dll.Asap3GetRecorderByName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SelectRecorder"):
            self.dll.Asap3SelectRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
            )
            self.dll.Asap3SelectRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetSelectedRecorder"):
            self.dll.Asap3GetSelectedRecorder.argtypes = (
                ctypes.c_void_p,
                ctypes.POINTER(TRecorderID),
            )
            self.dll.Asap3GetSelectedRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3RemoveRecorder"):
            self.dll.Asap3RemoveRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
            )
            self.dll.Asap3RemoveRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderMdfFileName"):
            self.dll.Asap3GetRecorderMdfFileName.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_char),
                ctypes.POINTER(DWORD),
            )
            self.dll.Asap3GetRecorderMdfFileName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SetRecorderMdfFileName"):
            self.dll.Asap3SetRecorderMdfFileName.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.c_char_p,
            )
            self.dll.Asap3SetRecorderMdfFileName.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3SetRecorderDataReduction"):
            self.dll.Asap3SetRecorderDataReduction.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.c_int,
            )
            self.dll.Asap3SetRecorderDataReduction.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderDataReduction"):
            self.dll.Asap3GetRecorderDataReduction.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetRecorderDataReduction.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3GetRecorderState"):
            self.dll.Asap3GetRecorderState.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_int),
            )
            self.dll.Asap3GetRecorderState.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3PauseRecorder"):
            self.dll.Asap3PauseRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.c_bool,
            )
            self.dll.Asap3PauseRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3StartRecorder"):
            self.dll.Asap3StartRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
            )
            self.dll.Asap3StartRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3StopRecorder"):
            self.dll.Asap3StopRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.c_bool,
            )
            self.dll.Asap3StopRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3EnableRecorder"):
            self.dll.Asap3EnableRecorder.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.c_bool,
            )
            self.dll.Asap3EnableRecorder.restype = ctypes.c_bool

        if hasattr(self.dll, "Asap3IsRecorderEnabled"):
            self.dll.Asap3IsRecorderEnabled.argtypes = (
                ctypes.c_void_p,
                TRecorderID,
                ctypes.POINTER(ctypes.c_bool),
            )
            self.dll.Asap3IsRecorderEnabled.restype = ctypes.c_bool

    def Asap3DefineRecorder(
        self, recorder_name: str, recorder_type: int = 0
    ) -> TRecorderID:
        """Create a new recorder.

        Parameters
        ----------
        recorder_name : str
            Name of the new recorder.
        recorder_type : int, optional
            Recorder type (0=eTRecorderTypeMDF, 1=eTRecorderTypeILinkRT,
            2=eTRecorderTypeBLF), by default 0.

        Returns
        -------
        TRecorderID
            Recorder ID handle.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder creation fails.
        """
        if not hasattr(self.dll, "Asap3DefineRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3DefineRecorder not available in this DLL version"
            )

        c_recorder_name = ctypes.c_char_p(recorder_name.encode("UTF-8"))
        recorder_id = TRecorderID()

        result = self.dll.Asap3DefineRecorder(
            self.handle.handle,
            c_recorder_name,
            ctypes.byref(recorder_id),
            ctypes.c_int(recorder_type),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to define recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return recorder_id

    def Asap3GetRecorderType(
        self, recorder_id: TRecorderID
    ) -> int:
        """Get the type of a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        int
            Recorder type (see TRecorderType enum).

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder type cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderType"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderType not available in this DLL version"
            )

        recorder_type = ctypes.c_int()
        result = self.dll.Asap3GetRecorderType(
            self.handle.handle, recorder_id, ctypes.byref(recorder_type)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder type (Error Code: {error_code})",
                error_code=error_code,
            )
        return recorder_type.value

    def Asap3GetRecorderName(
        self, recorder_id: TRecorderID
    ) -> Optional[str]:
        """Get the name of a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        Optional[str]
            Recorder name, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder name cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderName"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderName not available in this DLL version"
            )

        # First call to get required buffer size
        size = ctypes.c_long(0)
        name = None

        # Query size
        result = self.dll.Asap3GetRecorderName(
            self.handle.handle, recorder_id, name, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder name size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get name
        buffer_size = size.value + 1
        name = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetRecorderName(
            self.handle.handle, recorder_id, name, ctypes.byref(size)
        )
        if result:
            return name.value.decode("UTF-8")
        return None

    def Asap3GetRecorderCount(self) -> int:
        """Get count of defined recorders.

        Returns
        -------
        int
            Count of defined recorders.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder count cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderCount"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderCount not available in this DLL version"
            )

        count = ctypes.c_ulong()
        result = self.dll.Asap3GetRecorderCount(
            self.handle.handle, ctypes.byref(count)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder count (Error Code: {error_code})",
                error_code=error_code,
            )
        return count.value

    def Asap3GetRecorderByIndex(
        self, index: int
    ) -> TRecorderID:
        """Get a recorder ID from the recorder list by index.

        Parameters
        ----------
        index : int
            Recorder index (0..Asap3GetRecorderCount()-1).

        Returns
        -------
        TRecorderID
            Recorder ID.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderByIndex"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderByIndex not available in this DLL version"
            )

        recorder_id = TRecorderID()
        result = self.dll.Asap3GetRecorderByIndex(
            self.handle.handle,
            ctypes.c_ulong(index),
            ctypes.byref(recorder_id),
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder by index (Error Code: {error_code})",
                error_code=error_code,
            )
        return recorder_id

    def Asap3GetRecorderByName(
        self, recorder_name: str
    ) -> TRecorderID:
        """Get a recorder ID from the recorder list by name.

        Parameters
        ----------
        recorder_name : str
            Name of the recorder.

        Returns
        -------
        TRecorderID
            Recorder ID.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderByName"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderByName not available in this DLL version"
            )

        c_recorder_name = ctypes.c_char_p(recorder_name.encode("UTF-8"))
        recorder_id = TRecorderID()

        result = self.dll.Asap3GetRecorderByName(
            self.handle.handle, c_recorder_name, ctypes.byref(recorder_id)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder by name (Error Code: {error_code})",
                error_code=error_code,
            )
        return recorder_id

    def Asap3SelectRecorder(
        self, recorder_id: TRecorderID
    ) -> bool:
        """Select a defined recorder.

        The selected recorder will be used by Asap3SetupDataAcquisitionChnl()
        when save_to_file is True.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID to select.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder selection fails.
        """
        if not hasattr(self.dll, "Asap3SelectRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3SelectRecorder not available in this DLL version"
            )

        result = self.dll.Asap3SelectRecorder(
            self.handle.handle, recorder_id
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to select recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetSelectedRecorder(self) -> TRecorderID:
        """Get the currently selected recorder.

        Returns
        -------
        TRecorderID
            Currently selected recorder ID.

        Raises
        ------
        CANapeDataAcquisitionError
            If selected recorder cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetSelectedRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3GetSelectedRecorder not available in this DLL version"
            )

        recorder_id = TRecorderID()
        result = self.dll.Asap3GetSelectedRecorder(
            self.handle.handle, ctypes.byref(recorder_id)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get selected recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return recorder_id

    def Asap3RemoveRecorder(
        self, recorder_id: TRecorderID
    ) -> bool:
        """Remove a recorder.

        Note: The currently selected recorder cannot be removed.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID to remove.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder removal fails.
        """
        if not hasattr(self.dll, "Asap3RemoveRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3RemoveRecorder not available in this DLL version"
            )

        result = self.dll.Asap3RemoveRecorder(
            self.handle.handle, recorder_id
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to remove recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetRecorderMdfFileName(
        self, recorder_id: TRecorderID
    ) -> Optional[str]:
        """Get the MDF filename of a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        Optional[str]
            MDF filename, or None if failed.

        Raises
        ------
        CANapeDataAcquisitionError
            If filename cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderMdfFileName"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderMdfFileName not available in this DLL version"
            )

        # First call to get required buffer size
        size = DWORD(0)
        filename = None

        # Query size
        result = self.dll.Asap3GetRecorderMdfFileName(
            self.handle.handle, recorder_id, filename, ctypes.byref(size)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get filename size (Error Code: {error_code})",
                error_code=error_code,
            )

        # Allocate buffer and get filename
        buffer_size = size.value + 1
        filename = ctypes.create_string_buffer(buffer_size)
        result = self.dll.Asap3GetRecorderMdfFileName(
            self.handle.handle, recorder_id, filename, ctypes.byref(size)
        )
        if result:
            return filename.value.decode("UTF-8")
        return None

    def Asap3SetRecorderMdfFileName(
        self, recorder_id: TRecorderID, filename: str
    ) -> bool:
        """Set the MDF filename for a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.
        filename : str
            MDF filename.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If filename cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetRecorderMdfFileName"):
            raise CANapeDataAcquisitionError(
                "Asap3SetRecorderMdfFileName not available in this DLL version"
            )

        c_filename = ctypes.c_char_p(filename.encode("UTF-8"))
        result = self.dll.Asap3SetRecorderMdfFileName(
            self.handle.handle, recorder_id, c_filename
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to set recorder filename (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3SetRecorderDataReduction(
        self, recorder_id: TRecorderID, reduction: int
    ) -> bool:
        """Set the data reduction parameter for a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.
        reduction : int
            Reduction parameter (e.g., reduction=1 every value, reduction=2
            every second value, reduction=n every n'th value).

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If data reduction cannot be set.
        """
        if not hasattr(self.dll, "Asap3SetRecorderDataReduction"):
            raise CANapeDataAcquisitionError(
                "Asap3SetRecorderDataReduction not available in this DLL version"
            )

        result = self.dll.Asap3SetRecorderDataReduction(
            self.handle.handle, recorder_id, ctypes.c_int(reduction)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to set data reduction (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3GetRecorderDataReduction(
        self, recorder_id: TRecorderID
    ) -> int:
        """Get the data reduction parameter for a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        int
            Data reduction parameter.

        Raises
        ------
        CANapeDataAcquisitionError
            If data reduction cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderDataReduction"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderDataReduction not available in this DLL version"
            )

        reduction = ctypes.c_int()
        result = self.dll.Asap3GetRecorderDataReduction(
            self.handle.handle, recorder_id, ctypes.byref(reduction)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get data reduction (Error Code: {error_code})",
                error_code=error_code,
            )
        return reduction.value

    def Asap3GetRecorderState(
        self, recorder_id: TRecorderID
    ) -> int:
        """Get the state of a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        int
            Recorder state (see EnRecorderState enum).

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3GetRecorderState"):
            raise CANapeDataAcquisitionError(
                "Asap3GetRecorderState not available in this DLL version"
            )

        state = ctypes.c_int()
        result = self.dll.Asap3GetRecorderState(
            self.handle.handle, recorder_id, ctypes.byref(state)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to get recorder state (Error Code: {error_code})",
                error_code=error_code,
            )
        return state.value

    def Asap3PauseRecorder(
        self, recorder_id: TRecorderID, pause: bool
    ) -> bool:
        """Pause or resume recording into the MDF file.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.
        pause : bool
            If True, the recorder pauses recording. If False, the recorder
            continues recording.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder pause fails.
        """
        if not hasattr(self.dll, "Asap3PauseRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3PauseRecorder not available in this DLL version"
            )

        result = self.dll.Asap3PauseRecorder(
            self.handle.handle, recorder_id, ctypes.c_bool(pause)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to pause recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3StartRecorder(
        self, recorder_id: TRecorderID
    ) -> bool:
        """Start recording into the MDF file.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder start fails.
        """
        if not hasattr(self.dll, "Asap3StartRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3StartRecorder not available in this DLL version"
            )

        result = self.dll.Asap3StartRecorder(
            self.handle.handle, recorder_id
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to start recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3StopRecorder(
        self, recorder_id: TRecorderID, save_to_mdf: bool = True
    ) -> bool:
        """Stop recording and write MDF file.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.
        save_to_mdf : bool, optional
            Save the MDF file, by default True.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder stop fails.
        """
        if not hasattr(self.dll, "Asap3StopRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3StopRecorder not available in this DLL version"
            )

        result = self.dll.Asap3StopRecorder(
            self.handle.handle, recorder_id, ctypes.c_bool(save_to_mdf)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to stop recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3EnableRecorder(
        self, recorder_id: TRecorderID, enable: bool
    ) -> bool:
        """Enable or disable a recorder.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.
        enable : bool
            If True, enables the recorder. If False, disables it.

        Returns
        -------
        bool
            True if successful, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder enable/disable fails.
        """
        if not hasattr(self.dll, "Asap3EnableRecorder"):
            raise CANapeDataAcquisitionError(
                "Asap3EnableRecorder not available in this DLL version"
            )

        result = self.dll.Asap3EnableRecorder(
            self.handle.handle, recorder_id, ctypes.c_bool(enable)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to enable/disable recorder (Error Code: {error_code})",
                error_code=error_code,
            )
        return result

    def Asap3IsRecorderEnabled(
        self, recorder_id: TRecorderID
    ) -> bool:
        """Check if a recorder is enabled.

        Parameters
        ----------
        recorder_id : TRecorderID
            Recorder ID.

        Returns
        -------
        bool
            True if recorder is enabled, False otherwise.

        Raises
        ------
        CANapeDataAcquisitionError
            If recorder state cannot be retrieved.
        """
        if not hasattr(self.dll, "Asap3IsRecorderEnabled"):
            raise CANapeDataAcquisitionError(
                "Asap3IsRecorderEnabled not available in this DLL version"
            )

        enabled = ctypes.c_bool()
        result = self.dll.Asap3IsRecorderEnabled(
            self.handle.handle, recorder_id, ctypes.byref(enabled)
        )
        if not result:
            error_code = self._get_last_error()
            raise CANapeDataAcquisitionError(
                f"Failed to check recorder enabled state (Error Code: {error_code})",
                error_code=error_code,
            )
        return enabled.value

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

