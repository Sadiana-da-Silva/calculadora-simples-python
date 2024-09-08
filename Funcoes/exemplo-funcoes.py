# Com parâmetros e um retorno
def multiplica(numero, multiplicador):
    resultado = numero * multiplicador
    return resultado

print(multiplica(10, 1))
print(multiplica(20, 2))
print(multiplica(30, 3))
print(multiplica(40, 4))

# Sem parâmetros nem retorno
def imprime(texto):
    print("O texto é", texto)

imprime("Joana")