import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "include-files" : ["icons", "hello.html"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Dominator",
        version = "0.2",
        description = "My GUI application!",
        options = {"build_exe": {"icon" : "icons/icon.ico"}},
        executables = [Executable("start.py", base=base)])