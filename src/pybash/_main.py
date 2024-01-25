import subprocess as sp
import os
import sys
from .constants import *
from .functions import *

def import_ext(*args):
    local = dict()
    for ext in args:
        exec(f"from {ext} import *", None, local)
    globals().update(local)

# This is to solve some bugs
exit = lambda: None
del exit
del print

from .functions import print as echo
print = echo

def _run(command:str):
    args = command.split(" ")
    __command = args[0].strip()
    args.remove(args[0])
    from .util import args as _args
    args = _args(args)
    del _args
    if __command.startswith((".\\", "./")):
        __command = os.path.abspath(__command)
        
    if __command in globals():
        try:
            globals()[__command](*args)
        except BaseException as e:
            print(e)
        return
    try:
        sp.Popen([os.path.join(COMMANDS_PATH, __command), *args]).wait()
    except (FileNotFoundError):
        try:
            sp.Popen([__command, *args]).wait()
        except FileNotFoundError:
            if os.path.isabs(__command):
                __command = os.path.basename(__command)
            print(f"Command Not Found: {__command}")
        except (Exception) as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        if sys.platform.startswith("win"):
            os.system("title Bash")
        this_dir = os.getcwd()
        dir_for_print = this_dir.replace(USER_PATH, "~", 1)
        from builtins import print as _print
        _print(f"{GREEN}{USER_NAME}@{HOST_NAME} {WHITE}{BLUE}{dir_for_print}{WHITE}$", end=" ")
        del _print
        command = input().strip()
        if not command:
            continue

        if command == "exit":
            return 0
        
        for command in command.split(";"):
            _run(command.strip())
