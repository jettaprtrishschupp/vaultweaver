import subprocess
try:
    from auto_updater.notify import notify
except ImportError:
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from auto_updater.notify import notify

def main():
    try:
        out = subprocess.check_output(["git","log","--since=7.days","--pretty=oneline"]).decode("utf-8","ignore")
        n = len([l for l in out.splitlines() if l.strip()])
    except Exception as e:
        notify(f"Weekly report error: {e}"); return
    notify(f"Weekly report: {n} commits in the last 7 days")

if __name__ == "__main__":
    main()
