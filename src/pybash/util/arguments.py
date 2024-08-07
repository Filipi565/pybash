from .variables import variables
import typing as t

class _args(t.Iterable[str]):
    def __init__(self, args: t.Iterable[str]) -> None:
       self.__args__ = args

    def __iter__(self) -> t.Generator[str, None, None]:
        for item in self._step_1(self.__args__):
            while ("$(" in item):
                var_name = self._get_var_name(item)
                if var_name in variables:
                    item = item.replace(f"$({var_name})", variables[var_name])
                else:
                    raise Exception(f"Cloud not find the variable: \"{var_name}\"")
            
            yield item

    @classmethod
    def _get_var_name(cls, string: str):
        index = string.index("$(")+2
        return string[index:].split(")")[0]
    
    @classmethod
    def _step_1(cls, args: t.Iterable[str]):
        new_argument_bool = False
        new_argument_object = "/\\:;" * 100
        New_Argument: list[str] = None
        for argument in args:
            if not argument:
                continue

            if argument[0] + argument[-1] in {"\"\"", "\'\'"}:
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

def args(args: t.Iterable[str]) -> t.List[str]:
    return list(_args(args))
