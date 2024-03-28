m = float(input('\033[32mDigite uma distancia em metros: \033[m'))
print(f'A medida de {m}m corresponde á:')
k = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
c = m * 100
mm = c * 10
print(f'{k}km \n {hm:.2f}hm \n {dam:.1f}dam \n {dm:.0f}dm \n {c:.0f}cm \n {mm:.0f}mm')
