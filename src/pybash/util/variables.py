__all__ = ["variables"]

@(lambda f: dict(f()))
def variables():
    import subprocess as sp

    kw = dict()
    kw["stdout"] = kw["stdin"] = kw["stderr"] = sp.PIPE
    kw["text"] = True
    p = sp.Popen(["cmd.exe", "/c", "set"], **kw) # type: sp.Popen[str]
    variables, _ = p.communicate()
    variables = variables.strip()
    for line in variables.splitlines():
        var_name, var_value = line.split("=")
        yield (var_name, var_value)