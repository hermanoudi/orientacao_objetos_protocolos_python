
class Pessoa:
    def __init__(self, pk: str, name: str, points: int):
        self.pk = pk
        self.name = name
        self.points = points


def funcao(dados: Pessoa):
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

funcao(dados)

print(dados.name)
