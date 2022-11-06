from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

def filter(arg):
    #filter, also you could use lambda
    if isinstance(arg,list):
        return 1 in arg
    else:
        return 1 == arg

collection.find(filter)

# or

collection.find(lambda x: 1 in x if isinstance(x,list) else 1 == x )