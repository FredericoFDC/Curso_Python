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

print(sum(num for num in range(1,10)))
