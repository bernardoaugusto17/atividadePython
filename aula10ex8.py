from time import sleep
print('\033[32m-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS 🔼')
print('-=-' * 10)
a = float(input('\033[34mPrimeiro segmento: \033[m'))
b = float(input('\033[31mSegundo segmento: \033[m'))
c = float(input('\033[33mTerceiro segmento: \033[m'))
print('\033[35mVERIFICANDO...\033[m👾')
sleep(1.5)
if b + c > a and a + c > b and a + b > c:
    print('Os segmentos acima \033[32mpodem\033[m formar um \033[34mtriângulo!\033[m')
else:
    print('Os segmentos acima \033[31mnão podem formar um triângulo :(')