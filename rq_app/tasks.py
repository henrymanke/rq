# tasks.py

import time

def example_task(n):
    """Beispielhafte Funktion, die die Zeit wartet und dann zurückgibt."""
    print(f"Task gestartet mit n={n}")
    time.sleep(n)
    print("Task abgeschlossen")
    return f"Task wurde für {n} Sekunden pausiert"
