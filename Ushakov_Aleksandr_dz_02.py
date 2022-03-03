class Road:
    def __init__(self, length: int, width: int):
        """
        Конструктор класса
        :param length: длина в метрах
        :param width: ширина в метрах
        """
        self.lenght = length
        self.width = width

    def calculate(self, height: int = 5, mass_m_2: int = 25):
        """
        Считает массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param hight: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: int значение тонн, дробная часть если есть не учитывается
        """
        mass = self.lenght * self.width * height * mass_m_2
        return mass


if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')
