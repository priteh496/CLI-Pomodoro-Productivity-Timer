"""
Core countdown timer logic with terminal display.
"""

import time
import sys
from src.stats import SessionStats


class PomodoroTimer:
    def __init__(self, work_minutes: int, short_break: int, long_break: int,
                 sessions_before_long: int, task: str, stats: SessionStats):
        self.work_minutes = work_minutes
        self.short_break = short_break
        self.long_break = long_break
        self.sessions_before_long = sessions_before_long
        self.task = task
        self.stats = stats
        self.session_count = 0

    def _countdown(self, total_seconds: int, label: str):
        """Display a live countdown timer."""
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            bar_len = 30
            filled = int(bar_len * (total_seconds - remaining) / total_seconds)
            bar = "█" * filled + "░" * (bar_len - filled)
            sys.stdout.write(f"\r  {label}: [{bar}] {mins:02d}:{secs:02d}  ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write(f"\r  {label}: [{'█' * 30}] 00:00  ✅\n")
        sys.stdout.flush()

    def _notify(self, message: str):
        """Print a notification."""
        print(f"\n🔔 {message}")

    def run(self):
        """Main timer loop."""
        session_num = 1
        while True:
            # Work session
            label = f"Work #{session_num}"
            if self.task:
                label += f" [{self.task}]"
            self._notify(f"Work session #{session_num} starting...")
            self._countdown(self.work_minutes * 60, label)
            self.session_count += 1
            self.stats.record_session(self.work_minutes, self.task)

            # Decide break type
            if self.session_count % self.sessions_before_long == 0:
                self._notify("🌿 Long break time!")
                self._countdown(self.long_break * 60, "Long Break")
            else:
                self._notify("☕ Short break time!")
                self._countdown(self.short_break * 60, "Short Break")

            session_num += 1
