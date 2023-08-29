"""
    Em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
    dinâmicas e tambem de podermos colocar QUALQUER tipo de dado.

    Em C/Java: Arrays- Possuem tamanho e tipo de dado fixo: Ou seja, nesta linguagens se você criar um array do tipo int e com tamanho 5.
    Este array será sempre do tipo inteirop e poderá ter sempre no máximo 5 valores.
    Já em python:

    Dinâmico: Não possui tamnho fixo na Lista: ou seja , podemos criar a lista e simplesmente ir adicionando elementos:
    Qualquer tipo de dado: Não possuem tipo de dado fixo: ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: [] 

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print('Não encontrei ainda') 

# Podemos facilmente checar se determindado valor está contido na lista.
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print('Não encontrei ainda')

lista1.sort() # .sort() coloca em ordem a lista
print(lista1)

lista5.sort() # .sort() coloca em ordem a lista
print(lista5)
