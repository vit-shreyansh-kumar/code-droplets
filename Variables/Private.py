
__about__ = """

    Python's convention to make an instance variable private use __  or double underscore.
    It gives strong suggestion to not to touch it outside the class.
    Any such attempt will result in Attribute Error.

"""

class Employee:
    def __init__(self, name, designation):

        self.__name = name
        self.__designation = designation

if __name__ == "__main__":

    obj = Employee("Shreyansh Kumar", "Artist")
    print(obj.__name)
    print(obj.__designation)