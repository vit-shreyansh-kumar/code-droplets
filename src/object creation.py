
__about__ = """ Object Creation in Python """

class A:
    def whereiam(self):
        print("I am S")

class B:
    def whoiam(self):
        print("I am Shreyansh")


class C(A,B):
    pass

class D(C,B):
    pass


if __name__ == "__main__":

    # c = D()
    print(dir())
    # print(dir(c))





