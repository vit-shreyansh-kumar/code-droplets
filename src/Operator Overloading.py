__about__ = """ 
            Operator Overloading in Python. 
            """


class A:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        print(self.a)
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a


if __name__ == "__main__":
    1 + 2
    ob1 = A(1)
    ob2 = A(2)
    ob3 = A(3)
    ob4 = A(4)
    ob5 = A("Geeks")
    ob6 = A("For")

    print(ob1 + ob2 + ob3 + ob4)
    print(ob5 + ob6)