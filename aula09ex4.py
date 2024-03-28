frase = str(input('\033[32mDigite uma frase: \033[m')).lower().strip()
print(f'A letra \033[31mA\033[m aparece {frase.count('a')} vezes na frase.')
print(f'A primeira letra \033[31mA\033[m apareceu na posição {frase.find('a')+1}')
print(f'A última letra \033[31mA\033[m apareceu na posição {frase.rfind('a')+1}')