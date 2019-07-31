

class A:

    cla = 100

    def __init__(self):
        print("Init Value:",self.cla)


    def __new__(cls, *args, **kwargs):
        print("Call Value :",cls.cla)




if __name__ == "__main__":
    abc =A()
    print(abc.cla)
