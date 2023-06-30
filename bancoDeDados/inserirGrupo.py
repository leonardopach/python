from db import nova_conexao
from mysql.connector import ProgrammingError

sql = "INSERT INTO grupos ( descricao) VALUES( %s)"
args = (
    ("Um descrição",),
    ("duas descrição",),
    ("três descrição",),
    ("Quatro descrição",),
    ("Cinco descrição",),
    ("Seis descrição",),
    ("Sete descrição",),
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
