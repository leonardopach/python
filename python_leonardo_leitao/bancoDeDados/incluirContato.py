from db import nova_conexao
from mysql.connector import ProgrammingError

sql = "INSERT INTO contatos (nome, telefone) VALUES(%s, %s)"
args = ("Gabriela", "91234123")
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f"Error :{e.msg}", )
        else:
            print("1 Registro incluido id: ", cursor.lastrowid)
except ProgrammingError as e:
    print(f"Error :{e.msg}", )
