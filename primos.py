print('######### Descobrindo Números Primos #########\n')

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
  if n % c == 0:
    print('\033[33m', end='')
    tot += 1
  else:
    print('\033[31m', end='')
  print(f'{c}', end='')
print(f'\n\033[m0 número {n} foi divisível {tot} vezes.')
if tot == 2:
  print('É um número PRIMO.')
else:
  print('Não é um número PRIMO.\n')
  
print('###############################################')