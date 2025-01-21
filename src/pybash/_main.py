import subprocess as sp
import os
import sys
import types
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

def _cmd_exists(path):
    return (os.path.exists(path) or os.path.exists(f"{path}.exe"))

def _get_command(cmd):
    for path in os.environ["PATH"].split(VAR_SEP):
        v = os.path.abspath(os.path.join(path, cmd))
        if (_cmd_exists(v)):
            return v
    
    return v # Default value

def _run(string: str) -> None:
    from .util import args as _args
    try:
        args = _args(string.split(" "))
    except Exception as e:
        print(RED + f"Error: {e}" + RESET, file=sys.stderr)
        return
    command = args[0].strip()
    
    del args[0]
    del _args
    if command.startswith("."):
        command = os.path.abspath(command)
        
    if _in_globals(command):
        try:
            globals()[command](*args)
        except BaseException as e:
            print(RED + f"Error: {e}" + RESET, file=sys.stderr)
        return
    try:
        sp.Popen([_get_command(command), *args]).wait()
    except (FileNotFoundError):
        if os.path.isabs(command):
            command = os.path.basename(command)
        print(RED + f"Command Not Found: {command}" + RESET, file=sys.stderr)
    except (Exception) as e:
        print(RED + f"Error: {e}" + RESET, file=sys.stderr)

inp_text = f"{GREEN}{USER_NAME}@{HOST_NAME} {RESET}{BLUE}" + "{current_dir}" + f"{RESET}$"

def main() -> int:
    while True:
        try:
            if sys.platform.startswith("win"):
                os.system("title Bash")
            this_dir = os.getcwd()
            dir_for_print = this_dir.replace(USER_PATH, "~", 1)
            print(inp_text.format(current_dir=dir_for_print), end=" ")
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
