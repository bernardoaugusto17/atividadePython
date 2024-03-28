print('\033[32m========== SOMA DAS NOTAS! ==========\033[m')
n1 = float(input('Qual é a primeira nota do aluno? '))
n2 = float(input('Qual é a segunda nota do aluno? '))
s = (n1 + n2) / 2
print(f'A média desse aluno entre {n1} e {n2} é igual á: {s:.1f}!')
if s >= 6.0:
    print('Sua média foi \033[32mBoa!\033[m PARABÉNS!')
else:
    print('Sua média foi \033[31mRuim!\033[m ESTUDE MAIS!')