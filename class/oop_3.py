"""
Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные):

title: "Мороженое"

weight: 154

tp: "Еда"

price: 1024

Затем, после объявления класса, измените его атрибут price
на значение 2048 и добавьте еще один атрибут:

inflation: 100


"""


class Goods:

    def __init__(self, title, weight, tp, price):
        self.title = title
        self.weight = weight
        self.tp = tp
        self.price = price


good_1 = Goods('мороженное', '154', 'еда', '1024')
print(good_1.__dict__)

setattr(good_1, 'price', 2048)
print(good_1.price)

setattr(Goods, 'inflation', 100)
print(Goods.inflation)