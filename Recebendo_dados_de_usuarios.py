from datetime import date

# Entrada de dados
print("Qual é o seu nome? ")
nome = input()

# Exemplo de print antigo versao 2 python
# print("Seja bem vindo(a) %s " % nome)


# Exemplo de print versão 3.
# print("Seja bem vindo(a) {0}".format(nome))

# Exemplo atual de print versão 3.7
print(f"Seja bem vindo(a) {nome}")


print("Qual a sua idade? ")
idade = input()
# Processsamento

# Saída de dados
# print("Oi %s você tem %s anos" % (nome, idade))


print(f" A {nome} tem {idade} anos.")

print(
    f"{nome} nasceu em {2023 - int(idade)}."
)  #   int(idade)==> cast     ////   cast é a conversão de um tipo de dado para outro.
