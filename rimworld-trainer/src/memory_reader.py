"""Low-level memory reading utilities for process access."""

import ctypes
import ctypes.wintypes
from typing import Optional, List

# Windows API constants
PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400

class MemoryReader:
    """Reads process memory on Windows using kernel32."""

    def __init__(self, process_name: str):
        self.process_name = process_name
        self.handle = None
        self.pid = None

    def open_process(self) -> bool:
        """Open target process by name. Returns True on success."""
        kernel32 = ctypes.windll.kernel32
        # Simple PID finder (mock for cross-platform safety)
        import psutil
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == self.process_name:
                self.pid = proc.info['pid']
                self.handle = kernel32.OpenProcess(
                    PROCESS_VM_READ | PROCESS_QUERY_INFORMATION,
                    False, self.pid
                )
                return self.handle != 0
        return False

    def read_int(self, address: int) -> Optional[int]:
        """Read a 4-byte integer from process memory."""
        if not self.handle:
            return None
        buffer = ctypes.c_int(0)
        bytes_read = ctypes.c_size_t(0)
        kernel32 = ctypes.windll.kernel32
        success = kernel32.ReadProcessMemory(
            self.handle,
            ctypes.c_void_p(address),
            ctypes.byref(buffer),
            ctypes.sizeof(buffer),
            ctypes.byref(bytes_read)
        )
        return buffer.value if success else None

    def close(self):
        """Release process handle."""
        if self.handle:
            ctypes.windll.kernel32.CloseHandle(self.handle)
            self.handle = None