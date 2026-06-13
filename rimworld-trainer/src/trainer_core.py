"""Core trainer logic for RimWorld resource manipulation."""

from .memory_reader import MemoryReader
from typing import Dict, Optional

# Known memory offsets (example values, not real)
RESOURCE_OFFSETS = {
    "wood": 0x00A1B2C0,
    "steel": 0x00A1B2C4,
    "silver": 0x00A1B2C8,
}

class RimWorldTrainer:
    """High-level trainer interface for RimWorld resources."""

    def __init__(self):
        self.reader = MemoryReader("RimWorldWin64.exe")
        self.connected = False

    def connect(self) -> bool:
        """Attempt to connect to running RimWorld process."""
        self.connected = self.reader.open_process()
        return self.connected

    def get_resources(self) -> Dict[str, Optional[int]]:
        """Read current resource values from memory."""
        if not self.connected:
            return {}
        result = {}
        for name, offset in RESOURCE_OFFSETS.items():
            result[name] = self.reader.read_int(offset)
        return result

    def disconnect(self):
        """Close connection to game process."""
        self.reader.close()
        self.connected = False