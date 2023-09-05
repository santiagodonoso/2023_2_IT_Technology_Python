import sqlite3

db = sqlite3.connect("database.sqlite")
q = "DELETE FROM users WHERE id = ?" # ? is a placeholder
db.execute(q, ("36f71ec6-9b05-4994-8b94-8a871c3c1bbf",))
db.commit()










