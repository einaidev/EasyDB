from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

collection.delete("hello")
#collection.delete(path)