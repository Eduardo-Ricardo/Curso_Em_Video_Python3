# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.
soma = preco_1000 = 0
while True:
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: '))
    soma += preco
    if preco > 1000:
        preco_1000 += 1
    if soma == preco or preco_menor > preco:
        preco_menor = preco
        nome_preco_menor = nome
    resposta = str(input('Deseja continuar [s/n]: '))
    if resposta == 'n':
        break
print(f'total da compra: R$ {soma:.2f}')
print(f'Quantidade de produtos com valor superior a R$ 1000,00: {preco_1000}')
print(f'Produto mais barato: {nome_preco_menor}')
