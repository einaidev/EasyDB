handlerbase = """
'Auto Generated By Easy.DB'

import json,os,threading
from EasyDB.C import get_path
from EasyDB.bases import DataBase_Functions, FindMethod
class DB:
    def __init__(self, autosave=True) -> None:
        self.autosave = autosave
        self.funcionsWrapper = DataBase_Functions()
        self.modes = self.funcionsWrapper.modes

        try:
            if self.autosave:
                self.json = json.loads(open(_[name]_,"r").read())
            else:
                self.json = {}
        except:
            if os.listdir("_[temp]_").__len__() > 0:
                _b = []
                for i in os.listdir("_[temp]_"):
                    if i.endswith(".json"):
                        if i.replace(".json","").isnumeric():
                            _b.append(int(i.replace(".json","")))
                _b.sort()
                if not _b.__len__() == 0:
                    _a = _b.copy()
                    _a.sort(reverse=True)
                    self.idx = 0
                    self._e = True
                    try:
                        self.json = json.loads(open("_[temp]_/{0}.json".format(_b[-1]),"r").read())
                    except:
                        while self._e:
                            def __(idx,_a):
                                if os.listdir("_[temp]_") == 0:
                                    self.json = {}
                                    self._e = False
                                try:
                                    self.json = json.loads(open("_[temp]_/{0}.json".format(_a[self.idx%_a.__len__()]),"r").read())
                                    self._e = False
                                except:
                                    os.remove("_[temp]_/{0}.json".format(_a[self.idx%_a.__len__()]))
                                    self.idx +=1
                            threading.Thread(None,target=__,args=(self.idx,_a)).start()
                else:
                    self.json = {}
            else:
                self.json = {}
            json.dump(self.json, open(_[name]_,"w"), indent=4)

    def create(self, name, val, path:str=""):
        if not self.autosave:
            for i in self.modes["!autoSave"]:
                if i["name"] == "create":
                    i["function"](name,val,path,self)
        else:
            for i in self.modes["autoSave"]:
                if i["name"] == "create":
                    i["function"](name,val,path,self,_[name]_)     

    def get(self,path=""):
        _path = self.getPath(path)
        try:
            exec("global a; a = self.json{0}".format(_path if not path == "" else path))
            global a
            return a
        except:
            return None

        
    def delete(self,path):
        if not self.autosave:
            for i in self.modes["!autoSave"]:
                if i["name"] == "delete":
                    i["function"](path,self)
        else:
            for i in self.modes["autoSave"]:
                if i["name"] == "delete":
                    i["function"](path,self,_[name]_,"_[temp]_/{}.json")  

    def load(self,path, mode):
        if not self.autosave:
            for i in self.modes["!autoSave"]:
                if i["name"] == "load":
                    i["function"](path,self,mode)
        else:
            for i in self.modes["autoSave"]:
                if i["name"] == "load":
                    i["function"](path,self,_[name]_,mode)  

    def getPath(self,path=...):
        return get_path(path)

    def filter(self,func):
        return FindMethod(self.json).find(func)

    def find(self,func):
        return self.filter(func)[0]

    def save(self,):
        json.dump(self.json,open(_[name]_, "w"), indent=4)
        self.save__Backup()

    def save__Backup(self,obj=None):
        if os.listdir("_[temp]_").__len__() == 0:
            with open("_[temp]_/1.json", "w") as w:
                json.dump(self.json if not obj else obj,w,indent=4)
        else:
            _b = self.get_Backups()
            _ = self.get_Backups_List(_b)

            if (self.json if not obj else obj) in _:
                return
            if _b.__len__() == 0:
                _b.append(0)
            with open("_[temp]_/{0}.json".format(str(_b[-1]+1)), "w") as w:
                json.dump(self.json if not obj else obj,w,indent=4)

    def get_Backups(self,):
        _b = []
        for i in os.listdir("_[temp]_"):
                if i.endswith(".json"):
                    if i.replace(".json", "").isnumeric():
                        _b.append(int(i.replace(".json","")))
        _b.sort()
        return _b                

    def get_Backups_List(self,_b):
        _ = []
        for i in _b:
            try:
                _.append(json.loads(open("_[temp]_/{0}.json".format(str(i)),"r" ).read()))
            except:
                os.remove("_[temp]_/{0}.json".format(str(i)))
                _b.remove(i)
        return _

"""
initHandler= "'Auto Generated By Easy.DB'\nfrom ._[name]_ import DB"