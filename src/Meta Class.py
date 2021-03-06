__about__ = """
                A metaclass is a class whose instances are classes. 
                Like an "ordinary" class defines the behavior of the instances of the class, 
                a metaclass defines the behavior of classes and their instances.
            """

__usage__ = """
                logging and profiling
                interface checking
                registering classes at creation time
                automatically adding new methods
                automatic property creation
                proxies
                automatic resource locking/synchronization.
            """


class Metas(object):

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


a = Metas()

a(1, 2, 3)

