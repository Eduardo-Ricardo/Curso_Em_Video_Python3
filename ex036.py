# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
# exceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Qual o seu salário?'))
emprestimo = float(input('O qual o falor a ser financiado?'))
prestacoes = float(input('Em quantas parcelas?'))
if (emprestimo / prestacoes) < (salario / 3):
    print('\033[4;32mSeu empreéstimo foi aprovado!!!')
else:
    print('\033[1;31mInferlizmente, seu financiamento foi negado.')
