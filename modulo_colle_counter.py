"""
Módulo Collections - Counter 

Collections - high-performance Container Datetypes

Counter - recebe um interável como parâmetro e cria um objeto do tipo collections counter que é par
ecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor 
a quantidadede ocorrências desse elemento.


"""
# Utilizando o counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# utilizando o counter
res = Counter(lista)

print(type(res))
print(res)

# Encontrando as 5 palavras ou números com mais ocorrências no texto.
print(f'Esses são os valores que mais se repetem {res.most_common(5)}')
