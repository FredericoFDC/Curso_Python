"""
Teste de velocidade com expressoes geradores

# GEnerators (geradores)

def nums():
    for num in range(1, 10):
        yield num

gel = nums()

print(gel) # Generator

print(next(gel))
print(next(gel))

# Gerator Expression

ge2 = (num for num in range(1, 10))

print(ge2) # Generation expression

print(next(ge2))
print(next(ge2))


"""
# Realizando o teste de velocidade
import time

#geerator expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
