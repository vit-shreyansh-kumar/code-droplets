
class MyDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        self.func(*args, **kwargs)
        print("Function Executed")
        print("\n")

@MyDecorator
def function():
    print("SHREYANSH KUMAR")



if __name__ == "__main__":

    function()