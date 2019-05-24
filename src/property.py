__about__ = """ I mplementing property. """


class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):

        self.fullname = "{} {}".format(self.fname,self.lname)
        return self.fullname

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return "{}.{}@nagarro.com".format(self.fname, self.lname)


if __name__ == "__main__" :


    emp_object = Employee('shreyansh','kumar')
    emp_object.fname = "sushant"
    emp_object.fullname = "sushant sinha"

    print(emp_object.fname)
    print(emp_object.lname)
    print(emp_object.email)
