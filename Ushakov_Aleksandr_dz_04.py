def val_checker(lmbd_func):
    def wrapper(func):
        def process(item):
            if lmbd_func(item):
                print(func(item))
            else:
                raise ValueError(f'Wrong Value {item}')
        return process
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


try:
    a = (calc_cube(5))
    b = (calc_cube(-5))
except ValueError as i:
    print(i)
