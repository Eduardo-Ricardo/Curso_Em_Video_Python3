# leia o um salário e calcule um aumento de 15%
x = float(input('Qual o valor do salário? '))
print('o aumento sera de R$ {:.2f}, dando o total de R$ {:.2f}.'.format(x*0.15, x*1.15))