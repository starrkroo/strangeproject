#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('token.db')
cursor = conn.cursor()

token = 'acc8e91b6ecb6a0f1f6faf9a88ed741afd1be17f3c8cf5118c8f5f97f9668c18027c7513ecc6ce4e09866'

cursor.execute("""CREATE TABLE IF NOT EXISTS ttoken (
	name VARCHAR(85)
)
 """)

# query = """INSERT INTO python_group (name) VALUES (?)"""
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Амир')""")
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Исамутдин')""")
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Марат')""")
cursor.executemany("""INSERT INTO ttoken (name) VALUES (?)""", [((token),)])

conn.commit()
cursor.close()
conn.close()