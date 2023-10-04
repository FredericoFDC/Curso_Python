"""
Módulos externos

Utilizamos o gerenciador de pacotes Python chamado PIP - Python Installer Package

https://pypi.org.

colorama - usado para colorir as letras do texto.
"""
from colorama import init, Fore

init()

print(Fore.LIGHTBLUE_EX + 'Fredão é top')
print(Fore.YELLOW + 'Fredão é top')
print(Fore.RED + 'Fredão é top')
