# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

numero = int(input('Digite um numero (´999´ para fechar):'))
c = 0
soma = numero
while numero != 999:
    c += 1
    numero = int(input('Digite um numero (´999´ para fechar):'))
    soma += numero
soma -= 999
print('Soma dos termos:', soma)
print('Quantidade de termos digitados:', c)
