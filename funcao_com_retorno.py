"""
Funções com retorno

numeros = [1, 2, 3]

print(f'A lista inicial está com esse valor > {numeros}')

ret = numeros.pop() # Remove o ultimo valor da lista pop

print(f'Retorno de pop, número removido > {ret}')
print(f'Valores atuais depois do uso do pop > {numeros}')

# Exemplo de função

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno ret > {ret}')  # None = nada.
print(f'Retorno > {quadrado_de_7() + 1}')

# Exemplo 1
def diz_oi():
    return 'oi, prazer em te conhecer ^^'
print(diz_oi())

# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())

# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Exemplo 4
#Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo.randômico entra 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

"""
# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar(valor):
    if valor % 2 != 0:
        return True
    return False
print(eh_impar())