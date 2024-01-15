import subprocess as sp
import os
import sys
from .constants import *
from .functions import *
from .util import args as _args

# This is to solve some bugs
exit = lambda: None

def _run(command:str):
    args = command.split(" ")
    __command = args[0].strip()
    args.remove(args[0])
    args = list(_args(args))

    if __command == "import_ext":
        local = dict()
        for ext in args:
            exec(f"from {ext} import *", None, local)
        globals().update(local)
        return
    
    if __command[0:2] in ("./", ".\\"):
        __command = os.path.abspath(__command)
        
    if __command in globals():
        globals()[__command](*args)
        return
    try:
        sp.Popen([os.path.join(COMMANDS_PATH, __command), *args]).wait()
    except (FileNotFoundError):
        try:
            sp.Popen([__command, *args]).wait()
        except FileNotFoundError:
            print(f"Command Not Found: {__command}")
        except (Exception) as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        if sys.platform.startswith("win"):
            os.system("title Bash")
        while True:
            this_dir = os.getcwd()
            dir_for_print = this_dir.replace(USER_PATH, "~", 1)
            print(f"{GREEN}{USER_NAME}@{HOST_NAME} {WHITE}{BLUE}{dir_for_print}{WHITE}$", end=" ")
            command = input().strip()
            if not command:
                continue

            if command == "exit":
                return 0
            
            for command in command.split(";"):
                _run(command.strip())
    except:
        return 1