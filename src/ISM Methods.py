__about__ = """

            Instance Method,
            Static Method,
            Class Method.
            
            """


class Shreyansh:

    def __init__(self):
        print("Shreyansh Initialised")

    @staticmethod
    def mydump():
        print("I am in My Dump. ")

    @classmethod
    def mynewdump(cls):
        print("I am in My New Dump. ")


if __name__ == "__main__":

    abc = Shreyansh()
