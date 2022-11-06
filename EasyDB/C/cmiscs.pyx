import os

def get_path(path):
    _p = []
    for i in path.split("."):
        _p.append(f"[{i!r}]")
    _path = "".join(_p)
    return _path

