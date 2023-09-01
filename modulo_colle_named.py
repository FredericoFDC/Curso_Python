"""
Módulo Collections - Named Tuple

# Recaptulando tuplas

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple - São tuplas diferenciadas onde, especificamos um nome para a mesma e também
parâmetros.

"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple.

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple.

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple.

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando.
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados forma 1.

print(ray[0])
print(ray[1])
print(ray[2])

# Acessando os dados forma 2.

print(ray.idade)
print(ray.raca)
print(ray.nome)


print(ray.index('Chow-Chow')) # Index = qual posição do index.
print(ray.count('Chow-Chow')) # Count = quantas vezes se repete.
