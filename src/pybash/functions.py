from __future__ import annotations

import os
import sys
import shutil
from .constants import *
import typing as t
import importlib

def _get_all(module):
    all = getattr(module, "__all__", None) # type: filter[str] | None
    if all is not None:
        yield from all
    else:
        for item in dir(module):
            if item[0] == "_":
                continue

            value = getattr(module, item)
            if isinstance(value, type(os)):
                continue
            else:
                yield item

def _update_globals(module, globals):
    # type: (object, t.MutableMapping[str, object]) -> None
    for item in _get_all(module):
        globals[item] = getattr(module, item)

class PrintErrType(object):
    def __call__(self, *args: object):
        from builtins import print
        print(RED, end="")
        print(*args, file=sys.stderr)
        print(RESET, end="")

class ImportExtType(object):
    def __init__(self, globals: t.MutableMapping[str, object]):
        self.__globals = globals
    
    def __call__(self, *exts: str):
        for ext in exts:
            module = importlib.import_module(ext)
            _update_globals(module, self.__globals)

printerr = PrintErrType()

#region functions
@t.overload
def print(*args: object, end: str | None = None, sep: str = " ") -> None: ...

def print(*args: object, **kw: str):
    end = kw.pop("end", os.linesep)
    sep = kw.pop("sep", " ")
    file = kw.pop("file", sys.stdout)
    if end is None:
        end = os.linesep
    for item in kw:
        raise TypeError(f"print() got an unexpected keyword argument: {item}")
    
    def arguments(arguments): # type: (object) -> t.Generator[str, t.Any, None]
        for arg in arguments:
            if isinstance(arg, str):
                yield arg
            else:
                yield repr(arg)
    
    file.write(sep.join(arguments(args)))
    
    file.write(end)

def _abspath(path:str): # under development
    if path.startswith("~"):
        path = path.replace("~", USER_PATH, 1)
    
    path = os.path.abspath(path)
    if not ("*" in path):
        return path
    
    arquivos: list[str] = list()
    for _ in range(path.count("*")):
        count = path.index("*")
        __path = path[0:count]
        directory = os.path.dirname(__path)
        with os.scandir(directory) as scan:
            for item in scan:
                if item.path.startswith(__path):
                    arquivos.append(item.path)

            if len(arquivos) == 1:
                path = arquivos[0] + path[count+1:sys.maxsize]
                arquivos.clear()
            else:
                print("value without support \"*\"")
                return None
        
    if len(arquivos) == 0:
        return path

    print("value without support \"*\"")
    return None

def ClearTerminal(*_):
    print("\033[H\033[2J", end="")

def ChangeDirectory(directory = "."):
    directory = _abspath(directory)
    if directory is None:
        return
    
    if not os.path.exists(directory):
        raise FileNotFoundError("Path not found")

    if not os.path.isdir(directory):
        raise NotADirectoryError("Path is not a directory")

    os.chdir(directory)

def ListDirectory(directory = "."):
    directory = _abspath(directory)
    if directory is None:
        return
    
    with os.scandir(directory) as dir:
        for item in dir:
            if item.is_dir():
                print(f"\033[96m{item.name}\\")
            else:
                print(f"{RESET}{item.name}")

def Remove(*args: str):
    if len(args) == 1:
        path = _abspath(args[0])
        type = "normal"
        ignore_errors = False

    elif len(args) >= 2:
        type = "normal"
        ignore_errors = False
        for argv in args:
            if argv == "-rf":
                type = "forced"
            
            elif argv == "--ignore-erros":
                ignore_errors = True

            else:
                path = _abspath(argv)
    else:
        raise Exception("no argument was given")
    
    if path is None:
        return 

    if type == "normal":
        if os.path.isdir(path):
            raise Exception("Path is not a file")
        os.remove(path)
    
    if type == "forced":
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors)
            return
        
        try:
            os.remove(path)
        except BaseException:
            if not ignore_errors:
                raise

def RemoveDirectory(path: str):
    path = _abspath(path)
    if path is None:
        return
    
    if not os.path.isdir(path):
        raise Exception("Path is not a directory")
    
    try:
        os.rmdir(path)
    except Exception as e:
        print(e)

def MakeDirectory(path):
    os.makedirs(path)

def whoami():
    print(USER_NAME)

def hostname():
    print(HOST_NAME)

def add_ext_dir(path):
    path = _abspath(path)
    if path is None:
        return

    if not os.path.isdir(path):
        raise NotADirectoryError(f"Path {path} is not a dir")

    try:
        sys.path.append(path)
        #print(f"directory: \"{path}\" added to path!")
    except BaseException as e:
        printerr("Error: %s" % e)
#endregion

#region Alias
cls = clear = ClearTerminal
cd = ChangeDirectory
ls = ListDirectory
delete = rm = Remove
rmdir = RemoveDirectory
mkdir = MakeDirectory
#endregion

FuncType = type(cd)

def _all_filter(v):
    # type: (str) -> bool
    return v[0] != "_" and isinstance(globals()[v], FuncType)

__all__ = list(filter(_all_filter, globals()))
del _all_filter
del FuncType