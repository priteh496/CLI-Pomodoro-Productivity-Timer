"""
CLI Pomodoro Productivity Timer
Focus timer with work/break sessions and statistics.
"""

import argparse
from src.timer import PomodoroTimer
from src.stats import SessionStats


def parse_args():
    parser = argparse.ArgumentParser(description="CLI Pomodoro Productivity Timer")
    parser.add_argument("--work", type=int, default=25, help="Work session minutes (default: 25)")
    parser.add_argument("--short-break", type=int, default=5, help="Short break minutes (default: 5)")
    parser.add_argument("--long-break", type=int, default=15, help="Long break after 4 sessions (default: 15)")
    parser.add_argument("--sessions", type=int, default=4, help="Sessions before long break (default: 4)")
    parser.add_argument("--stats", action="store_true", help="Show today's session stats")
    parser.add_argument("--task", type=str, default="", help="Task name for this session")
    return parser.parse_args()


def main():
    args = parse_args()
    stats = SessionStats()

    if args.stats:
        stats.show()
        return

    timer = PomodoroTimer(
        work_minutes=args.work,
        short_break=args.short_break,
        long_break=args.long_break,
        sessions_before_long=args.sessions,
        task=args.task,
        stats=stats,
    )

    print("\n🍅 Pomodoro Timer Started")
    print(f"   Work: {args.work}m | Short Break: {args.short_break}m | Long Break: {args.long_break}m")
    if args.task:
        print(f"   Task: {args.task}")
    print("   Press Ctrl+C to stop\n")

    try:
        timer.run()
    except KeyboardInterrupt:
        print("\n\n⏹ Timer stopped.")
        stats.show()


if __name__ == "__main__":
    main()
