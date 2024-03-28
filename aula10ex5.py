from datetime import date
from time import sleep
print('\033[32m========================')
print('      ANO BISSEXTO      ')
print('========================\033[m')
a = int(input('Que ano voce quer analisar? Coloque \033[31m[0]\033[m para analizar o ano atual: '))
print('\033[35mANALISANDO...\033[m👾')
sleep(2)
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano \033[34m{a}\033[m é \033[31mbissexto!\033[m')
else:
    print(f'O ano \033[34m{a}\033[m não é \033[31mbissexto.')