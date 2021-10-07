# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ele aparece pela primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase qualquer: ').strip()
frase = frase.lower()
print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))
