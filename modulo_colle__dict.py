"""
Módulo Collections - Default dict

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # Se digitarmos uma chave que não exitem da erro KeyError

"""
# Fazendo import

from collections import defaultdict

#OBS = Lambda são funções sem nome, que podem ou não receber parâmetros 
# de entrada e retornar Valores.

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])  # KeyError = no dicionário comum, mas aqui não.
print(dicionario)