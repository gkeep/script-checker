import sys
from cx_Freeze import setup, Executable

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    include_files = [""]
else:
    include_files = get_qt_plugins_paths("PySide2", "platforms")

build_exe_options = {
    "excludes": ["tkinter"],
    "include_files": include_files,
    "path": sys.path + ["src"],
    "packages": "queue",
}

executables = [Executable("src/main.py", base=None, target_name="script_checker")]

setup(
    name="script-checker",
    version="2023.09",
    description="script-checker",
    options={
        "build_exe": build_exe_options,
    },
    executables=executables,
)