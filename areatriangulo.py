print('###### Calculo Triângulo ######\n')
print('Digite os valores de a, B e C')

a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
c = int(input('Valor de C: '))

if a > b+c:
    print('\n#############################\n')
    print(f'Valor de A: {a}\nValor de B: {b}\nValor de C: {c}\nEsses valores não formam um triângulo.')
else:
    # Calculo do perimetro:
    s = (a + b + c) / 2
    
    # Calculo da area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(f'A area do triângulo é de {area:.2f}')