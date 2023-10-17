"""
Decoradores - Decorator

O que são decorators?

- Decorators são funções;
- Decorator envolvem outras funções e aprimoram seus comportamentos;

/---------------------------/
/    Function Decorator     /
/---------------------------/


/---------------------------/
/    Função                 /
/---------------------------/

Decorators como funçoes 

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhcer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo')

#test 1

teste = seja_educado(saudacao)

teste()

"""
# Decorator com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer em te conhecer')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é fred')

#Testando

apresentando()
