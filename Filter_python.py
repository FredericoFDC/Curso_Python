"""
Filter
filter () -> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean ()
media = statistics.mean(dados)
print(f'Media: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais)> 0, paises)
print(list(res))

usuarios = [
    {"username": "Samuel", "tweets": ["Eu gosto de bolo", "Eu gosto de pizzas"]},
    {"username": "Igor", "tweets": ["Eu gosto de carros"]},
    {"username": "Vanessa", "tweets": ["Eu gosto de bolo", "Eu gosto de chocolate"]},
    {"username": "Carla", "tweets": []},
    {"username": "Trakinas", "tweets": []},
    {"username": "Marcos", "tweets": []}
]
#print(usuarios)
# Filtrar os usuários que estão inativos no Twitter

# Forma 1
#inativos = list(filter(lambda u: len(u['tweets'])== 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuarios: not usuarios['tweets'], usuarios))

print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', "Maria"]

# Devemos criar uma lista contendo 'sua instrutura e ' + nome, desde que cada noime tenha menos
#de 5 caracteristicas

lista = list(map(lambda nome: f'Sua instrutura é {nome}',filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
