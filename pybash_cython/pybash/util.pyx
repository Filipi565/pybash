def args(args:list[str]):
    new_argument_bool = False
    for argument in args:
        if not argument:
            continue

        if argument[0] + argument[-1] in ("\"\"", "\'\'"):
            yield argument[1:-1]
            continue

        if argument.startswith("\"") or argument.startswith("\'"):
            New_Argument = list()
            New_Argument.append(argument)
            new_argument_bool = True
            continue
        
        if argument.endswith("\'") or argument.endswith("\""):
            new_argument_bool = False
            New_Argument.append(argument)
            yield " ".join(New_Argument)[1:-1]
            continue
        
        if new_argument_bool:
            New_Argument.append(argument)
        else:
            yield argument

