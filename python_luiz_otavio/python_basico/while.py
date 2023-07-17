qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"{linha = }, {coluna = }")
        coluna += 1
    linha += 1


nome = "Leonardo pacheco"

contador = 0
novo_nome = ""
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f"*{letra}"
    contador += 1

print(novo_nome)
