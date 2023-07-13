import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# SQL


cursor.close()
con.close()
