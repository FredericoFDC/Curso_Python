"""
Funções com parâmetros de entrada
- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que :
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma fução

def quadrado(numero):
    #return numero * numero # vezes
    return numero ** 2 # elevado a 2
print(quadrado(2))
print(quadrado(4))
print(quadrado(7))

# Refatorando uma fução

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitos felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/(a) {aniversariante}')

cantar_parabens('Marcos')

"""
# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada 
# em uma função quantas parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

def soma(a, b):
    return a + b

def multiplicacao(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplicacao(2, 5))
print(multiplicacao(10, 20))

print(outra(2, 5, 'Geek'))
print(outra(10, 20, 'Geek'))
