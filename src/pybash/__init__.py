from .util import VersionInfo
__version__ = VersionInfo(1, 4, 0)
del VersionInfo

from ._main import main
del util, _main

__all__ = [
    "main"
]
