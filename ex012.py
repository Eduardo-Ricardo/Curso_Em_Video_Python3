# Faça um algoritmo que calcule 5% de desconto nos produtos
x = str(input('Qual o produto que você quer aplicar o desconto de 5%? '))
y = float(input('Qual o valor do(a) {}? '.format(x)))
print('O desconto será de R${:.2f}!'.format(y*0.95))
