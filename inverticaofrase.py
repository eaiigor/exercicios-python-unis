print('##### Invertendo Frases #####\n')

frase = str(input('Digite uma frase: '))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print(invertida)

print('\n#############################')