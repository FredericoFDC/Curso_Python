"""
**Kwargs
dicionario
# Mais complexo 
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# nas nossas funcções podemos ter:
# parâmetros obrigatórios;
# *args;
# parâmetros  default( não obrigatorios)
# ** kwargs

"""
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', eu='Não', voce='Vai')
minha_funcao(34, 'Felipe', 4, 5, 3, solteiro=True)
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)
