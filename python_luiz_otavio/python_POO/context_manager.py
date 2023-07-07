class MyOpen():
    def __init__(self, caminho_arquivo, modo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.caminho_arquivo, self.modo)
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print("fechando aquivo")
        self._arquivo.close()
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # return True


with MyOpen("arquivo_context_manager.txt", 'w') as arquivo:
    arquivo.write("Linha 1 \n")
    arquivo.write("Linha 2 \n")
    arquivo.write("Linha 3 \n")
    print("with", arquivo)
