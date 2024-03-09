from importlib import import_module
from pathlib import Path

__all__ = []

for f in list(Path(__file__).parent.glob("*.py")):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
        __all__.append(module_name)
    del f, module_name

del import_module, Path
