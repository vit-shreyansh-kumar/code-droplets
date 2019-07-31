
__about__ = """

Python's convention to make an instance variable protected is to add a prefix _  (single underscore) to it.
This effectively prevents it to be accessed, unless it is from within a sub-class.

"""


class Employee:
    def __init__(self, name , designation):

        self._name = name   #Protected Attribute
        self._designation = designation  #Protected Attribute


# class NewEmployee(Employee):
#     def __init__(self,name,designation):
#         super().__init__(name,designation)


if __name__ == "__main__":

    obj = Employee("Shreyansh Kumar", "Developer")
    print(obj._name)
    print(obj._designation)