# Faça um programa que leia se um ano é bisexto

ano = int(input('Qual ano você quer chegar se é bissexto? '))
if ano >= 0:
    if ano % 4 == 0:
        print('o ano {} é bissexto'.format(ano))
    else:
        print('o ano {} não é bissexto'.format(ano))
else:
    print('Digite apenas anos d.C')
