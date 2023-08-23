"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa
2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis e, python fazemos:
nome_da_variável = valor_da_variavel

Python é uma liguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java;
int numero = 42;
"""

numero = 42 # Exemplo de variável gloval
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = '01'
print(numero)
print(type(numero))

numero = 2

if numero < 10:
    novo = numero + 10  # A variável 'novo' esta declarada na variável local.
    print(novo)
