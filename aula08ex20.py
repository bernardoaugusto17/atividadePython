from random import shuffle
from time import sleep
print('\033[32m=' * 21)
print('ORDEM DE APRESENTAÇÃO')
print('=' * 21)
a1 = str(input('\033[mPrimeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('\033[35mMUDANDO A ORDEM...\033[m🌪️')
sleep(2.0)
print(f'\033[34mA ordem de apresentação será\033[m 📝:')
print(lista)