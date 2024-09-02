from dataclasses import dataclass

@dataclass
class Pessoa:
    pk: str
    name: str
    points: int


def funcao(dados: Pessoa):
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

funcao(dados)

print(dados.name)
