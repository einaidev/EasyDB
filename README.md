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
> You can see some examples on: [Create Items](https://github.com/einaidev/EasyDB/blob/main/examples/deleteItem.py)

to delete an object you just use the .delete method. see below
```py
collection.delete("path")
```









