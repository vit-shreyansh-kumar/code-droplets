
def get_time(func):

    def inner_calc(*args,**kwargs):

        import datetime
        before_execution = datetime.datetime.now()
        x = func(*args,**kwargs)
        after_execution = datetime.datetime.now()

        time_taken = after_execution - before_execution

        print("Time taken {}".format(time_taken))
        return x
    return inner_calc

@get_time
def function(stuff):
    import time
    time.sleep(3)

function(1)


def outer_decorator(*outer_args, **outer_kwargs):
    def decorator(fn):
        def decorated(*args, **kwargs):
            # (*outer_args, **outer_kwargs)
            return fn(*args, **kwargs)

        return decorated

    return decorator


@outer_decorator(1, 2, 3)
def foo(a, b, c):
    print(a)
    print(b)
    print(c)


foo()