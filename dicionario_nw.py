"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS = Sobre dicionário
    - Chave e valor são separados por dois pontos 'chave:valor' ;
    - Tanto chave quanto valor podem ser de qualquer tipo de dado ;
    - Podemos misturar tipos de dados;

# Criação de dicionários
# Forma 1 ( mais comun)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py':'Paraguai'}

print(paises)
print(type(paises))  # Class dict é = Dicionário.

# Forma 2 ( menos comun)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos 

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
#print(paises['ru'])

# Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get (Recomendado)
print(paises.get('br'))
print(paises.get('ru'))

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py':'Paraguai'}  # 'Chave' : 'Valor' exmplo = 'br':'Brasil // 'br' = chave // 'Brasil = valor.
 
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dados (int, float, string, boolean), inclusive
# listas, tuplas, dicionários, como chaves de dicionário

# Tuplas po exemplo são bastante interresantes de  serem utilizadas
# como chave de dicionários, pois as mesmas são imutáveis.
localidade = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidade)
print(type(localidade))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionários, Não podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 ( mais comum )

ret = receita.pop('mar') # pop = Remove o ultimo valor da lista, no dicionário precisamos informar a chave.
print(ret)

print(receita)

# Forma 2

del receita['fev']  # del = remove o elemento do dicionário.

print(receita)

del receita['fev']

print(receita)

# OBS - Se a chave não existir será gerado o KeyError
# Neste caso o valor removido não é retornado

# Imagina que você tem um comércio eletrônico, onde temos um carrinho
# de compras na qual adicionamos produtos.

CArrinho de compras:
    produto 1:
        - nome;
        - quantidade;
        - valor;
    produto 2:
        - nome;
        - quantidade;
        - valor;

# Poderiamos utilizar uma lista para isso? Sim
#Forma 1 utilizando lista

carrinho = []

produto1 = ['playstation 4', 1, 2300.00] # indice 0 = playstation 4, indice 1 = 1 quantidade, indice 2 = 2300 valor.
produto2 = ['God Of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Poderiamos utilizar uma tupla? Sim.
# Forma 2 utilizando tupla

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('God Of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Poderiamos utilizar um dicionário? Sim
# Forma 3 utilizando dicionário

carrinho = []

produto1 = {'nome':'playstation 4', 'quantidade': 1,'valor': 2300.00}
produto2 = {'nome':'God Of War 4','quantidade': 1,'valor':150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto.
# Podemos ter a certeza sobre cada informação.

# Limpar dados do dicionário.

#d.clear()

#print(d)

# Copiando um dicionário para outro

d = dict(a=1, b=2, c=3)

# Forma 1

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['e'] = 5
print(d)
print(novo)

"""
# Forma não usual de crição de dicionários.

outro = {}.fromkeys('a', 'b')  # Fromkeys() = cria um dicionário. chave e valor

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')   # chave e valor

print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros um interável e um  valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
