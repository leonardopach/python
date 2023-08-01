from calculadora import somar

try:
    print(somar(2, 6))
except AssertionError as e:
    print(f"Conta inválida: {e}")
