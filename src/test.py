import sys
from pathlib import Path

PROJECTPATH = Path(__file__).parent.parent.absolute()

if PROJECTPATH not in sys.path:
    sys.path.append(PROJECTPATH)

print(sys.path)