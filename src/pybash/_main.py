import subprocess as sp
import os
import sys
from .constants import *
from .functions import *

# This is to solve some bugs
exit = lambda: None
del exit
del print

from .functions import _ImportExtType
import_ext = _ImportExtType(globals())
del _ImportExtType

from .functions import print as echo
print = echo

def _in_globals(item: str) -> bool:
    try:
        globals()[item]
    except KeyError:
        return False
    else: # if item is in global ...
        if item[0] == "_":
            return False
        else:
            return True

def _run(command: str) -> None:
    args = command.split(" ")
    __command = args[0].strip()
    args.remove(args[0])
    from .util import args as _args
    args = _args(args)
    del _args
    if __command.startswith("."):
        __command = os.path.abspath(__command)
        
    if _in_globals(__command):
        try:
            globals()[__command](*args)
        except BaseException as e:
            print(RED + f"Error: {e}" + RESET, file=sys.stderr)
        return
    try:
        sp.Popen([os.path.join(COMMANDS_PATH, __command), *args]).wait()
    except (FileNotFoundError):
        try:
            sp.Popen([__command, *args]).wait()
        except (FileNotFoundError):
            if os.path.isabs(__command):
                __command = os.path.basename(__command)
            print(RED + f"Command Not Found: {__command}" + RESET, file=sys.stderr)
        except (Exception) as e:
            print(RED + f"Error: {e}" + RESET, file=sys.stderr)
    except Exception as e:
        print(RED + f"Error: {e}" + RESET, file=sys.stderr)

def main() -> int:
    while True:
        try:
            if sys.platform.startswith("win"):
                os.system("title Bash")
            this_dir = os.getcwd()
            dir_for_print = this_dir.replace(USER_PATH, "~", 1)
            print(f"{GREEN}{USER_NAME}@{HOST_NAME} {RESET}{BLUE}{dir_for_print}{RESET}$", end=" ")
            command = input().strip()
            if not command:
                continue

            if command == "exit":
                return 0
            
            for command in command.split(";"):
                _run(command.strip())

        except KeyboardInterrupt:
            pass
        
        except BaseException:
            return 1