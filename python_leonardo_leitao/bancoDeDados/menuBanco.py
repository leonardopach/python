from db import nova_conexao


def Menu(banco):
    sql = "SELECT * FROM contatos WHERE"
    match banco:
        case 1:
            with nova_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(sql)
                for contato in cursor:
                    print(contato)
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case _:
            return '** inválido **'


while True:
    print("Opções do Banco: ")
    print("Consultar  - 1")
    print("Sair  - 5")
    escolha = int(input("Digite um numero: "))
    print(Menu(escolha))
    if escolha == 5:
        break
