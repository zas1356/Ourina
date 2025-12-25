import importlib.util
import sys
from pathlib import Path

def load_pyc(name, pyc_path):
    spec = importlib.util.spec_from_file_location(name, pyc_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

_dir = Path(__file__).parent

try:
    from .cli import OurinaCLI
except:
    _cli = load_pyc("cli", _dir / "cli.pyc")
    OurinaCLI = _cli.OurinaCLI

try:
    from .themes import get_theme, set_theme, list_themes, THEMES
except:
    from themes import get_theme, set_theme, list_themes, THEMES

__all__ = ["OurinaCLI", "get_theme", "set_theme", "list_themes", "THEMES"]
