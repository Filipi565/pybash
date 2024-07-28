# PyBash

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
pip install $USERPROFILE\\TemporaryModule
```

This is Equivalent to "pip install C:\Users\MyUser\TemporaryModule"

* Bug Fixes

Fixed "--command" argument not working

Fixed "import_ext" function now working

* Upload the License File that i accidentally deleted