# RimWorld Trainer

A lightweight memory trainer for RimWorld (Windows x64). Reads resource values (wood, steel, silver) from the game process.

## Features
- Connect to running RimWorld process
- Read current resource amounts from memory
- Extensible offset system

## Requirements
- Python 3.8+
- Windows (uses kernel32.dll for memory access)
- Running RimWorld (RimWorldWin64.exe)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from src.trainer_core import RimWorldTrainer

trainer = RimWorldTrainer()
if trainer.connect():
    resources = trainer.get_resources()
    print(resources)  # {'wood': 250, 'steel': 100, 'silver': 500}
    trainer.disconnect()
```

## Testing
```bash
python -m pytest tests/
```