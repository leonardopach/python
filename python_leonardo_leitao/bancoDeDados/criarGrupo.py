from db import nova_conexao
from mysql.connector import ProgrammingError

criar_tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT PRIMARY KEY AUTO_INCREMENT,
        descricao VARCHAR(50)
    )
"""

alterar_tabela_contato1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""
alterar_tabela_contato2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(criar_tabela_grupo)
            cursor.execute(alterar_tabela_contato1)
            cursor.execute(alterar_tabela_contato2)
        except ProgrammingError as e:
            print(f"Erro: {e.msg}")
except ProgrammingError as e:
    print(f"Erro conexao: {e.msg}")
