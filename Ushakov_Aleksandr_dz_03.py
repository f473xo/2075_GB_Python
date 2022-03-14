class Number:
    def __init__(self, num):
        self.num = num

    @classmethod
    def num_to_list(cls):
        list = []
        while True:
            try:
                get_num = input('Введите число. Для завершения работы и вывода результата введите end - ')
                if get_num == 'end':
                    return list
                elif get_num.isdigit():
                    list.append(get_num)
                else:
                    raise ValueError
            except ValueError:
                print('Вводите только числа.')


a = Number.num_to_list()
print(a)
