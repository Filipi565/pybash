import typing as t

class _args:
    @classmethod
    def args(cls, args: t.Iterable[str]):
        new_argument_bool = False
        new_argument_object = "/\\:;" * 100
        New_Argument: list[str] = None
        for argument in args:
            if not argument:
                continue

            if argument[0] + argument[-1] in ("\"\"", "\'\'"):
                yield argument[1:-1]
                continue

            if argument.startswith(("\"", "\'")):
                New_Argument = list()
                New_Argument.append(argument)
                new_argument_bool = True
                new_argument_object = argument[0]
                continue
            
            if argument.endswith(new_argument_object):
                new_argument_bool = False
                New_Argument.append(argument)
                new_argument_object = "/\\::" * 100
                yield " ".join(New_Argument)[1:-1]
                continue
            
            if new_argument_bool:
                New_Argument.append(argument)
            else:
                yield argument
        
        del New_Argument, new_argument_bool, new_argument_object

def args(args: t.Iterable[str]) -> t.List[str]:
    return list(_args.args(args))