from time import sleep
num = int(input('\033[32mInforme um número até 9999: \033[m'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[35mAnalisando o número {}...\033[m'.format(num))
sleep(2)
print('\033[31mUnidade\033[m: {}'.format(u))
print('\033[33mDezena\033[m: {}'.format(d))
print('\033[34mCentena\033[m: {}'.format(c))
print('\033[37mMilhar\033[m: {}'.format(m))