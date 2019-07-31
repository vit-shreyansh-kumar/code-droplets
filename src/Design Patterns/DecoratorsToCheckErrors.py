
class CheckForErrors:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):

        print([isinstance(j, str) for j in params])

        if any([isinstance(i, str) for i in params]):
            raise TypeError(" Parameter Cannot be a String !!.")

        else:
            return self.function(*params)

@CheckForErrors
def add_numbers(*numbers):
    return sum(numbers)


print(add_numbers(3, 0))
