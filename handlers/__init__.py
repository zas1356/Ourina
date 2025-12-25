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
    from .commands import CommandHandler, CommandResult
except:
    _commands = load_pyc("commands", _dir / "commands.pyc")
    CommandHandler = _commands.CommandHandler
    CommandResult = _commands.CommandResult

__all__ = ["CommandHandler", "CommandResult"]
