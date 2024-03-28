from time import sleep
print('        \033[32mQUEM É VOCÊ?        ')
nome = str(input('Digite seu nome completo \033[m🪪 : ')).strip()
n = nome.split()
print('\033[35mMuito prazer em te conhecer!\033[m')
sleep(1)
print(f'Seu primeiro nome é \033[37m{n[0]}\033[m')
print(f'Seu último nome é \033[34m{n[len(n)-1]}\033[m')