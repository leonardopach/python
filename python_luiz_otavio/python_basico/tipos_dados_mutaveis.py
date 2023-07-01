valorA = "Leonardo"
valorA = "Pedro"
print(id(valorA))

listaA = ["Silva", "Lucas"]
listaB = listaA
listaC = listaA.copy()

listaB[0] = "Valor"
print(id(listaA), id(listaB), id(listaC))
print(listaA, listaB)
print(listaC)
