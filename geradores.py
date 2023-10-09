"""
Geradores 

- Geradores (Generators) são iterator (iteradores)

OBS: O contrario não é verdadeiro, Ou seja, nem todo iterator é generator.

Outras informações


# Exemplo Generator function

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# yield = retorna o contador
gen = conta_at(5)
#print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



# Exemplo Generator function

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_at(10)

for num in gen:
    print(num)

    

# Exemplo Generator function

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_at(10)

print(next(gen))
print(" ")

for num in gen:
    print(num)



"""
# Exemplo Generator function

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = list(conta_at(10))

print(gen)
