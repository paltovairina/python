class Road:
    # атрибуты класса
    _mass_for_meter_road = 25  # масса асфальта для покрытия одного кв.метра дороги асфальтом толщиной в 1см,кг
    _depth_road = 5  # число см толщины полотна

    # методы
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def total_mass_asphalt(self):
        return self._length * self._width * self._mass_for_meter_road * self._depth_road / 1000


road = Road(20, 5000)
print(f"Масса асфальта для покрытия всей дороги - {road.total_mass_asphalt()} тонн(ы)")
