# PyBash

# Release Noted: 1.4.1

* Enviroment bug fix

# Release Notes: 1.4.0

* Fix code

* Add getting the process output as command line

Ex.:

```bash
echo `where cmd`
```

output: C:\Windows\System32\cmd.exe

# Release Notes: 1.3.3

* Envrioment Variables

Chaged the way to call a envrioment variable

from: "$VARNAME" to "$(VARNAME)"

Ex.:

```bash
cd $(TEMP)
```

This is Equivalent to "cd C:\Users\MyUser\AppData\Local\Temp"

# Release Notes: 1.3.2

* Envrioment Variables

You can now use your envrioment variables

Ex.:

```bash
cd $TEMP 
```

This is Equivalent to "cd C:\Users\MyUser\AppData\Local\Temp"

This function is used on executing other programs too

Ex.:

```bash
pip install $USERPROFILE\TemporaryModule
```

This is Equivalent to "pip install C:\Users\MyUser\TemporaryModule"

* Bug Fixes

Fixed "--command" argument not working

Fixed "import_ext" function not working

Fixed ".\YourProgram.exe" implementation not working

* Upload the License File that i accidentally deleted
