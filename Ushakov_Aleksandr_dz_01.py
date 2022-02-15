def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные числа от 1 до number (включительно)"""
    for i in range(1, n+1, 2):
        yield i


n = 15
generator = odd_nums(n)
for el in generator:
    print(el)
