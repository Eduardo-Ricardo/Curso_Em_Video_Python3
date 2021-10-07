# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500. E QUE SEJAM IMPARES.
x = 0
for count in range(1, 501):
    if count % 3 == 0 and count % 2 == 1:
        x = count + x
print(x)
