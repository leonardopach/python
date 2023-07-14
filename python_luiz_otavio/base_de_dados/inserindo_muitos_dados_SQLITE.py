import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# Registrar valores nas colunas da tabela
sql = (f'INSERT INTO {TABLE_NAME} (name, weight)'
       'VALUES (?, ?)')

cursor.executemany(sql, (
    ("silva", 4),
    ('luiz', 5)
)
)
# usando dicionario
sql_dict = (f'INSERT INTO {TABLE_NAME}'
            '(name, weight)'
            'VALUES (:name, :weight)')

cursor.execute(sql, {'name': 'silva', 'weight': 4})

con.commit()

cursor.close()
con.close()
