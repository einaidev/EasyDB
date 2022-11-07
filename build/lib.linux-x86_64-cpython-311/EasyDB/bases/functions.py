from .decorators import Mode
import json, os, io

class _:
    modes ={}

class DataBase_Functions:
    modes = {}
    def __init__(self) -> None:
        self.modes = _.modes

    @Mode("!autoSave", _.modes)
    def create(name,val,path="",class_=None):
        # print(name,val,path,class)
        _path = class_.getPath(path)

        if not path == "":
            exec("class_.json{}[{!r}] = val".format(_path,name))
        else:
            exec("class_.json[{!r}] = val".format(name))

    @Mode("autoSave",_.modes)
    def create(name,val,path="",class_=None,loc=""):
        class_.save__Backup()
        _path = class_.getPath(path)



        if not path == "":
            exec("class_.json{}[{!r}] = val".format(_path,name))
        else:
            exec("class_.json[{!r}] = val".format(name))

        with open(loc,"w") as w:
            try:
                json.dump(class_.json,w,indent=4)
            except Exception as e:
                print(e,class_.json)
                w.write("{}")
                
        class_.save__Backup()

    @Mode("!autoSave",_.modes)
    def load(fp:str | io.BufferedReader, class_) -> None:
        try:
            class_.json = json.load(fp) if not isinstance(fp,str) else json.load(open(fp,"r"))
        except Exception as e:
            if isinstance(e, io.UnsupportedOperation):
                raise ValueError("Unsuported mode, please, enable read mode\nopen(path, \"r\")")
            else:
                raise e

    @Mode("autoSave",_.modes)
    def load(fp:str | io.BufferedReader, class_, loc) -> None:
        try:
            class_.save__Backup()
            class_.json = json.load(fp) if not isinstance(fp,str) else json.load(open(fp,"r"))
            json.dump(class_.json, open(loc,"w"), indent=4)
        except Exception as e:
            if isinstance(e, io.UnsupportedOperation):
                raise ValueError("Unsuported mode, please, enable read mode\nopen(path, \"r\")")
            else:
                raise e

    @Mode("!autoSave", _.modes)
    def delete(path,class_):
        _path = class_.getPath(path) 
        exec("del class_.json{}".format(_path))

    @Mode("autoSave",_.modes)
    def delete(path,class_,loc,loc_):
        _back = class_.json.copy()
        class_.save__Backup()
        _path = class_.getPath(path) 
        _b = class_.get_Backups()    
        _ = class_.get_Backups_List(_b)

        idx = _.index(class_.json)
        _.pop(idx)
        os.remove(loc_.format(_b[idx]))

        exec("del class_.json{}".format(_path))
        json.dump(class_.json,open(loc,"w"),indent=4)
        if class_.autosave:
            _b.pop(idx)
        class_.save__Backup(_back)

class filter:
    def __init__(self, path,v) -> None:
        self._path = path
        self._value = v

    @property
    def value(self): 
        return self._value
    
    @property
    def path(self):
        return self._path


class FindMethod:
    def __init__(self,_json) -> None:
        self.json = _json

    def find(self,func) -> list[filter]:
        _ = []
        for i in self.Walk_(self.json):
            if func(i[-1]) and isinstance(func(i[-1]),bool):
                _.append(filter("".join([f"[{x!r}]"for x in i[:-1]]), i[-1]))
            else:
                if not isinstance(func(i[-1]),bool):
                    raise ValueError("The function dont return a boolean")
        return _
        
    def Walk_(self,val,pre=None):
        pre = pre if pre else []
        if isinstance(val,dict):
            for k,v in val.items():
                if isinstance(v,dict):
                    for d in self.Walk_(v,pre+[k]):
                        yield d
                elif isinstance(v,list):
                    if all(isinstance(item,int) for item in v) or all(isinstance(item,str) for item in v):
                        yield pre+[v]
                    else:
                        for i in v:
                            for d in self.Walk_(i,pre+[k]):
                                yield d
                else:
                    yield pre+[k,v]
        else:
            yield pre + [val]
