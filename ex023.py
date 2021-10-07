# Crie um algoritmo  que leia um numero de 0 a 9999 e mostre na tela cada um dos seus digitos separados

num = str(input('Digite um numero de 0 a 9999 por favor... '))
num = '{:0>4}'.format(num)
print(num)
print('+{}+{}+\n|{:<10}|{:^5}|'.format('-'*10, '-'*5, 'Tipo', 'Qtd.'))
print('+{}+{}+\n|{:<10}|{:^5}|'.format('-'*10, '-'*5, 'Milhar', num[0]))
print('+{}+{}+\n|{:<10}|{:^5}|'.format('-'*10, '-'*5, 'Centena', num[1]))
print('+{}+{}+\n|{:<10}|{:^5}|'.format('-'*10, '-'*5, 'Dezena', num[2]))
print('+{}+{}+\n|{:<10}|{:^5}|'.format('-'*10, '-'*5, 'Unidade', num[3]))
print('+{}+{}+'.format('-'*10, '-'*5))

