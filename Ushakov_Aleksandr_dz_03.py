class Cell:
    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        i = '\n'.join(['*' * number for _ in range(self.cells // number)])
        return f'{i}\n{"*" * (self.cells % number)}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells >= other.cells:
            return Cell(self.cells - other.cells)
        raise ValueError('Недопустимая операция')

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Действие допустимо только для экземпляров того же класса')
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        try:
            return Cell(self.cells // other.cells)
        except ZeroDivisionError:
            print('Деление на ноль недопустимо')

    def __floordiv__(self, other):
        try:
            return Cell(self.cells // other.cells)
        except ZeroDivisionError:
            print('Деление на ноль недопустимо')


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)
    print(cell_1.make_order(10))

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)
    try:
        cell_1 * 123
    except TypeError as err:
        print(err)
