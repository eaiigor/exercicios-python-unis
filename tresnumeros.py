print('##### Qual é o menor? #####\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

# Processando dados
menor = n1
if n2<n1 and n2<n3:
  menor = n2
if n3<n1 and n3<n2:
  menor = n3

# Resultado
print(f'\nO menor valor digitado foi {menor}.')
print('\n##########################')