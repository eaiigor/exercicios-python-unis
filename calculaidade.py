print('########### Calculadora Tempo de Vida ###########\n')

# ENTRADA DE DADOS
nome = str(input('Qual é seu nome? '))
idade = int(input('Digite sua idade: '))

# PROCESSAMENTO DOS DADOS
dias = idade*365
meses = idade*12

# FINAL
print(f'\n{nome}, você possui {idade} anos. \nSua idade em meses: {meses}.\nSua idade em dias: {dias}')
print('\nObrigado.\n')
print('#################################################')
