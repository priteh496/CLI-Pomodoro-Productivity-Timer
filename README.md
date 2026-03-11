# CLI Pomodoro Productivity Timer

## Description
A terminal-based Pomodoro timer with visual progress bar, configurable session lengths, and session statistics tracking.

## Features
- Configurable work/short break/long break durations
- Visual progress bar in terminal
- Automatic long break after N sessions
- Session statistics saved to home directory
- Optional task labeling per session

## Tech Stack
- Python 3.10+
- `time`, `json`, `pathlib`

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python main.py
python main.py --work 30 --short-break 10
python main.py --task "Write unit tests"
python main.py --stats
```

## Example Output
```
🍅 Pomodoro Timer Started
   Work: 25m | Short Break: 5m | Long Break: 15m

🔔 Work session #1 starting...
  Work #1: [████████████░░░░░░░░░░░░░░░░░░] 12:34
```
