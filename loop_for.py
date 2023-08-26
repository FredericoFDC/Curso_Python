"""
Loop For

Loop = Estrutura de repetição.
For é uma dessas estruturas.
For = para.

C ou Java.

for(int i = 0; i < 10; i ++){
    //execução do loop
}

Python

For item in interavel:
    //execução do loop

Ultilizamos loops para iterar sobre sequências ou sobre valores interáveis

Exemplos de interáveis:
-String
   nome = 'Geek University'
-Lista
 lista = [1, 3, 5, 7, 9]
-Range
    númeors = range(1, 10)

Exemplos
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeors = range(1, 10) # Temos que tranformar em uma lista

#Exemplos de for 1:
#para letras dentro nome
for letras in nome:
    print(letras)

#Exemplos de for 2:
for numero in lista:
    print(lista)

#Exemplos de for 3: range(valor_inicial, valor_final)
for numero in range(1, 10):
    print(numero)

OBS: Quando não precisamos de um valor, podemos descartálos utilizando um underline(_).

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeors = range(1, 10) # Temos que tranformar em uma lista

# i = indice
# v = valor
# enumerate = gera para cada letra um indice, ou seja ( n = 0, o = 2, m = 3, e = 4. (nome))
for valor in enumerate(nome):
    print(valor[1])  # valor ou valor[0] ou valor[1]

Exemplo:
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
"""
nome = "Geek University"
for letra in nome:
    print(letra, end="")
