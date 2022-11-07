import os, sys, importlib
from ..bases import handlerbase,DB,initHandler,code
class CollectionModel:
    def __init__(self,name,autosave, _path) -> None:
        self._path = os.path.dirname(_path)
        self.name = name+"_DB"
        self.autosave = autosave
        if self.name in os.listdir(self._path):
            if (self.name+".py" not in os.listdir(f"{self._path}/{self.name}")):
                self._(self.name)
            if self.name+".json" not in os.listdir(f"{self._path}/{self.name}"):
                self._(self.name)
        else:
            os.mkdir(f"{self._path}/{self.name}")
            os.mkdir(f"{self._path}/{self.name}/tmp")
            self._(self.name)
    def _(self,name) -> None:
        if self.autosave:
            with open(f"{self._path}/{self.name}/{name}.json", "w") as w_:
                w_.write("{}") 
        with open(f"{self._path}/{self.name}/{name}.py", "w") as w_:
            w_.write(handlerbase.replace("_[name]_",f'"{self._path}/{self.name}/{name}.json"').replace("_[temp]_", f"{self._path}/{self.name}/tmp"))
        with open(f"{self._path}/{self.name}/__init__.py", "w") as w_:
            w_.write(initHandler.replace("_[name]_",f'{name}'))

    def db(self) -> DB:
        def __():
            _name=""
            _e = False
            for i in os.walk(self._path):
                if self.name in i[1]:
                    _name = i[0]
                    break
            try:    
                _:DB = importlib.__import__(f"{self.name}").DB(self.autosave)
            except:
                _i = 1
                _n = (_name.split("\\") if "\\" in _name else _name.split("/"))[1:]
                _ = None
                while True:
                    try:
                        # print("{1}.{0}".format(self.name, ".".join(_n[::-1][:_i][::-1])))
                        _:DB = importlib.__import__("{1}.{0}".format(self.name, ".".join(_n[::-1][:_i][::-1]))).__dict__[self.name].DB(self.autosave)
                        break
                    except Exception as e:
                        _i += 1
                        if _i > _n.__len__():
                            print(e)
                            break          
            return _
        return __