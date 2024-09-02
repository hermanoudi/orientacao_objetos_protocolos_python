from typing import Union, List, Any, Optional

# type_aliases
OptionalMessage = Optional[Union[int, str, List]]

def imprime_mensagem(msg: OptionalMessage = None) -> None:
    print(msg)


imprime_mensagem("Hermano")
imprime_mensagem(123)
imprime_mensagem([1,2,3])
imprime_mensagem(3.2) #Não é aceito, o mypy apresenta erro.
