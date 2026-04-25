import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "include-files" : ["icons", "hello.html"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Dominator",
        version = "0.3",
        description = "Dominant colors extractor",
        options = {"build_exe": {"icon" : "icons/icon.ico"}},
        executables = [Executable("start.py", base=base)])