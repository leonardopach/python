import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()


cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 1')

con.commit()

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
con.close()
