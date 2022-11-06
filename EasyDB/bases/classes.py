from .functions import filter

class DB:
    def __init__(self,autosave=True) -> None:
        ...

    def create(self, name, val, path:str=""):
        """Create
        the "create" method is responsible for creating objects in the database        

        usage: .create(<name>,<val>,<path | opcional>)
        """

    def delete(self,path):
        """Create
        the "delete" method is responsible for deleting objects in the database        

        usage: .delete(<path>)
        """ 

    def get(self,path="") -> dict | list | str | int | object:
        ...

    def filter(self,function) -> list[filter]:
        ...

    def find(self,function) -> filter:
        ...