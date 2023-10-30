"""
POO - Herança (inheritance)

A idade de herança e a de reaproveitar codigo. 
"""
class pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    def cpf_renda(self):
        return f'{self.__cpf} {self.__renda}'
    

class cliente(pessoa): # Herança entra aqui (pessoa) = herança

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class funcionario(pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
        
    
cliente_new = cliente('Carlos', 'Barbosa', '555.555.555-55', 5000)

print(cliente_new.nome_completo())
