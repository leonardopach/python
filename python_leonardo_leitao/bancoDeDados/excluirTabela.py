from db import nova_conexao
from mysql.connector import ProgrammingError

delete_contato = """
    DROP TABLE IF EXISTS contatos
      """
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(delete_contato)
        except ProgrammingError as e:
            print(f"Erro: {e.msg}")
except ProgrammingError as e:
    print(f"Erro conexao: {e.msg}")
