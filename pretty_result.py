def pretty_result(original_function):
    def wrapper(*args):
        ans = original_function(*args)
        pretty = "The result of the function '{}' is: {}".format(original_function.__name__, ans)
        return pretty
    return wrapper

@pretty_result
def adder(a, b):
    return a + b

print(adder(3,4))