# typing hints

# ass funcao
# def classe
# metodos
#################################
nome = "Hermano"
numero = 42
quantia = 56.3
active = False

# Duck Typing
def soma(a: int,b: int) -> int:
    return a + b

print(soma("Hermano", "Flávio")) # Python não obriga que as anotações sejam exatamente isso que vai ser usado.
