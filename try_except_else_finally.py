"""
Try // Except // Else // Finally

Disca de quando e onde tratar código:

TODA ENTRADA DE DADOS DEVE SER TRATADA!

Exemplo 1

#num = 0
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

    #Exemplo 2
# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

#OBS= O bloco finally sempre e executado.


# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
else:
    print(dividir(num1, num2))

"""

# Exemplo mais complexo Correto
# Você é responsável pelas entradas das suas funções
# Então faça os tratamentos

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto.'
    except ZeroDivisionError:
        return 'Não e possível dividir por 0.'
    
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))