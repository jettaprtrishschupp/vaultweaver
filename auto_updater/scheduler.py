import random, time, subprocess
from datetime import datetime, timedelta

try:
    from auto_updater.notify import notify
except ImportError:
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from auto_updater.notify import notify

def run_updater():
    msg = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Запускаю updater.py"
    print(msg); notify(msg)
    subprocess.run(["python3", "auto_updater/updater.py"])

def main():
    delay = random.randint(0, 120*60)
    print(f"[{datetime.now():%F %T}] Scheduler стартовал, задержка {delay//60} мин")
    notify(f"Scheduler стартовал, задержка {delay//60} мин")
    time.sleep(delay)

    runs = random.choices([0,1,2], weights=[1,3,2])[0]
    notify(f"Сегодня планируется {runs} запуск(ов)")
    if runs == 0: return

    start_sec, end_sec = 9*3600, 22*3600
    times = sorted(random.sample(range(start_sec, end_sec), runs))
    notify("Сегодня коммиты будут в: " + ", ".join((datetime.min + timedelta(seconds=t)).strftime("%H:%M") for t in times))

    for t in times:
        now = datetime.now()
        target = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(seconds=t)
        wait = (target - now).total_seconds()
        if wait > 0:
            time.sleep(int(wait))
        run_updater()
    notify(f"Scheduler завершил работу, сегодня выполнено {runs} запуск(ов)")

if __name__ == "__main__":
    main()
