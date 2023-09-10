"""
Entendendo o *args
- O *args é um parâmetro,como outro qualquer. Isso significa que você poderá chamar
 de qualquer coisa, desde que começe com asterisco

Exemplo
*xix
Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função

# Exemplo
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(1, 2, 3))

# Entendendo o *args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))

# Outro exemplo de *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek'
    return 'Eu não tenho certeza de quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

# Exemplo 3

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3,4,5,6))

numeros = [1,2,3,4,5,6,7] # Nao consegue fazer a operação com essa lista

print(soma_todos_numeros(*numeros)) # O * server para passar um coleção de dados

numeros = [1,2,3,4,5,6] # Nao consegue fazer a operação com essa lista
# Desempacotador
num1, num2, num3, num4, num5, num6 = numeros
# Desempacotador

print(soma_todos_numeros(num1, num2, num3, num4, num5, num6))

"""
# Exemplo 3

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3,4,5,6))

numeros = [1,2,3,4,5,6,7] # Nao consegue fazer a operação com essa lista

print(soma_todos_numeros(*numeros)) # O * server para passar um coleção de dados

numeros = [1,2,3,4,5,6] # Nao consegue fazer a operação com essa lista
# Desempacotador
num1, num2, num3, num4, num5, num6 = numeros
# Desempacotador

print(soma_todos_numeros(num1, num2, num3, num4, num5, num6))
