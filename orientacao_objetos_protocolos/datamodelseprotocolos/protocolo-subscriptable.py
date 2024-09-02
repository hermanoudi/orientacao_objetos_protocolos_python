# Protocolos / Data Model
# Collection - Sized + Container + Iterable

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

    def __len__(self):
        return 4

class Azul(Cor):
    english_name = "blue"
    icon = "🟦"

    def __len__(self):
        return 1

class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"

    def __len__(self):
        return 3

class Laranja(Cor):
    english_name = "orange"
    icon = "🟧"

    def __len__(self):
        return 2

class Verde(Cor):
    english_name = "green"
    icon = "🟩"

    def __len__(self):
        return 6


class Violeta(Cor):
    english_name = "purpple"
    icon = "🟪"

# Iterable
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in self._cores])

    # Container - __contains__ -> bool    
    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]
    
    #sized - 
    def __len__(self):
        return len(self._cores)
    
    #subscriptable
    def __getitem__(self, item):
        if isinstance(item, (int, slice)): #0, 2:4
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor

rgb = Paleta(Vermelho(), Verde(), Azul())

print(rgb[2])
print(rgb["vermelho"])
