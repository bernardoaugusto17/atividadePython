print('\033[32m========== CALCULADORA BÁSICA ==========\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
rq = (n1+n2) ** (1/2)
print(f'{n1} + {n2} é igual á {a}\n {n1} - {n2} é igual á {s}\n {n1} x {n2} é igual á {m}\n {n1} dividido por {n2} é igual á {d:.1f}')
print(f'A potencia de {n1} e {n2} é: {p}\n A divisão inteira de {n1} e {n2} é: {di}\n O resto da divisão de {n1} e {n2} é: {r}')
print(f'A raiz quadrada de {n1} + {n2} é: {rq:.1f}')
print('\033[32m========================================\033[m')
