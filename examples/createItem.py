from EasyDB import EasyDB,DB

collection:DB = EasyDB().newCollection

items = [
    ("hello", {}),
    ("how are you?", "good", "hello")
    #(key, object, path)
]

for i in items:
    collection.create(*i)

# or

collection.create("hello", {})
collection.create("how are you?", "good","hello")