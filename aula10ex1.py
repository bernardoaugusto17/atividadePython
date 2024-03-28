from random import randint
from time import sleep
print('\033[32m-=-' * 9)
print('PENSANDO EM UM NÚMERO...')
print('-=-' * 9)
n1 = int(input('\033[37mDescubra qual foi o número que pensei de 0 á 5: \033[m'))  # JOGADOR TENTA ADIVINHAR...
escolhido = randint(0, 5)  # FAZ O COMPUTADOR 'PENSAR'
print('\033[35mPROCESSANDO...\033[m')
sleep(2.5)
if n1 == escolhido:
    print(f'\033[34mParabéns\033[m eu pensei no número {escolhido}, \033[32mVoce acertou!\033[m')
else:
    print(f'VISHH, \033[31mVoce errou!\033[m Eu pensei no número {escolhido} e não no {n1}!')
