class Car:

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, more_speed=15) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed = more_speed + self.speed
        print(f'Автомобиль {self.name} повысил скорость на 15 км/ч. Текущая скорость: {self.speed} км/ч')

    def stop(self, speed=0) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = speed
        print(f'Автомобиль {self.name} остановился. Скорость {self.speed} км/ч.')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction in ('направо', 'налево', 'прямо', 'назад'):
            print(f'Автомобиль {self.name} движется {direction}')
        else:
            raise ValueError(f'Нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        print(f'Скорость автомобиля {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость превышена!')


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена более чем в 3 раза! Куда летишь, родной, тебя дома ждут!')


class PoliceCar(Car):
    def show_speed(self, is_police=True):
        super().show_speed()
        if self.speed > 60:
            print(f'Вруби мигалку и забудь про скорость!')


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'Gazel')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()
    town_car.show_speed()
    work_car.show_speed()
    town_car.stop()
    police_car.show_speed()
    sport_car.show_speed()
    sport_car.turn('назад')
    sport_car.turn('направо')
