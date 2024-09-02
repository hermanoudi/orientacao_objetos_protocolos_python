from optparse import Option
from typing import Union, List, Any, Optional

# type_aliases
OptionalMessage = Optional[Union[int, str, List]]

def imprime_mensagem(msg: int | str | List | None) -> None:
    print(msg)


imprime_mensagem("Hermano")
imprime_mensagem(123)
imprime_mensagem([1,2,3])
#imprime_mensagem(3.2) #Não é aceito, o mypy apresenta erro.

# Antes do Python 3.9
def function(arg: Optional[Set[int]]):
    ...

# Depois do Python 3.9
def function(arg: set[int] | None):
    ...
