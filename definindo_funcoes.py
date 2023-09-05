"""
Definindo funções

- Funçoes são pequenos trechos dde códigos que realizam tarefas específica:

já utilizamos várias funções desde que iniciamos este curso:
-len()
-print()
-max()
-min()
-count()
- e muito outras
cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando a função integrada (built-in ) do python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

# Definindo a primeira função
"""
# Exemplo 1

def diz_oi():
    print('oi')

#Para utilizar função devemos chamar ele.

diz_oi()

# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitos felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

for n in range(4):
    cantar_parabens()
    