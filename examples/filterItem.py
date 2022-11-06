from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

def filter(arg):
    #filter, also you could use lambda
    if isinstance(arg,list):
        return 1 in arg
    else:
        return 1==arg

for x in collection.filter(filter):
    print(x.value, x.path)

# or

for x in collection.filter(lambda x: 1 in x if isinstance(x,list) else 1 == x ):
    print(x.value, x.path)