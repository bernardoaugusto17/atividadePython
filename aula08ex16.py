from math import trunc
print('\033[32m|PORÇÃO INTEIRA|')
n = float(input('Digite um valor: \033[m'))
di = trunc(n)
print(f'O número {n} tem a porção inteira de {di}')
