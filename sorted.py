"""
Sorted 
OBS - Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort() so funciona na lista

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() server para ordenar.

Exemplo 


numeros = [6, 1, 8, 2]

print(sorted(numeros))


#Exemplo
usuarios = [
    {"username": "Samuel", "tweets": ["Eu gosto de bolo", "Eu gosto de pizzas"]},
    {"username": "Igor", "tweets": ["Eu gosto de carros"]},
    {"username": "Vanessa", "tweets": ["Eu gosto de bolo", "Eu gosto de chocolate"]},
    {"username": "Carla", "tweets": [], "cor": "amarelo"},
    {"username": "Trakinas", "tweets": []},
    {"username": "Marcos", "tweets": []}
]
#print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

"""
# Último exemplo 

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Too old to rock in roll", "tocou": 32}

]
# Ordena da menos tocada para a mais tocada.
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada.
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
