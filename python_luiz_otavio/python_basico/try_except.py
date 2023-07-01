try:
    numero_primeiro = input("Digite um valor: ")
    numero_segundo = input("Digite um valor: ")
    calcular = numero_primeiro * numero_segundo
    print(calcular)
except Exception as e:
    print(f"Error: {e}")
