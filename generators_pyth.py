"""
Generators

Não vimos:
- tuple comprehension .... porque elas se chamam Generators

nome = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehesion
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# Qual é a utilidade de getsizeof() -> Retorna a quantidade de bytes
from sys import getsizeof
#Mostra quantos bytes a string 'Geek' está ocupando em memória.
print(getsizeof('Geek'))

"""
# Qual é a utilidade de getsizeof() -> Retorna a quantidade de bytes
from sys import getsizeof

# Gerando uma lista de números com List Comprehesion
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehesion
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehesion
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension : {set_comp}')
print(f'Dictionary Comprehension : {dic_comp}')
print(f'Generator Expression : {gen}')
