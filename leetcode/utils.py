from time import perf_counter

def time_it(function):
    def inner(*args, **kwargs):
        start = perf_counter()
        response = function(*args, **kwargs)
        end = perf_counter()
        print(f"{function.__name__} took {(end-start)} ms")
        return response
    return inner
