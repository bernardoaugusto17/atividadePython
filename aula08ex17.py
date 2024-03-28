from math import hypot
print('   \033[32m|CÁLCULO HIPOTENUSA|\033[m    ')
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
h = hypot(ca, co)
print(f'\033[35mA hipotenusa mede {h:.2f}\033[m')
