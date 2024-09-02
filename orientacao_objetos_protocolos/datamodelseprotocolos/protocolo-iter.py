# Protocolos / Data Model

# Iterable -  __iter__()
class Cor(): # Base Class

    def __str__(self): # como o toString() do java.
        return self.icon
    
    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"

class Azul(Cor):
    english_name = "blue"
    icon = "🟦"

class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"

class Laranja(Cor):
    english_name = "orange"
    icon = "🟧"

class Verde(Cor):
    english_name = "green"
    icon = "🟩"

class Violeta(Cor):
    english_name = "purpple"
    icon = "🟪"

# Iterable
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in self._cores])


rgb = Paleta(Vermelho(), Verde(), Azul())
for cor in rgb:
    print(cor)
