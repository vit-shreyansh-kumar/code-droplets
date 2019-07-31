

class Iterator:

    def __init__(self,stop):
        self.stop = stop

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):

        if self.start < self.stop:
            self.start += 1

        return self.start - 1


if __name__ == "__main__":

    list = [1,2,3,4,5,6,7]

    iterate = Iterator(10)
    for x in iterate:
        print(x)