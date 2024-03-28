from time import sleep
print('\033[32m|AUMENTO DE SALÁRIO|\033[m')
s = float(input('\033[37mQual é o salário atual? \033[m'))
print('\033[35mCALCULANDO...\033[m👾')
sleep(1.5)
if s > 1250:
    a1 = s + (s*0.10)
    print(f'Seu salário com \033[33m10%\033[m de aumento vai passar a ser \033[32m{a1:.2f}R$\033[m')
else:
    a2 = s + (s*0.15)
    print(f'Seu salário com \033[34m15%\033[m de aumento passa a ser \033[32m{a2:.2f}R$\033[m')