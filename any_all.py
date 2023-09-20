"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável
está vazio.

# Exemplo all()
print(all([0, 1, 2, 3, 4, 5])) # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4, 5])) # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes)) # True
nomes = ['Carlos', 'Camila', 'Carla', 'Cristina','Daniel']
print(all(nome[0] == 'C' for nome in nomes)) # False


# OBs : Um intrável vazio convertido em boolean é false , mas o alt() entende como true

print(all([letra for letra in 'eio' if letra in 'aeiou']))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

Any() -> Retorna true se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio
retorna False

print(any([0, 1, 2, 3, 4, 5])) # Retorna True
print(any([0, False, {}, {}, {}, False])) # Retorna False
print(any([0, False, {}, 1, {}, False])) # Retorna True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
"""

