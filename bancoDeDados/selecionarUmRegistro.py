from db import nova_conexao

sql = "SELECT telefone, nome FROM contatos"


with nova_conexao() as conexao:
    cursor = conexao.cursor(buffered=True)
    cursor.execute(sql)

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
