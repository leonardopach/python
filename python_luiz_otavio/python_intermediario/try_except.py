try:
    b = "0"
    a = 10
    c = a / b
except ZeroDivisionError:
    print("Division error")
except NameError:
    print("Nome B não definido")
except (TypeError, IndexError) as error:
    print(f"{error}")
    print(f"nome: {error.__class__.__name__}")
except Exception as e:
    print(f"Erro: {e}")
finally:
    print("Continua")
