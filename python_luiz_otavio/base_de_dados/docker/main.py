import os

import dotenv
import pymysql

dotenv.load_dotenv()
TABLE_NAME = "customers"
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

print(os.environ['MYSQL_USER'])
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        print(cursor)
        # Limpa a tabela
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()
    # Inserindo um valor
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) '
               'VALUES '
               '(%s, %s) ')

        data = ("Lucas", 25)
        cursor.execute(sql, data)
    connection.commit()

    # Inserindo um valor dict
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) '
               'VALUES '
               '(%(name)s, %(age)s) ')

        data2 = {'name': 'Dicionario', 'age': 100}
        cursor.execute(sql, data2)
    connection.commit()

    # Inserindo um valor interador dict
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) '
               'VALUES '
               '(%(name)s, %(age)s) ')

        data3 = (
            {'name': 'Dicionario', 'age': 140},
            {'name': 'Caderno', 'age': 150},
            {'name': 'Lapis', 'age': 103},
            {'name': 'Caneta', 'age': 120},
        )
        cursor.executemany(sql, data3)
    connection.commit()

    # Inserindo um valor interador tuple
    with connection.cursor() as cursor:
        sql = (f'INSERT INTO {TABLE_NAME} '
               '(nome, idade) '
               'VALUES '
               '(%s, %s) ')

        data4 = (
            ('Siri', 14),
            ('Helena', 50),
        )
        cursor.executemany(sql, data4)
    connection.commit()

    # SELECT
    with connection.cursor() as cursor:
        sql = (f'SELECT * FROM {TABLE_NAME} ')
        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)
        for row in cursor.fetchall():
            _id, name, age = row
            print(_id, name, age)
    connection.commit()
