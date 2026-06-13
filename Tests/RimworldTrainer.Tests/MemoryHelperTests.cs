using RimworldTrainer.Utils;
using Xunit;

namespace RimworldTrainer.Tests
{
    public class MemoryHelperTests
    {
        [Fact]
        public void IsProcessRunning_WhenProcessNotRunning_ReturnsFalse()
        {
            Assert.False(MemoryHelper.IsProcessRunning("NonExistentProcess"));
        }
    }
}