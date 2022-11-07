from .functions import filter
import io

class DB:
    def __init__(self,autosave=True) -> None:
        ...

    def create(self, name, val, path:str=""):
        """Create
        the "create" method is responsible for creating objects in the database        

        usage: .create(<name>,<val>,<path | opcional>)
        ----------------------------------------------
        """

    def delete(self,path):
        """Delte
        the "delete" method is responsible for deleting objects in the database        

        usage: .delete(<path>)
        ----------------------
        """ 

    def get(self,path="") -> dict | list | str | int | object:
        """Get
        the "get" method is responsible for geting items from the database        

        usage: .get(<path>)
        -------------------
        """ 
        ...

    def filter(self,function) -> list[filter]:
        """Filter
        the "filter" method is responsible for filtering items from the database       

        usage: .filter(<filter>)
        ------------------------
        filter models:
        -------------
            filter = lambda x: "hello" == x
        """ 
        ...

    def find(self,function) -> filter:
        """Find
        the "find" method is responsible for findings items from the database       

        usage: .find(<filter>)
        ------------------------
        filter models:
        -------------
            filter = lambda x: "hello" == x
        """
        ...

    def save(self,) -> None:
        """Find
        the "save" method is responsible for saving the database       

        usage: .save()
        --------------
        """
        ...

    def load(self, fp:str | io.BufferedReader) -> None:
        """Load
        the "load" method is responsible for load a json in the database    

        mode: set | append

        usage: .load(path or open())
        --------------
        """
        ...