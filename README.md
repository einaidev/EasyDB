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
