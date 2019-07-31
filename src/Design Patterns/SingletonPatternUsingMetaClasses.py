
__about__ = """ To restrict the creation of an object. """


class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args,**kwargs)
            return cls._instance[cls]
        else:
            return cls._instance[cls]


class MySubclass(metaclass=Singleton):

    def __init__(self, value):
        print("Called for Initialization")
        print(value)


if __name__ == "__main__":

    a = MySubclass(1)
    b = MySubclass(2)
    c = MySubclass(3)

    print(" A Object:", a)
    print(" B Object:", b)
    print(" C Object:", c)

