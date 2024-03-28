nome = str(input('\033[35mQual é seu nome? \033[m'))
if nome == 'Bernardo':
    print('\033[32mQue nome lindo voce tem!\033[m')
else:
    print('\033[37mSeu nome é tão normal!\033[m')
print(f'\033[33mBom dia\033[m, {nome}!')