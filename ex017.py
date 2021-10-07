#Calcula a  Hipotenusa
from math import sqrt

x, y = float(input("Digite o valor do cateto oposto: ")), float(input("Digite o valor do cateto adjacente: "))
print("O comprimento da hipotenusa é igual a: {}".format(sqrt((x**2)+(y**2))))