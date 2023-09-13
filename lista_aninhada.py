"""
Lista aninhada
- Algumas linguagens de programção possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em python nós temos as listas

numeros = [1, 2, 3, 4, 5]

# Exemplo

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
print(lista)
print(type(lista))

# Como fazemos para acessar os dados?

print(lista[0][1]) # 0 numero da linha // 1 numero da coluna = 2
print(lista[2][1]) # 2 numero da linha // 1 numero da coluna = 8

# Iterando com loops em uma lista aninhada
for lista in lista:
    for num in lista:
        print(num)

# Exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

# Lista Comprehension
[[print(valor) for valor in lista] for lista in listas]

"""
# Exemplo 2

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
