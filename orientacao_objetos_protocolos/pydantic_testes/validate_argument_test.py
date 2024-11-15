from pydantic import validate_call

@validate_call
def soma(x: int, y:int):
    return x + y

#Valida os tipos de entrada no momento na execução
# print(soma("flavio","Hermano"))
print(soma(5,3))
