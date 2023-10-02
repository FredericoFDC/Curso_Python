"""
Trabalhando com módulo builtin - módulo integrados que já vem instalados no python -

Exemplo 1 

# Podemos importa todas as funçoes de um módulo utilizando 0 *
from random import *

print(random())

#Exemplo 2
# Importando todo o módulo 

import random

print(random.random())

# Exemplo 3
#Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

"""
# Utilizar tuple para colocar múltiplos imports
from random import (random, 
                    randint, 
                    shuffle, 
                    choice)

print(random())
print(randint(3, 10))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('Ferrarezi'))