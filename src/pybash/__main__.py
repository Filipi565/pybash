from . import main
import sys

if len(sys.argv) == 1:
    sys.exit(main())

from ._main import _run as run

no_exit = False

for i, argv in enumerate(sys.argv):
    if argv == "--no-exit":
        no_exit = True
    
    if argv == "--command":
        for comando in sys.argv[i+1].split(";"):
            run(comando.strip())

if no_exit:
    sys.exit(main())