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
    return None

# Functions
def ClearTerminal(*_):
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def ChangeDirectory(directory = "."):
    directory = __abspath(directory)
    if directory == None:
        return
    
    if not os.path.exists(directory):
        raise Exception("Path not found")

    if not os.path.isdir(directory):
        raise Exception("Path is not a directory")

    os.chdir(directory)

def ListDirectory(directory = "."):
    directory = __abspath(directory)
    if directory == None:
        return
    
    with os.scandir(directory) as dir:
        for item in dir:
            if item.is_dir():
                print(f"\033[96m{item.name}\\")
            else:
                print(f"{WHITE}{item.name}")
        print(WHITE, end="")

def Remove(*args:str):
    if len(args) == 1:
        path = __abspath(args[0])
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
                path = __abspath(argv)
    else:
        raise Exception("no argument was given")
    
    if type == "normal":
        if os.path.isdir(path):
            raise Exception("Path is not a dir")
        os.remove(path)
    
    if type == "forced":
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors)
            return
        
        os.remove(path)

def RemoveDirectory(path:str):
    if not os.path.isdir(path):
        raise Exception("Path is not a directory")
    
    try:
        os.rmdir(path)
    except Exception as e:
        print(e)

def MakeDirectory(path):
    os.mkdir(path)

def whoami(*_):
    print(USER_NAME)

def hostname(*_):
    print(HOST_NAME)

def add_ext_dir(path):
    path = __abspath(path)
    if not os.path.isdir(path):
        raise Exception(f"Path {path} is not a dir")

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
rmdir = RemoveDirectory
mkdir = MakeDirectory
#endregion
