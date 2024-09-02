# Protocolos / DataModel

# Addible - __add__ / __radd__

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


print("Cores primarias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print(amarelo, azul, vermelho)

print("Cores secundarias")
print("Amarelo + Vermelho: ", amarelo + vermelho) # Tipagem Forte
print("Azul + Amarelo: ", azul + amarelo)
print("Vermelho + Azul: ", vermelho + azul)
