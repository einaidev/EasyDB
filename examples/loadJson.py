from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

collection.load("<path or file stream>", mode="append")
#collection.load("<path or file stream>", mode "append"|"set")