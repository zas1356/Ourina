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
    from .gemini import GeminiClient
except:
    _gemini = load_pyc("gemini", _dir / "gemini.pyc")
    GeminiClient = _gemini.GeminiClient

try:
    from .memory import Memory
except:
    _memory = load_pyc("memory", _dir / "memory.pyc")
    Memory = _memory.Memory

try:
    from .engine import OurinaEngine
except:
    _engine = load_pyc("engine", _dir / "engine.pyc")
    OurinaEngine = _engine.OurinaEngine

from .personality import Personality
from .todo import TodoManager
from .voice import VoiceOutput

__all__ = ["GeminiClient", "Memory", "Personality", "OurinaEngine", "TodoManager", "VoiceOutput"]
