from pathlib import Path

def from_root():
    return Path(__file__).resolve().parent.parent.parent
