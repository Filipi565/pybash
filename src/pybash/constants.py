import os
import socket

RESET = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[31m"
CYAN = "\033[96m"

USER_PATH = os.path.expanduser("~")

COMMANDS_PATH = os.path.abspath(os.path.join(__file__, "..", "commands"))

USER_NAME = os.getlogin()
HOST_NAME = socket.gethostname()

del os
del socket