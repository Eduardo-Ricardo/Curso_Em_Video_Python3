# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

escolha = str(input("""
ESCOLHA UMA OPÇÃO ABAIXO: 
(1) Dinheiro ou cheque;
(2) Catão á vista;
(3) 2x no cartão;
(4) 3x ou mais;
+==+==+==+==+==+==+==>>>>>""")).strip()
preco = float(input('O valor do produto:'))
if escolha == '1':
    print('Valor a ser pago: {}'.format(preco*0.90))
elif escolha == '2':
    print('Valor a ser pago: {}'.format(preco*0.95))
elif escolha == '3':
    print('Valor a ser pago: 2x de {}'.format(preco/2))
elif escolha == '4':
    vezes = int(input('Quantas vezes: '))
    print('Valor a ser pago: {}x de {}'.format(vezes, (preco*1.2)/vezes))
else:
    print('escolha invalida')
