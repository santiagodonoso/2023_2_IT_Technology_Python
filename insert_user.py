import sqlite3
import uuid

# Cast <class 'uuid.UUID'> to string
id = str(uuid.uuid4()) # <class 'str'>
print(id)
print(type(id))
db = sqlite3.connect("database.sqlite")
q = "INSERT INTO users VALUES(?, ?)"
db.execute(q, (id, 'D'))
db.commit()





















