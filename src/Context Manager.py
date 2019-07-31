__about__ = """ Custom Context Manager. """


class ContextManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open = open(self.filename,self.mode)
        return self.open

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open.close()


if __name__ == "__main__" :

    with ContextManager('myfile', "w+") as manager:

        manager.write("Hey Bro ")
