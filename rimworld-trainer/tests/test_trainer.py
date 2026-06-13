"""Unit tests for RimWorld Trainer components."""

import unittest
from unittest.mock import patch, MagicMock
from src.memory_reader import MemoryReader
from src.trainer_core import RimWorldTrainer, RESOURCE_OFFSETS

class TestMemoryReader(unittest.TestCase):
    """Test MemoryReader initialization and process opening."""

    @patch('src.memory_reader.psutil.process_iter')
    def test_open_process_found(self, mock_process_iter):
        """Test opening a running process by name."""
        mock_proc = MagicMock()
        mock_proc.info = {'pid': 1234, 'name': 'RimWorldWin64.exe'}
        mock_process_iter.return_value = [mock_proc]

        reader = MemoryReader("RimWorldWin64.exe")
        # Mock kernel32 OpenProcess to return non-zero handle
        with patch('ctypes.windll.kernel32.OpenProcess', return_value=1):
            result = reader.open_process()
        self.assertTrue(result)
        self.assertEqual(reader.pid, 1234)

    @patch('src.memory_reader.psutil.process_iter')
    def test_open_process_not_found(self, mock_process_iter):
        """Test when process does not exist."""
        mock_process_iter.return_value = []
        reader = MemoryReader("Nonexistent.exe")
        result = reader.open_process()
        self.assertFalse(result)

class TestRimWorldTrainer(unittest.TestCase):
    """Test RimWorldTrainer integration."""

    def test_connect_fail_no_process(self):
        """Test connect returns False when process missing."""
        trainer = RimWorldTrainer()
        with patch.object(trainer.reader, 'open_process', return_value=False):
            result = trainer.connect()
        self.assertFalse(result)
        self.assertFalse(trainer.connected)

    def test_get_resources_not_connected(self):
        """Test get_resources returns empty dict when not connected."""
        trainer = RimWorldTrainer()
        result = trainer.get_resources()
        self.assertEqual(result, {})

    def test_resource_offsets_defined(self):
        """Ensure resource offsets are properly defined."""
        expected = {"wood", "steel", "silver"}
        self.assertEqual(set(RESOURCE_OFFSETS.keys()), expected)

if __name__ == '__main__':
    unittest.main()