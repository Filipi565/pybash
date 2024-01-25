from .util import VersionInfo
__version__ = VersionInfo(1, 1, 0)
del VersionInfo

from ._main import main

__all__ = [
    "main"
]