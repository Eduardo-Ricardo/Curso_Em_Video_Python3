# Crie um programa que receba um valor em metros e converta para centímetros e milímetros
x = float(input('Digite o valor em metros para ser convertido em cm e mm: '))
print('{:.2f} metros é, {:.0f} centímentros ou {:.0f} milímetros'.format(x, x*100, x*1000))
