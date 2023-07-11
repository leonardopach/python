from threading import Thread
from time import sleep


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread("Thread 1", 5)
t1.start()

t2 = MeuThread("Thread 2", 3)
t2.start()

t3 = MeuThread("Thread 3", 4)
t3.start()


for i in range(10):
    print(i)
    sleep(1)


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=("Ola mundo", 5))
t.start()
