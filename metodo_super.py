"""
O metodo super() se refere a super classe.

"""
class Animal:

    def __init__(self, nome, especie):
        self.__nome= nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')
    
    def gigante(self, forca, tamanho):
        print(f'O {self.__nome}, tem {forca} e seu tamanho e {tamanho}')
class Gato(Animal):
    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        # super().__init(nome, especie)
        self.__raca = raca

raca = Gato('Guilbert', 'Nivus', 'Neg')

raca.faz_som('Miau')

raca.gigante('muita força', ' muito grande')