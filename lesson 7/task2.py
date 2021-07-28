from abc import ABC, abstractmethod


class ClothesAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    @property
    def tissue_consumption(self):
        return
        pass


class Clothes(ClothesAbstractClass):
    def __init__(self, coat_size, suit_height):
        self.coat_size = coat_size
        self.suit_height = suit_height

    def abstract_method(self):
        return f"Это абстрактный метод класса {__class__.__name__}"

    @property
    def tissue_consumption(self):
        return f"Для пошива пальто и костюма необходимо затратить " \
               f"{(self.coat_size / 6.5 + 0.5) + (2 * self.suit_height + 0.3)} метра(ов) ткани"


class Coat(Clothes):
    def __init__(self, coat_size, suit_height):
        super().__init__(coat_size, suit_height)
        self.coat_size = coat_size

    def abstract_method(self):
        return f"Это абстрактный метод класса {__class__.__name__}"

    @property
    def tissue_consumption(self):
        return f"Для пошива пальто размера {self.coat_size} необходимо затратить {self.coat_size / 6.5 + 0.5} " \
               f"метра(ов) ткани"


class Suit(Clothes):
    def __init__(self, coat_size, suit_height):
        super().__init__(coat_size, suit_height)
        self.suit_height = suit_height

    def abstract_method(self):
        return f"Это абстрактный метод класса {__class__.__name__}"

    @property
    def tissue_consumption(self):
        return f"Для пошива костюма роста {self.suit_height} необходимо затратить {2 * self.suit_height + 0.3} " \
               f"метра(ов) ткани"


all_tissue = Clothes(coat_size=1, suit_height=1)
coat_tissue = Coat(coat_size=1, suit_height=1)
suit_tissue = Suit(coat_size=1, suit_height=1)
print(coat_tissue.abstract_method())
print(coat_tissue.tissue_consumption)
print(suit_tissue.abstract_method())
print(suit_tissue.tissue_consumption)
print(all_tissue.abstract_method())
print(all_tissue.tissue_consumption)
