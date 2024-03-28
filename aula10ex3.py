print('=== \033[31mPAR\033[m OU \033[34mÍMPAR\033[m ===')
n = int(input('\033[32mDigite um número 🔢: \033[m'))
if n / 2 % 1:
    print(f'O número {n} é \033[34mÍmpar.\033[m')
else:
    print(f'O número {n} é \033[31mPar.\033[m')