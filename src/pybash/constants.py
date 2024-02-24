import os
import socket

WHITE = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"

USER_PATH = os.path.expanduser("~")

COMMANDS_PATH = os.path.abspath(os.path.join(__file__, "..", "commands"))

USER_NAME = os.getlogin()
HOST_NAME = socket.gethostname()

del os
del socket

class CommandNotFound(Exception):
    def __init__(self, command_name):
        super().__init__(f"Command not found {command_name}")