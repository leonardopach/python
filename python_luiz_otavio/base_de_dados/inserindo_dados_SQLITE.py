import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# Registrar valores nas colunas da tabela
sql = f"INSERT INTO {TABLE_NAME} (name, weight)" "VALUES (?, ?)"

cursor.execute(sql, ["leonardo", 102])
con.commit()

cursor.close()
con.close()
