""" 

Tuplas (tuple)
Tuplas são bastente parecidas com listas.
Existem basicamente duas diferenças násicas:

1- As tuplas são representadas por parênteses ()

2- As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2 : Tuplas com 1 elemento

tupla3 = (4)  # Isso não e uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla3)

print(type(tupla4))

tupla5 = 4,  # Isso é uma tupla
print(tupla3)

print(type(tupla5))

OBS: Podemos concluir que tuplas são definidas pela vírgula e não pela uso do parênteses

(4) não e tupla
(4,) é tupla
4, é tupla

tuplas = tuple(range(11))
print(tuplas)
print(type(tuplas))

tupla = ('Geek University', 'Programação em Python: Essencial', )

escola, curso = tupla

print(escola)
print(curso)

# Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.

tuplas = (1, 2, 3, 4, 5, 6)

print(sum(tuplas))  # sum = Soma
print(max(tuplas))  # max = Valor máximo ( maior valor dentro da tupla)
print(min(tuplas))  # min = Valor mínimo ( menor valor dentro da tupla)
print(len(tuplas))  # len = Tamanho

# Concatenação de tuplas

tupla1 = (1, 2, 3,)
print(tupla1)

tupla2 = (4, 5, 6,)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

# tupla1 só pode receber um novo valor se for dito isso dessa maneira:
tupla1 = tupla1 + tupla2
print(tupla1)

# iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n, end= ' ')
    # iterando sobre uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))  # count = conta quantas vezes se repete o valor dentro da tuplo.

exemplo

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro')

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# interar com while

i= 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# verificar em qual indice um elemento está na tupla

print(meses.index('setembro'))

# OBS : Caso o elemnto não exista, será gerado ValueError

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[0:]) # Pega a tupla do 0 até o final e mostra.
print(meses[5:]) # Pega a tupla apartir do 5 até o final e mostra.
print(meses[5:9]) # Pega a tupla apartir do 5 até o 9 e mostra.


"""
# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1

# Quando ultilizar tuplas
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro.
# - Trabalhar com elementos imutáveis traz segurança ao código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla 

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)
