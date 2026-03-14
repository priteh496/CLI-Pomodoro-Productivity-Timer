"""
Session statistics - tracks completed pomodoro sessions using a local JSON file.
"""

import json
import os
from datetime import date
from pathlib import Path


STATS_FILE = Path.home() / ".pomodoro_stats.json"


class SessionStats:
    def __init__(self):
        self.data = self._load()

    def _load(self) -> dict:
        if STATS_FILE.exists():
            try:
                return json.loads(STATS_FILE.read_text())
            except (json.JSONDecodeError, OSError):
                pass
        return {}

    def _save(self):
        STATS_FILE.write_text(json.dumps(self.data, indent=2))

    def record_session(self, minutes: int, task: str = ""):
        today = str(date.today())
        if today not in self.data:
            self.data[today] = {"sessions": [], "total_minutes": 0}
        self.data[today]["sessions"].append({"minutes": minutes, "task": task or "General"})
        self.data[today]["total_minutes"] += minutes
        self._save()

    def show(self):
        print("\n📊 Pomodoro Statistics\n")
        if not self.data:
            print("  No sessions recorded yet.")
            return
        for day, info in sorted(self.data.items(), reverse=True)[:7]:
            sessions = len(info["sessions"])
            total = info["total_minutes"]
            print(f"  {day}: {sessions} session(s) | {total} minutes focused")
        print()
