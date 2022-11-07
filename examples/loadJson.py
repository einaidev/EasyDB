from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

collection.load("<path or file stream>", mode="add")
#collection.load("<path or file stream>", mode "append"|"set")