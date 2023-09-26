"""
Raise TipoDoErro

# Exemplo Real 1

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek','azul')

# O raise como return finaliza a função. Ou seja nada após será execultado

# Exemplo Real 2

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisar estar entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek','vermelho')
"""
# Exemplo Real 2

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisar estar entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek','vermelho')