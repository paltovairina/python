class StorageOfOfficeEquipment:
    """
    Класс,описывающий склад оргтехники
    """

    def __init__(self, storage_dict):
        self.storage_dict = dict(storage_dict)

    @staticmethod
    def s_o_o_f():
        print("Склад оргтехники")


class OfficeEquipment:
    def __init__(self, brand, model, color, number):
        self.brand = brand
        self.model = model
        self.color = color
        self.number = number


class Printer(OfficeEquipment):
    def __init__(self, brand, model, color, number, type_printer):
        super().__init__(brand, model, color, number)
        self.type_printer = type_printer

    def __str__(self):
        return f"Тип оргтехники:{__class__.__name__},производитель:{self.brand},модель:{self.model},цвет:{self.color}," \
               f"количество:{self.number},тип устройства:{self.type_printer}"


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, color, number, type_scanner):
        super().__init__(brand, model, color, number)
        self.type_scanner = type_scanner

    def __str__(self):
        return f"Тип оргтехники:{__class__.__name__},производитель:{self.brand},модель:{self.model},цвет:{self.color}," \
               f"количество:{self.number},тип устройства:{self.type_scanner}"


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, color, number, type_xerox):
        super().__init__(brand, model, color, number)
        self.type_xerox = type_xerox

    def __str__(self):
        return f"Тип оргтехники:{__class__.__name__},производитель:{self.brand},модель:{self.model},цвет:{self.color}," \
               f"количество:{self.number},тип устройства:{self.type_xerox}"


p = Printer("Canon", "123", "чёрный", "100 шт.", "струйный")
p2 = Printer("HP", "456", "серый", "50 шт.", "лазерный")
print(p.__str__())
print(p2.__str__())
