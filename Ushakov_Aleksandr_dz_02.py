def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_list = 0
    indx = 0
    while indx < len(dataset):
        begin = 0
        num = dataset[indx]
        while num != 0:
            begin = begin + num % 10
            num = num // 10
        if begin % 7 == 0:
            sum_list = sum_list + dataset[indx]
        indx = indx + 1
    return sum_list  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    new_list = [x + 17 for x in dataset]
    sum_list = 0
    indx = 0
    while indx < len(new_list):
        begin = 0
        num = new_list[indx]
        while num != 0:
            begin = begin + num % 10
            num = num // 10
        if begin % 7 == 0:
            sum_list = sum_list + new_list[indx]
        indx = indx + 1
    return sum_list  # Верните значение полученной суммы


my_list = [i**3 for i in range(1, 1001, 2)]  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)