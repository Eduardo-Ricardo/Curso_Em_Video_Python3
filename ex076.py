# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Miojo', 2, 'Hamburguer', 1, 'Coca-Cola', 8, 'Bolacha', 2, 'Arroz', 20, 'Macarrão', 4)
print((produtos[0::2]))
linha = 0
for c in range(0, len(produtos), 2):
    if len(produtos[c]) > linha:
        linha = len(produtos[c])
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'+{"-" * linha}+{"-" * 10}+')
        print(f'|{produtos[c]}{" "*(linha - len(produtos[c]))}|', end="")
    else:
        print(f'R${produtos[c]:.>5},00|')
print(f'+{"-" * linha}+{"-" * 10}+')