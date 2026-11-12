"""Make `tools` importable from the tests."""

import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent

sys.path.insert(0, str(TOOLS))
