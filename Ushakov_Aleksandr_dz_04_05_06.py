class Stockroom:
    eqip_dict = {}
    eqip_count = {}

    def add_eqip(self, eqip, i=1):
        try:
            if isinstance(i, int):
                print(f'{eqip.eqip_type} в кол-ве {i} шт. поступил на склад.')
                while i:
                    self.eqip_dict.setdefault(eqip.eqip_type, []).append(eqip)
                    self.eqip_count.setdefault(eqip.eqip_type, 0)
                    self.eqip_count[eqip.eqip_type] += 1
                    i -= 1
            else:
                raise ValueError
        except ValueError:
            print('Операция невозможна.')

    def to_shop(self, eqip, i=1):
        try:
            if isinstance(i, int):
                print(f'{eqip.eqip_type} в кол-ве {i} шт. отправлен в магазин.')
                while i:
                    self.eqip_dict[eqip.eqip_type].remove(eqip)
                    self.eqip_count[eqip.eqip_type] -= 1
                    i -= 1
            else:
                raise ValueError
        except ValueError:
            print('Операция невозможна.')


class OfficeEquipment:
    def __init__(self, eqip_type, paper_format, brand, serial_number):
        self.eqip_type = eqip_type
        self.paper_format = paper_format
        self.brand = brand
        self.serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, eqip_type, paper_format, technology_of_print, brand, serial_number):
        super().__init__(eqip_type, paper_format, brand, serial_number)
        self.technology_of_print = technology_of_print


class Scaner(OfficeEquipment):
    def __init__(self, eqip_type, paper_format, sensor_type, brand, serial_number):
        super().__init__(eqip_type, paper_format, brand, serial_number)
        self.sensor_type = sensor_type


class Xerox(OfficeEquipment):
    def __init__(self, eqip_type, paper_format, resolution, brand, serial_number):
        super().__init__(eqip_type, paper_format, brand, serial_number)
        self.resolution = resolution


printer = Printer('Printer', 'A4', 'Laser Print', 'HP', 'Laser107w')
scaner = Scaner('Scaner', 'A4', 'CIS', 'Canon', 'P-215II')
xerox = Xerox('Xerox', 'A4', '600x600', 'Xerox', 'B215')
stockroom = Stockroom()
stockroom.add_eqip(xerox)
stockroom.add_eqip(scaner)
stockroom.add_eqip(printer, 3)
stockroom.to_shop(printer, '3')
print(stockroom.eqip_count)
stockroom.to_shop(printer, 2)
print(stockroom.eqip_count)
