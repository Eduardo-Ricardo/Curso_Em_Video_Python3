# Crie um algoritmo que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quaisele foi alugado
# Calcule o preço a pagar. Sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 Km rodado.
x, y = float(input("Por quantos dias o carro foi alugado? ")), float(input("Quantos Km foram rodados? "))
print('O valor total a pagar é de : R$ {}'.format(x*60+y*0.15))
