

class Computer:

    def __init__(self,name,size):
        self.brand = name
        self.size = size


class Laptop(Computer):

    def __init__(self,name,size,model):

        super().__init__(name,size)
        self.model = model


if __name__ == "__main__":

    abc = Laptop('MSI','15.6','GL Series')

    print("Name: {}".format(abc.brand))
    print("Size: {}".format(abc.size))
    print("Model: {}".format(abc.model))