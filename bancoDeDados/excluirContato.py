from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "DELETE FROM contatos WHERE nome = %s"
args = ("Silva",)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f"Failed to execute {e}")
    else:
        print(f"Successfully {cursor.rowcount}")
