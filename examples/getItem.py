from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

collection.get("hello")
#collection.get(path)
#ift dont found the key, returns None