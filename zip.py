"""
Zip
zip() craia um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados
como entrada em pares
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

#Sempre podemos gerar uma lista, tupla ou dicionário

print(list(zip1))

print(tuple(zip1))

print(set(zip1))

print(dict(zip1))

#  Exemplo 1
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a':11, 'b':12, 'c': 13, 'd':14 ,'e':15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""
# Exemplo 2

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

#final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
#print(final)
#print(type(final))
