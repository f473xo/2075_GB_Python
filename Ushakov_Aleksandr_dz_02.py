class Division(Exception):
    def __init__(self, num):
        self.num = num


a = input('Введите число которое хотите разделить - ')
b = input('Введите число на котрое будете делить - ')
try:
    a = float(a)
    b = float(b)
    if b != 0:
        print(round(a / b, 2))
    else:
        raise Division('Нельзя делить на 0!')
except Division as err:
    print(err)
