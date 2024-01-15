import os
import sys
import shutil
from .constants import *

#region functions
def __abspath(path:str): # under development
    if path.startswith("~"):
        path = path.replace("~", USER_PATH, 1)
    
    path = os.path.abspath(path)
    if not ("*" in path):
        return path
    
    arquivos = list()
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
                return "."
        
    if len(arquivos) == 0:
        return path

    print("value without support \"*\"")
    return "."

# Functions
def ClearTerminal(*_):
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def ChangeDirectory(directory = "."):
    directory = __abspath(directory)
    if not os.path.exists(directory) and not os.path.isdir(directory):
        print("The Path is not a dir or is not found")
        return

    os.chdir(directory)

def ListDirectory(directory = "."):
    directory = __abspath(directory)
    with os.scandir(directory) as dir:
        for item in dir:
            if item.is_dir():
                print(f"\033[96m{item.name}\\")
            else:
                print(f"{WHITE}{item.name}")

def Remove(path:str):
    if os.path.isdir(path):
        print("path is not a file")
        return

    try:
        os.remove(path)
    except Exception as e:
        print(e)

def RemoveDirectory(path:str):
    if not os.path.isdir(path):
        print("path is not a directory")
        return
    
    try:
        os.rmdir(path)
    except Exception as e:
        print(e)

def MakeDirectory(path):
    os.mkdir(path)

def ForceRemove(path):
    path = __abspath(path)
    if path == ".":
        return
    
    if not os.path.exists(path):
        print("path not found")
        return

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
        return

    try:
        os.remove(path)
    except Exception as e:
        print(e)

def whoami(*_):
    print(USER_NAME)

def hostname(*_):
    print(HOST_NAME)

def add_ext_dir(path):
    path = __abspath(path)
    if not os.path.isdir(path):
        print(f"path {path} is not a dir")
    
    try:
        sys.path.append(path)
        #print(f"directory: \"{path}\" added to path!")
    except (Exception, BaseException) as e:
        print(f"Error: {e}")
#endregion

#region Alias
cls = clear = ClearTerminal
cd = ChangeDirectory
ls = ListDirectory
echo = print
delete = rm = Remove
frm = ForceRemove
rmdir = RemoveDirectory
mkdir = MakeDirectory
#endregion
