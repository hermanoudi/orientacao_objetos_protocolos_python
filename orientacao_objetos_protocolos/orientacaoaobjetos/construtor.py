
class Team:
    """Represents a brasilian team"""
    country = "Brasil"

    def __init__(self, tecnico, goleiros, laterais, zagueiros, meias, atacantes):
        self.tecnico = tecnico
        self.goleiros = goleiros
        self.laterais = laterais
        self.zagueiros = zagueiros
        self.meias = meias
        self.atacantes = atacantes
        

goleiros = ["Leo Jardim", "Algum da base"]
laterais = ["Puma", "Paulo Henrique", "Leandrinho", "Victor Luiz"]
zagueiros = ["Léo Pelé", "Maicon", "João Victor", "Lyncon"]
meias = ["Sforza", "Coutinho", "Payet", "Cocão", "JP", "Estrela", "Hugo Moura", "Galdames", "Paulinho", "Jair"]
atacantes = ["Ryan", "Veggeti", "David", "Emerson Rodrigues", "Adson", "GB"]
tecnico = "Rafael Paiva"
vasco = Team(tecnico, goleiros, laterais, zagueiros, meias, atacantes) # __init__ (inicializador da classe)


print("#"*50)

print(f"Goleiros: - {vasco.tecnico}")
print(f"Laterais: - {vasco.laterais}")
print(f"Zagueiros: - {vasco.zagueiros}")
print(f"Meias: - {vasco.meias}")
print(f"Atacantes: - {vasco.atacantes}")

