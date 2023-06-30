class RGB:
    def __init__(self):
        self.cores = ["red", "green", "blue", "alpha"][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == "__main__":
    cores = RGB()

    for x in cores:
        print(x)
