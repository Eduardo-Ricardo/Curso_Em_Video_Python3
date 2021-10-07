# Desenvolva um programa que te diga quanto dolares voce pode comprar com base en quantos reais voce tem
x = float(input('Me diga, quantos reais você tem pra ver quantos dolares voce pode comprar: '))
print('com R${:.2f} voce pode comprar ${:.2f}, sobrando R${:.2f}.'.format(x, x//5.20, x%5.20))