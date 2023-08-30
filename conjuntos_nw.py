"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos conjuntos
da matemática

- Aqui no python, os conjuntos são chamados de sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e intens duplicados.

os conjuntos ( sets ) são referenciados em python com chaves {}

Diferença entre conjuntos ( Sets ) e Mapas ( dicionário ) em python: 
    - um mapa tem chave/valor;
    - um sets tem apenas valor;

Exemplo 1
# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS - Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo 
# será ignorado sem gerar error e não fará parte do conjunto.

#Forma 2

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

Exemplos 2

# importante lembrar que além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados então temos 9 elementos.
lista = [99, 2, 34, 23, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados então temos 9 elementos.
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam valores duplicados por isso temos 8 elementos.
dicionário = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionário} com {len(dicionário)} elementos')

# Conjuntos não aceitam valores duplicados por isso temos 8 elementos.
conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

Exemplos 3

# Assim como todo outro conjunto python podemos colocar tipos de dados misturados em sets
# por exemplo

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalment

for valor in s:
    print(valor)


Exemplo 6
# usos interessantes com sets
# imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu.
# Informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
#e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades destintas ou únicas temos
# oque vc faria? Faria um loop na lista ?
# Podemos utilizar o set para isso

print(len(set(cidades)))
print(set(cidades))  # set ou conjunto nos tras somente as cidades únicas

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicação dentro de conjuntos ou sets não gera erro e não e adicionado
print(s)

# Remover elementos em um conjunto
# Forma 1
s = {1, 2, 3}
print(s)
s.remove(3)  # Não e índice e sim a informação do valor que vai ser removido.
print(s)

# Na forma 1 caso o valor não seja encontrado vai ser gerado o erro KeyError.

# Forma 2

s.discard(2)
print(s)

# Na forma 2 se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)
# Copiando um conjunto para outro

# Forma 1 de copia Deep Copy

novo = s.copy()  # Aqui aloca um novo valor somente na copia.
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 de copiar Shallow Copy

novo = s   # As duas variaveis vão ter o mesmo valor

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


# Métodos matemáticos de conjuntos(Sets)

#Imagine que temos dois conjuntos: Um contendo estudantes de curso python e um 
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

print(len(estudantes_python))
print(len(estudantes_java))

# Veja que alguns alunos que estudam Python também estudam java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

#Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)   # union = referece aos estudantes unicos dos dois cursos entre os dois cursos
print(unicos1)

# Forma 2 - utilizando o caractere pipe | ///  Para inserir pipe aperte alt + 124

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam java.

# Gerar conjuntos de estudantes que estão ambos nos dois cursos.

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java) # intersection = mostra quais pessoas estão nos dois cursos
print(ambos1)

# Forma 2 - utilizando o &  ////  & = e comercial

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar conjuntos de estudantes de um curso que não estam no outro

# Forma 1 - Utilizando difference

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


"""
# soma, valor máximo, valor mínimo, tamanho

s = {1, 2, 3, 4, 5, 6, 7}

print(sum(s)) # Sum = soma
print(max(s)) # max = Maior valor no conjunto
print(min(s)) # min = Menor valor no conjunto
print(len(s)) # len = Tamanho do conjunto
