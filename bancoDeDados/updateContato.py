from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "UPDATE contatos SET nome = %s WHERE id = 13"

with nova_conexao() as conexao:
    try:
        nome = input("Digite um nome: ")
        args = (f"{nome}",)
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f"Failed to execute {e}")
    else:
        print(f"Successfully {cursor.rowcount}")
