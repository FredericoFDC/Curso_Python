"""
Debugando com PDB

PDB -> Python Debugger

bug - Inseto

"""

#Forma profissional de debugger
#Em Python

#Exemplo

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))