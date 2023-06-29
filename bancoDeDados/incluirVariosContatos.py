from db import nova_conexao
from mysql.connector import ProgrammingError

sql = "INSERT INTO contatos (nome, telefone) VALUES(%s, %s)"
args = (
    ("Gabriela", "91234123"),
    ("Silva", "32"),
    ("Roberta", "12"),
    ("Sabrina", "23"),
    ("Nicolas", "543"),
    ("Jessica", "43"),
    ("Guilherme", "123"),
)
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f"Error :{e.msg}", )
        else:
            print(f"{cursor.rowcount} Registro incluido")
except ProgrammingError as e:
    print(f"Error :{e.msg}", )
