using System;
using System.Diagnostics;
using System.Windows;
using Memory;

namespace RimworldTrainer
{
    public partial class MainWindow : Window
    {
        private Mem _mem = new Mem();
        private const string ProcessName = "RimWorldWin64";

        public MainWindow()
        {
            InitializeComponent();
            Loaded += OnWindowLoaded;
        }

        private void OnWindowLoaded(object sender, RoutedEventArgs e)
        {
            var process = Process.GetProcessesByName(ProcessName).FirstOrDefault();
            if (process == null)
            {
                MessageBox.Show($"{ProcessName} not running!", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            _mem.OpenProcess(process.Id);
            UpdateStatus();
        }

        private void UpdateStatus()
        {
            StatusLabel.Content = _mem.theProc == null ? "Disconnected" : $"Connected to PID: {_mem.theProc.Id}";
        }

        private void AddSilver_Click(object sender, RoutedEventArgs e)
        {
            if (_mem.theProc == null) return;
            var address = _mem.AoBScan("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 ?? 8B 40 ??").Result.FirstOrDefault();
            if (address == 0) return;

            var silverPtr = _mem.ReadLong(address + 0x3) + address + 0x7;
            _mem.WriteMemory(silverPtr.ToString("X"), "int", (_mem.ReadInt(silverPtr.ToString("X")) + 1000).ToString());
        }
    }
}