import sqlite3

db = sqlite3.connect("database.sqlite")
q = "INSERT INTO users VALUES(?, ?)"
db.execute(q, (1, 'A'))
db.commit()





















