import re


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        nums = re.findall(r'\d+', date)
        date_num = [int(i) for i in nums]
        Date.valid_num(date_num)

    @staticmethod
    def valid_num(date):

        day, month, year = date[0], date[1], date[2]
        if (0 < day <= 31) and (0 < month <= 12) and (0 < year <= 3000):
            print(f'{day:02}, {month:02}, {year}')
        else:
            print('Неверно введена дата')


Date.date_to_int('13-03-2022')
Date.date_to_int('40-14-8000')
