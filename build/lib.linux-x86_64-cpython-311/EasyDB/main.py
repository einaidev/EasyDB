from .collections_ import *
import sys,os
class EasyDB:
    def __init__(self, autoSave = True) -> None:
        self.autoSave = autoSave
        
    @property
    def newCollection(self) -> CollectionModel:
        origin = sys.modules['__main__'].__file__
        __ = []
        ([(__.append(x) if os.path.dirname(os.path.abspath(origin)) in sys.modules[x].__file__.__str__() else ...)if "__file__" in sys.modules[x].__dict__ else ... for x in sys.modules])
        _path = sys.modules[__[-1]].__file__ if __.__len__() > 1 else origin

        _:CollectionModel =  CollectionModel(_path.split("\\")[-1].replace(".py","") 
        if "\\" in _path else _path.split("/",)[-1].replace(".py",""),  self.autoSave,_path).db()
        return _()