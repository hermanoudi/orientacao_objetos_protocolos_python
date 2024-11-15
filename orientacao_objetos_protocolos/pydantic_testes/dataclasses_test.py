from pydantic.dataclasses import dataclass
from pydantic import StrictInt

@dataclass
class Pessoa:
    nome: str
    idade: StrictInt


print(Pessoa(nome="Hermano", idade=29))
