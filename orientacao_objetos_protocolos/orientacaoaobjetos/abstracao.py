# Abstração
class Person:
    kingdom = "animalia"


class Fruit:
    kingdom = "vegetalia"


class Animal:
    kingdom = "animalia"


Hermano = Person()
print(Hermano.kingdom)

apple = Fruit()
print(apple.kingdom)

dog = Animal()
print(dog.kingdom)
