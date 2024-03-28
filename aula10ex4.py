from time import sleep
print('\033[32m=' * 21)
print('|PREÇO DA SUA VIAGEM|')
print('=' * 21)
d = float(input('\033[37mQual é a distância da viagem em quilometros? \033[m'))
print('\033[35mCALCULANDO PASSAGEM...💵🚌\033[m')
sleep(2.5)
if d <= 200:
    p1 = 0.50 * d
    print(f'Sua passagem será de \033[32m{p1:.2f}R$')
else:
    p2 = 0.45 * d
    print(f'Sua passagem será de \033[32m{p2:.2f}R$')
print('\033[33mBOA VIAGEM!')