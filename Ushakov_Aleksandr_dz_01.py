class TrafficLight:
    color = ''

    def running(self):
        colors = {'Красный': 4, 'Желтый': 2, 'Зеленый': 3}
        for color, seconds in colors.items():
            print(f'{color}, {seconds} сек')


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
