"""
OBS:
  O separador de casas decimais na programção é o ponto e não a vírgula.

  Quando convertemos de Float para Int perdemos a precisão de valores.
"""


# Errado
valor = 1, 44

print(valor)
print(type(valor))

# Certo

valor = 1.44
print(valor)
print(type(valor))


# É possivel fazer dupla atribuição

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para int.

res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
# Exemplo 5j ( j é um valor).
