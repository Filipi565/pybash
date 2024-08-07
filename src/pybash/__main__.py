from . import main
import sys

if len(sys.argv) == 1:
    sys.exit(main())

from ._main import _run as run

no_exit = False

for i, argv in enumerate(sys.argv):
    if argv == "--no-exit":
        no_exit = True
    
    if ("--version" in sys.argv) or ("-V" in sys.argv):
        from . import __version__ as version
        print(version)
        del version
        try:
            sys.argv.remove("--version")
        except ValueError:
            pass
        try:
            sys.argv.remove("-V")
        except ValueError:
            pass
    
    if argv == "--command":
        try:
            for comando in sys.argv[i+1].split(";"):
                run(comando.strip())
        except IndexError:
            raise RuntimeError("Command not given")

if no_exit:
    sys.exit(main())