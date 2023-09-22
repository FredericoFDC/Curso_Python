"""
Len, Abs, Sum, Round

-- Len
len() retorna o tamanho.
#exemplo
print(len('Geek University'))

# Por debaixo dos pano, quando utilizamops a fução len() o python faz o seguinte:
# Dunder len
print('Geek University'.__len__())


# Abs
-- Abs() retorna o valor absoluto de um número inteiro ou real, de forma básica,
seria o seu valor real sem o sinal.

# Exemplos
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Não existe abs de uma string
print(abs('Geek'))

# Sum
sum() recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos

obs - o valor inial default = 0
# Exemplo Sum
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5,], 5)) # Valor fixo de 5

print(sum([3.145, 5.678]))

# Round
round() retorna um número arredondado

"""
#Exemplo
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2121212121, 2))

print(round(1.21999999, 2))