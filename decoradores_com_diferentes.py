"""
Decoratos com diferentes assinaturas

Decorators como funçoes 

#Relembrando 

Função com erroo

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'
    
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

#Testando

print(saudacao('Angelina'))

print(ordenar('Picanha', 'Batata Frita'))

Função com erroo

#Função correta

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'
    
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

#Testando

print(saudacao('Angelina'))

print(ordenar('Picanha', 'Batata Frita'))
"""
# DEcorator com argumentos


def verifica_primeira_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto! Primeiro argumento precisa ser {valor}"
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeira_argumento("Pizza")
def comida_favorita(*args):
    print(args)


@verifica_primeira_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))

print(soma_dez(8, 21))

print(comida_favorita("Arroz", "Carne", "Feijao"))

print(comida_favorita("Pizza", "Arroz", "Carne", "Feijao"))
