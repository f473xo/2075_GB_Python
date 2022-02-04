from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    prices_list = []
    for price in list_in:
        rubles = int(price)
        pennies = round((price - rubles) * 100)
        price_str = f'{rubles} руб {pennies:02} коп'  # пишет строку и добавляет нули
        prices_list.append(price_str)
    str_out = ', '.join(prices_list)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'Преобразование в строку: {result_1}')


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(f'Остался ли результат result_2 тем же? Ответ: {my_list == result_2}')
print(f'Список с элементами по возрастанию: {result_2}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_3 = sort_price_adv(my_list)
print(f'Список с элементами по убыванию: {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort(reverse=True)
    list_out = list_in[:5]
    return list_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_4 = check_five_max_elements(my_list)
print(f'Пять максимальных значений списка: {result_4}')
