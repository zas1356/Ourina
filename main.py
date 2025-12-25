#!/usr/bin/env python3
import asyncio
import sys
import os
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    os.system('chcp 65001 > nul 2>&1')

sys.path.insert(0, str(Path(__file__).parent))

from ui.cli import OurinaCLI


def main():
    try:
        cli = OurinaCLI()
        asyncio.run(cli.run())
    except KeyboardInterrupt:
        print("\n\nBye! See you next time!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
