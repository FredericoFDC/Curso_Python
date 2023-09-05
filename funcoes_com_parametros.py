"""
Funções com Parâmetros Padrão (Default Parametros)

print('Geek University')

print()
-Exemplo de função onde a passagem de parâmetro seja opcional

-Exemplo de função onde a passagem de parâmentro seja obrigatória.
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())

def exponencial(numero, pontecia=2):
    return numero ** pontecia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))   #Por padrão eleve ao quadrado
print(exponencial(3, 2))  # Eleva a potência informada pelo usúario

# Exemplo 1

def soma(num1=2, num2=2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo 2

def mostra_informacao(nome='Geek', instrutor= False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Exemplo 3

def soma(num1, num2):
    return num1 + num2
def mat(num1, num2, fun=soma):
    return fun(num1, num2)
def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))


"""

