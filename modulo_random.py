"""
Módulo random e o que são módulos?

Em python, módulo nada mais são do que outros arquivos python.

Para utilizar o módulo tempos que importar ou instalar.

#Forma 1 - importando todo o módulo

import random

print(random.random())

# Forma 2
# Importando uma função especifica do módulo

from random import random

for i in range(10):
    print(random())

    
# uniform() - Gerar um número real pseudo-aleatório entre os valore estabelcidos

from random import uniform

for i in range(10):
    print(uniform(3, 10))

# randint() -> Gera números inteiros - pseudo aleatórios entre os valores estabelecidos.

from random import randint

for o in range(15):
    print(randint(1, 61), end=', ')

# Choice() - mostra um valor aleatório entre um iterável.
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
    
"""
# shuffle() - Tem a função de embaralhar dados
from random import shuffle

cartas = ['k', 'Q', 'J', 'A', '2', '3', '4']

print(cartas)
shuffle(cartas)
print(cartas.pop()) #pop
