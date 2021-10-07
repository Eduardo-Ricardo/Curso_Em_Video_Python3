# Desenvolva um programa  que pergunte a distancia da de uma viagem um Kmm.
# calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens ate 200 Km, acima disso cobre R$ 0,45/Km

dist = int(input("Qual a distancia da sua viagem em Km: "))
if dist > 200:
    print('Sua viagem custará R$ {:.2f}.'.format(dist*0.45))
else:
    print('Sua viagem custará R$ {:.2f}.'.format(dist*0.5))
