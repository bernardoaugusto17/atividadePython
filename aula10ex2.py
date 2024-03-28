from time import sleep
v = float(input('\033[35mQual é a velocidade atual do carro 🚗 ? \033[m'))
print('\033[32m=' * 26)
print('CALCULANDO A VELOCIDADE...')
print('=' * 26)
sleep(3)
if v > 80:
    print(f'\033[31mVOCÊ FOI MULTADO! Excedeu o limite permitido que é de 80km/h\033[m')
    m = v * 7 - 560
    print(f'Voce deve pagar uma multa no valor de \033[32m{m:.2f}R$\033[m')
print(f'\033[33mTenha um bom dia!\033[m dirija com segurança!')