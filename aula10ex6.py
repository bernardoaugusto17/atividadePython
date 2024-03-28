from time import sleep
print('\033[32m-' * 25)
print('MAIOR E MENOR NÚMERO')
print('-' * 25)
print('\033[37m|Digite 3 números|\033[m')
n1 = int(input('\033[34mNúmero 1: \033[m'))
n2 = int(input('\033[33mNúmero 2: \033[m'))
n3 = int(input('\033[31mNúmero 3: \033[m'))
print('\033[35mPROCESSANDO...\033[m👾')
sleep(1.5)
if n1 >= n2 and n1 >= n3:
    print(f'O maior número é {n1}')
if n2 > n1 and n2 >= n3:
    print(f'O maior número é {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')
if n1 <= n2 and n1 <= n3:
    print(f'O menor número é {n1}')
if n2 < n1 and n2 <= n3:
    print(f'O menor número é {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')
# FORMA SIMPLIFICADA:

# VERIFICANDO QUEM É MENOR:
# menor = n1
# if n2 < n1 and n2 < n3:
#    menor = n2
# if n3 < n1 and n3 < n2:
#    menor = n3
# VERIFICANDO QUEM É O MAIOR:
# maior = n1
# if n2 > n1 and n2 > n3:
#    maior = n2
# if n3 > n1 and n3 > n2:
#    maior = n3