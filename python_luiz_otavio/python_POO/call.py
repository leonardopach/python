class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(f"{nome} está chamando ", self.phone)


call1 = CallMe("1234123")
call1("Leonardo")
