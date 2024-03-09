from importlib import import_module
from pathlib import Path

__all__ = []

# for f in list(Path(__file__).parent.glob("*.pyx")) + list(Path(__file__).parent.glob("*.py")):
for f in list(Path(__file__).parent.glob("*.py")):
# pyx_files = ['buffer_work_space.pyx', 'anchoring.pyx', 'file_read_back.pyx', 'galechurch.pyx', 'greedy.pyx',
#              'utilities.pyx']
#
# for f in [Path(__file__).parent / f for f in pyx_files] + list(Path(__file__).parent.glob("*.py")):
    print(f)
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
        __all__.append(module_name)
    del f, module_name

del import_module, Path
