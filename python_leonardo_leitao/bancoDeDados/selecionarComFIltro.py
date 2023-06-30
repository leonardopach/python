from db import nova_conexao

sql = "SELECT * FROM contatos WHERE nome  like 'Ga%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for contato in cursor:
        print(contato)
