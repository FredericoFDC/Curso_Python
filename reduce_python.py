"""

"""
# Como funciona na prática?
# Vamos utilizar a função redice() para multiplicar todos os números de uma lista 

from functools import reduce

dados = [1, 2, 3, 4, 7, 11, 15, 28, 30, 31]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros

mult = lambda x, y: x *y

res = reduce(mult, dados)
print(res)
