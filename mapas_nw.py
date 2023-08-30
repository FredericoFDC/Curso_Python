"""
Mapas - Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

Exemplo 1

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Interar sobre dicionário
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi $ {receita[chave]}.00')

Exemplo 2

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

print(receita.keys()) # key = chama todas as chaves do dicionário dict_keys

for chave in receita.keys():   # Método recomendado pelo python
    print(receita[chave])

Exemplo 3

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Acessando os valores

print(receita.values())   # Values() Tras os valores do dicionário.

for valor in receita.values(): 
    print(valor)

Exemplo 4

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

Exemplo 5

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma, valor máximo. valor mínimo, tamanho
# Se os valores forem todos interiros ou reais

print(sum(receita.values())) # sum = soma
print(max(receita.values())) # max = valor máximo
print(min(receita.values())) # min = valor mínimo
print(len(receita.values())) # len = tamanho


"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma, valor máximo. valor mínimo, tamanho
# Se os valores forem todos interiros ou reais

print(sum(receita.values())) # sum = soma
print(max(receita.values())) # max = valor máximo
print(min(receita.values())) # min = valor mínimo
print(len(receita.values())) # len = tamanho

