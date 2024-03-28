from time import sleep
nome = str(input('\033[32mDigite seu nome completo: \033[m'))
print('\033[35mAnalisando seu nome...\033[m👾')
sleep(3)
print(f'Seu nome em maiúsculas é: \033[32m{nome.upper()}\033[m')
print(f'Seu nome em minúsculas é: \033[32m{nome.lower()}\033[m')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')