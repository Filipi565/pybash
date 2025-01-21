import socket
import sys
import os

RESET = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[31m"
CYAN = "\033[96m"

USER_PATH = os.path.expanduser("~")

USER_NAME = os.getlogin()
HOST_NAME = socket.gethostname()

VAR_SEP = ";" if sys.platform == "win32" else ":"

del os
del sys
del socket