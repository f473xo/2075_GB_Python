class Stationery:
    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуск отрисовки:')


class Pen(Stationery):
    def draw(self):
        print('Pen: приступил к отрисовке объекта "Ручка"')


class Pencil(Stationery):
    def draw(self):
        print('Pen: приступил к отрисовке объекта "Карандаш"')


class Handle(Stationery):
    def draw(self):
        print('Pen: приступил к отрисовке объекта "Маркер"')


start = Stationery()
start.draw()
pen = Pen()
pen.draw()
start.draw()
pencil = Pencil()
pencil.draw()
start.draw()
handle = Handle()
handle.draw()
