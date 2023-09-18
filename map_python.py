'''
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
       calcula a área de um círculo com raio r 
    return math.pi * (r ** 2)
print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um interável

areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com lambda

print(list(map(lambda r: math.pi + (r **2), raios)))

'''
# Para fixar - Map

# Temos dados iteráveis:
# Dados: a1, a2, ...... an
# Temos um função:
# Função: f(x)
# Utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função
# O map object: f(a1), f(a2), ..... f(an)

# Mais exemplos


