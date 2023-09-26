"""
O block try/except
utilizamos o bloco try/exept para tratar erros que podem ocorrer no nosso código.
prvinindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperados.

A forma geral mais simples é
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1- tratando um erro genérico
try:
    geek()
except:
    print('Deu algum problema')
# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro

# Exemplo 2- tratando um erro genérico
try:
    len(5)
except:
    print('Deu algum problema')
# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro
OBS - Tratar erro de forma genérica não e a melhor forma de tratamento de erros.
o ideal e sempre tratar de forma específica 

#Exemplo 3
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

#Exemplo 4
try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

#Exemplo 5
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte Erro: {err}')

#Exemplo 6
try:
    len(5)
except NameError as erra:
    print(f'deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente') # genérico
"""
#Exemplo 7

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
dic = {"nome": "Geek"}

print(pega_valor(dic, "nome"))
print(pega_valor(dic, "asa"))
print(pega_valor(7, "asa"))
