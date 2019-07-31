import abc


class Base(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def value(self):
        return "To be overridden."


class Implementation(Base):

    @property
    def value(self):
        return "Concrete Implementation."


if __name__ == "__main__":
    b = Base()
    print("Base.value:", b.value)

    i = Implementation()
    print("Implementation.value:",i.value)