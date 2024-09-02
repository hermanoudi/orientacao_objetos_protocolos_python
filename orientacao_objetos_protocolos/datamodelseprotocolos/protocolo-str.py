# protocolos / Data model
# Printable

class Cor(): # Base Class
    english_name = "color"
    icon = "⬜"

    def __str__(self): # como o toString() do java.
        return f"{self.english_name} - {self.icon}"

class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"

class Azul(Cor):
    english_name = "blue"
    icon = "🟦"

class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"


print("Cores primarias")
obj = Amarelo()

new = str(obj) # casting
print(new)

print(Amarelo())
print(Azul())
print(Vermelho())
