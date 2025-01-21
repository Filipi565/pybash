import subprocess as sp
import typing as t
import os

def _get_text_of_process(command: str):
    args = list(_args(command.split(" ")))
    
    kw = {}
    kw["stdin"] = kw["stdout"] = kw["stderr"] = sp.PIPE
    kw["text"] = True

    process = sp.Popen(args, env=os.environ, **kw)
    stdout, stderr = process.communicate()

    if (process.returncode != 0):
        raise Exception(f"Process returned with an error with Code: {process.returncode}, Error output: {stderr}")
    
    return stdout.strip()

class _args(t.Iterable[str]):
    def __init__(self, args: t.Iterable[str]) -> None:
       self.__args__ = args

    def __iter__(self) -> t.Generator[str, None, None]:
        items = self._step_1(self.__args__)

        for item in self._step_2(items):
            while ("$(" in item):
                var_name = self._get_var_name(item)
                if var_name in os.environ:
                    item = item.replace(f"$({var_name})", os.environ[var_name])
                else:
                    raise Exception(f"Cloud not find the variable: \"{var_name}\"")
            
            yield item

    @classmethod
    def _get_var_name(cls, string: str, start: str = "$(", end: str = ")"):
        index = string.index(start)+len(start)
        return string[index:].split(end)[0]

    @classmethod
    def _step_2(cls, args: t.Iterable[str]):
        for item in args:
            if item[0] + item[-1] == "``":
                yield _get_text_of_process(item[1:-1])
            else:
                yield item

    @classmethod
    def _step_1(cls, args: t.Iterable[str]):
        new_argument_bool = False
        new_argument_object = "/\\:;"
        New_Argument: list[str] = None
        for argument in args:
            if not argument:
                continue

            if argument[0] + argument[-1] in {"\"\"", "\'\'"}:
                yield argument[1:-1]
                continue

            if argument.startswith(("\"", "\'", "`")):
                New_Argument = list()
                New_Argument.append(argument)
                new_argument_bool = True
                new_argument_object = argument[0]
                continue
            
            if argument.endswith(new_argument_object):
                new_argument_bool = False
                New_Argument.append(argument)

                if (new_argument_object == "`"):
                    yield " ".join(New_Argument)
                else:
                    yield " ".join(New_Argument)[1:-1]
                
                new_argument_object = "/\\::"
                continue
            
            if new_argument_bool:
                New_Argument.append(argument)
            else:
                yield argument

def args(args: t.Iterable[str]) -> t.List[str]:
    return list(_args(args))
