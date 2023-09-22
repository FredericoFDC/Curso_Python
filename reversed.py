"""
Reversed

Não confunda com a função reserve() que estudamos em listas.

A função reverse() só funciona na lista.

Já a função reversed() funciona com qualquer iterável.

A função reversed() retorna um iterável chamado list reverser iterator

"""
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto.

# Lista.
print(list(reversed(lista)))

# Tuple.
print(tuple(reversed(lista)))

# Conjunto.
print(set(reversed(lista))) # Set não define ordem

print('\n')

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end=' ')

print('\n')
# Podemos fazer o mesmo sem o uso do for

print(' '.join(list(reversed('Geek University'))))

print('\n')

# Ja vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])

print('\n')

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end= ' ')

print('\n')

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n, end= ' ')
