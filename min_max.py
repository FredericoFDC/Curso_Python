"""
Min e Max

max() -- Retorna o maior valor em um iterável ou o maior de dois ou mais elementos 

# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

# Exemplos
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) # 129

# Exemplos
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) # 129

# Exemplos
dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario)) # f

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario.values())) # 129

Exemplo

print(max(3, 34)) # max 34

# Faça um programa que receba dois valores do usuário e mostre o maior valor

val1=int(input('Informe o primeiro valor: '))
val2=int(input('Informe o segundo valor: '))

print(max(val1, val2))

Exemplos
print(max(75, 888, 1050))
print(max('abc', 'addd', 'afsfsfsfs'))
print(max('a', 'b', 'c', 'l'))
print(max(3.555, 8.5555))

min() -> Retorna o menor valor em um iterável ou menor de dois

"""
# Exemplo

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))
