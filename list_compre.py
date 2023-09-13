"""
List Comprehension 

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe de List Comprehension

- lista - [dado for dado in iterável]

#exemplo 1
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros] # - Lista []
print(res)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

"""
#exemplo 1
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros] # - Lista []
print(res)

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor + valor

res = [funcao(numeros) for numero in numeros]
print(res)
