# EasyDB
a simple python local database

## Documentation
to get started in an easy way... let's start by creating a new instance of the Data Base

```py
from EasyDB import EasyDB, DB

db = EasyDB(autoSave=True)
collection: DB = db.newCollection
```

what is "autoSave" of the DB instance?

it is an automatic backup method, which you can activate or deactivate... having this system activated... your database is less vulnerable to a total loss
of data, in case something unforeseen occurs

# Creating Objects In The Database
> You can see some examples on: [Create Items](https://github.com/einaidev/EasyDB/blob/main/examples/createItem.py)

for you to create objects in the database, it is also very easy... see below
```py
collection.create("hello", "word")
```
>Just that? ya

it is worth noting. To create objects in the database in a specific way you can do:

```py
collection.create("hello", {})
collection.create("how are you?","good, and you?", "hello")
```
```json
{
  "hello": {
    "how are you?": "good, and you?"
  }
}
```
> the path must be divided by dots

```py
collection.create("hello", {})
collection.create("how are you?", {}, "hello")
collection.create("good, and you?", "me also", "hello.how are you?")
```
## Deleting Objects
> You can see some examples on: [Delete Items](https://github.com/einaidev/EasyDB/blob/main/examples/deleteItem.py)

to delete an object you just use the .delete method. see below
```py
collection.delete("path")
```
## Filtering objects
> You can see some examples on: [Filtering Items](https://github.com/einaidev/EasyDB/blob/main/examples/filterItem.py)
To get start filtering objects, you must create a filter, lambda or a normal def
```py
def filter(arg): #receive a db object
  #your stuff, but must return a bool
  return arg == 1
  
 #or
 
filter = lambda x: x == 1
 
```
 and then, call 
```py
for i in collection.filter(filter):
  print(i.path, i.value)
```
### Attributes
filtering method returns 2 attributes. path and value
> value return the value what returns True
> path return the path of the value ("path.to.value")

## Find objects
> You can see some examples on: [Finding Items](https://github.com/einaidev/EasyDB/blob/main/examples/findItem.py)
Find item is like the filtering method... but returns only one value

```py
result = collection.find(filter)
print(result.path, result.value)
```

## Get object
> You can see some examples on: [Getting Items](https://github.com/einaidev/EasyDB/blob/main/examples/getItem.py)
To get a item, you can just type:
```py
print(collection.get(path if has))
```

## Miscs
if autoSave is off... you can store any type of object.
however when trying to save, it will corrupt your database

# Progres
- [x] sync and local db
- [ ] async DB
