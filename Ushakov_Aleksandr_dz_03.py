def type_logger(func):
    def wrapper(*args):
        item = func(*args)
        for el in args:
            i = f'{el}:{type(el)}'
            print(i)
        return item
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
