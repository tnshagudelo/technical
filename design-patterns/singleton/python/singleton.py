"""
Singleton pattern — two common Python implementations.

1. Classic __new__ override
2. Thread-safe variant using a lock
"""

import threading


# ---------------------------------------------------------------------------
# Implementation 1: using __new__
# ---------------------------------------------------------------------------

class Singleton:
    """Simple singleton via __new__."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # __init__ runs every time the constructor is called, so guard
        # any stateful initialisation with a flag.
        if not hasattr(self, "_initialised"):
            self.value = 0
            self._initialised = True


# ---------------------------------------------------------------------------
# Implementation 2: thread-safe using a lock
# ---------------------------------------------------------------------------

class ThreadSafeSingleton:
    """Singleton with double-checked locking for thread safety."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:          # second check inside lock
                    cls._instance = super().__new__(cls)
        return cls._instance


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(a is b)       # True — same object

    a.value = 42
    print(b.value)      # 42 — shared state

    x = ThreadSafeSingleton()
    y = ThreadSafeSingleton()
    print(x is y)       # True
