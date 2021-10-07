# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for n1 in range(n1, razao*10+n1, razao):
    #  1° termo ↑   ↑n/repetições   ↑ razão
    print(n1)
