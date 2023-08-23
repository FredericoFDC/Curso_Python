"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

   /// Regras de funcionamento ///
Para o 'and', ambos os valores precisam ser True.
Para o 'or' , um outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira Flase, se for False vira True.
Para o 'is', = está.

"""

ativo = True
logado = True

if ativo and logado:
    print('Usuário ativo no sistema')
    print('Bem vindo')
elif not ativo:
    print('Você precisa ativar a conta')
elif logado is ativo:
    print("Falta ativar sua conta no e-mail")
else:
    print('Você precisa ativar sua conta, por favor verifique seu e-mail.')

    