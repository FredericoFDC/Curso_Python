"""
Erros mais comuns em python

-- E importante prestar atenção e aprender a ler as saídas de erros geradas pela execução


printf('Geek University')

Os erros mais comuns:

1 - SyntaxErros = Ocorre quando o python encontra um erro de sintaxe. ou seja. você escreveu algo que 
o python não reconhece como parte da linguagem.

errado> 
def funcao:
    print("Geel University")

Correto>
    def funcao():
    print('Geel University')

# Exemplo SyntaxError

None = 1

# Exemplo SyntaxError

return

2- NameError = Ocorre quando uma variável ou função não foi definida

# Exemplo NameError
print(geek)

3 - TypeError = Ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplo TypeError

print(len(5))

# Exemplo TypeError

print('Geek'+[])

# Exemplo TypeError

print('Geek'+ 4)

4 - IndexError = Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice inválido

# Exemplo IndexError

lista = ['Geek']
print(lista[0][10])

# Exemplo IndexError

lista = ['Geek']
print(lista[5])

5 - ValueError - Ocorre quando uma função/operação built -in (integrada)
recebe um argumento com tipo correto mas valor inapropriado

# Exemplo ValueError

print(int('Geek'))

6 - KeyError - Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplo KeyError

dic = {}
print(dic['Geek'])

7 - AttributeError = Ocorre quando uma variável não tem atributo/função

# Exemplo AttributeError

tupla = (11, 2, 31, 4)
print(tupla.sort())

Não existe sort em tupla então da error AttributeError

8 - IndentationError = Ocorre quando não respeitamos a indentação do python que e de 4 espaços

# Exemplo IndentationError

def nova():
print('Geek')

# Exemplo IndentationError

for i in range(10):
1+1


"""
# Exemplo IndentationError

