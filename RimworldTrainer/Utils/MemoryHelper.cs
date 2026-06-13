using Memory;

namespace RimworldTrainer.Utils
{
    public static class MemoryHelper
    {
        public static bool IsProcessRunning(string processName)
        {
            return Mem.GetProcessesByName(processName).Length > 0;
        }
    }
}