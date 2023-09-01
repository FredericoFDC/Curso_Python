"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantido.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor {valor}\n' )

    
OBs = Como OrderemDict garanti a inserção de valores corretamente 

# Para utilizar o orderemDict

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor {valor}\n' )

"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) 
# True/False ?? São iguais ?? Sim. Porque para o dicionario comun são.

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)
# True/False ?? São iguais ?? Não. Porque no Ordered Dict a Ordem dos valores faz diferença.
