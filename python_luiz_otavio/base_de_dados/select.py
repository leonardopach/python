import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()


cursor.execute(f"SELECT id, name, weight FROM {TABLE_NAME}")

row = cursor.fetchone()
print(row)
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
con.close()
