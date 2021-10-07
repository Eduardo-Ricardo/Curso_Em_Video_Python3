# Escreva um algoritmo  que pergunte o salario de um funcionário
# Se o salário for maior de R$ 1250,00 calcule um aumento de 10%
# Para salários inferiores calcule 15%

sal = float(input('qual o seu sálario?'))
if sal >= 1250.00:
    print('O seu aumento será de R$ {:.2f}, totalizando R$ {:.2f}.'.format(sal*0.1, sal*1.1))
else:
    print('O seu aumento será de R$ {:.2f}, totalizando R$ {:.2f}.'.format(sal * 0.15, sal * 1.15))

