from math import radians, sin, cos, tan
from time import sleep
print('  \033[32m|SENO - COSSENO - TANGENTE|\033[m  ')
a = float(input('Digite o angulo que voce deseja: '))
print('\033[35mCALCULANDO...\033[m🤔')
sleep(2.5)
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O angulo de {a} tem o \033[31mSENO\033[m de {s:.2f} \nO angulo de {a} tem o \033[33mCOSSENO\033[m de {c:.2f} \nO angulo de {a} tem o \033[34mTANGENTE\033[m de {t:.2f}')