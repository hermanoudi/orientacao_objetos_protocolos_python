
# Herança # Capacidade de herdar outras classes

from abc import ABC


class Fruit(ABC): # classe abstrata / superclass
    kingdom = "vegetalia"


class Food(ABC):
    price = 4.5


class Apple(Fruit, Food): # Herança em uma classe material #Herança Multipla #mixins
    internal_color = "white"


class RedApple(Apple):
    external_color = "red"


class GreenApple(Apple):
    external_color = "green"


class MinhaMacaQueEstaSobreAMesa(GreenApple):
    ...


minha_maca = MinhaMacaQueEstaSobreAMesa()
print(minha_maca.external_color)
print(minha_maca.internal_color)
print(minha_maca.kingdom)
print(minha_maca.price)
