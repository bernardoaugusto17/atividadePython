from random import choice
from time import sleep
print('\033[32mQUAL DELES EU ESCOLHO?\033[m🤔')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
input('\033[37mTENTE ADIVINHAR QUAL DELES EU ESCOLHI\033[m 😏: ')
print('\033[35mVERIFICANDO...\033[m')
sleep(2)
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'Eu escolhi o aluno \033[31m{escolhido}!\033[m')
