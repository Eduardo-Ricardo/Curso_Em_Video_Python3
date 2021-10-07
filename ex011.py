# Faça um algoritmo que leia a area de uma parede e supondo que uma lata de tinta pinta 2m²,
# calcule quantas latas de tinta são nessessários para pintar a parede
x, y = float(input("Qual a altura da parede? ")), float(input('e qual a largura dela?'))
area = float(x*y)
print('Com a parede tendo {:.2f}m² para pintar você precisará de {:.1f} latas de tinta '.format(area, area/2))
