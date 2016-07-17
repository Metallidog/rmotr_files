def small_numbers(limit = 50):
    def decorate(function):
        def wrapper(*args):
            if any(map(lambda num: num>limit, (n for n in args if isinstance(n, float) or isinstance(n, int)))):
                raise ValueError()
            return (function(*args))
        return wrapper
    return decorate

@small_numbers(limit=100)
def f1(a_str, a_float):
    return 'mock1 - {} {}'.format(a_str, a_float)

@small_numbers(limit=50)
def f2(an_int, a_str):
    return 'mock2 - {} {}'.format(an_int, a_str)

f1('world', 100)
f2('hello', 51)
