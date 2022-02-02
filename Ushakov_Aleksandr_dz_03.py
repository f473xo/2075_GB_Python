def transform_sring(number: int) -> str:
    if number % 10 == 1 and number != 11:
        print((number), 'процент')
    elif number % 10 == 2 and number != 12 or number % 10 == 3 and number != 13 or number % 10 == 4 and number != 14:
        print((number), 'процента')
    else:
        print((number), 'процентов')

for n in range(1, 101):
    print(transform_sring(n))
# В результате между строк выводиться None, как ни пытался - не могу убрать(