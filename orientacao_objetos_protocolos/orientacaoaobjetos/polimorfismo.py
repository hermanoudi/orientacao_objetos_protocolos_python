# Polimorfismo
# Capacidade de um implementação se comportar de maneira similar independente da forma do objeto
from abc import ABC

class Dog:
    def make_sound(self):
        return "woof woof"

class Cat:
    def make_sound(self):
        return "meow meow"

def print_sound(obj):
    if not hasattr(obj, "make_sound"):
        raise ValueError(f"{obj} is not Soundable")
    print(obj.make_sound())


rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)


### Novo Exemplo ###
class Person(ABC):
    ...

class PhisicalPerson(Person):
    def validate_document(self):
        return "validated to phisical"


class JuridicPerson(Person):
    def validate_document(self):
        return "validated to Juridic"


def check_validate_document(obj):
    if not hasattr(obj, "validate_document"):
        raise ValueError("Object is not Validatable")
    print(obj.validate_document())

hermano = PhisicalPerson()
check_validate_document(hermano)

moura_fund = JuridicPerson()
check_validate_document(moura_fund)

beltrano = Person()
check_validate_document(beltrano)
