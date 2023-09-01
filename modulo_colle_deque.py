"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""
#importa
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

# appende = adiciona no final do deque

deq. append('y') # append() = Adiciona um valor no deque = para lista
print(deq)

# appendleft = adiciona no inicio do deque

deq.appendleft('k')

print(deq)

#remover elementos

print(deq.pop()) # pop - remove o utimo valor
print(deq)

print(deq.popleft()) # popleft - remove o primeiro valor
print(deq)
