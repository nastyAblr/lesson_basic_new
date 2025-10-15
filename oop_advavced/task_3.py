"""
Создайте класс Plants, унаследуйте class Tree, Grass, Bush(Кустарник).
Продумайте и реализуйте логику всех классов.
"""


class Plants:
    def __init__(self, name, height_cm, is_flowering):
        self.name = name
        self.height_cm = height_cm
        self.is_flowering = is_flowering

    def photosynthesize(self):
        return f"{self.name} осуществляет фотосинтез."

    def grow(self, cm):
        self.height_cm += cm
        return f"{self.name} вырос на {cm} см. Текущая высота: {self.height_cm} см."


class Tree(Plants):
    def __init__(self, name, height_cm, is_flowering, age, has_fruits):
        super().__init__(name, height_cm, is_flowering)
        self.age = age
        self.has_fruits = has_fruits

    def shed_leaves(self):
        return f"{self.name} сбрасывает листья осенью."

    def bear_fruits(self):
        if self.has_fruits:
            return f"{self.name} приносит плоды."
        else:
            return f"{self.name} не плодоносит."


class Grass(Plants):
    def __init__(self, name, height_cm, is_flowering, lawn_type):
        super().__init__(name, height_cm, is_flowering)
        self.lawn_type = lawn_type  # например: декоративный, спортивный

    def mow(self):
        self.height_cm = max(0, self.height_cm - 5)
        return f"{self.name} пострижена. Текущая высота: {self.height_cm} см."


class Bush(Plants):
    def __init__(self, name, height_cm, is_flowering, berry_type=None):
        super().__init__(name, height_cm, is_flowering)
        self.berry_type = berry_type  # если куст плодоносит ягодами

    def prune(self):
        self.height_cm = max(0, self.height_cm - 10)
        return f"{self.name} обрезан. Текущая высота: {self.height_cm} см."

    def harvest_berries(self):
        if self.berry_type:
            return f"С куста {self.name} собраны ягоды: {self.berry_type}."
        else:
            return f"{self.name} не приносит ягод."


oak = Tree("Дуб", 500, False, 50, False)
print(oak.photosynthesize())
print(oak.shed_leaves())
print(oak.bear_fruits())

rye_grass = Grass("Райграс", 30, True, "спортивный")
print(rye_grass.grow(5))
print(rye_grass.mow())

blackberry = Bush("Ежевика", 100, True, "ежевика")
print(blackberry.harvest_berries())
print(blackberry.prune())
