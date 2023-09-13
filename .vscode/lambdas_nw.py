"""
Utilizando Lambdas

Conhecidas por Expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções aônimas

# Função em python

def soma(a, b):
    return a + b


def funcao(x):
    return 3 * x + 1
print(funcao(4))
print(funcao(7))

# Expressão lambda

lambda x : 3 * x + 1

# Como utilizar a expressão lambda

calc = lambda x : 3 * x + 1
print(calc(4))
print(calc(7))


 Exemplo 1
# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('  angelina ', ' JOLIE' ))
print(nome_completo(' FELICITY             ', '   jOnEs'))

 # Exemplo 2
# Em funções python podemos ter nenhum ou várias entradas. Em lambdas também:
amar = lambda : 'Como não amar python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1/ x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn:<expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS : Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Exemplo 3

autores = ['Isaac Asimov Limos', 'Ray Bradbury', ' Robert Bin Becks', 'Arthur nw', 'Frank heb', 'Orson scott',
           'Douglas Add', 'H. G. Wels', 'Leig Hut Power']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
#--------------------------------------------------------------------------------------
#O método sort() permite que você organize uma lista em ordem ascendente ou descendente
#--------------------------------------------------------------------------------------

"""
# Função quadrática
#f(x) = a * x ** 2 + b * x + c
# Definindo a função
def geradora_funcao_quadratica(a, b, c):
    # Retorna a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c
teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2)) #com valor de x já.

# Aplicação de lambda 
