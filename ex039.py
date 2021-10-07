#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
#  alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
# Aqui recebe a data retiro os espaços indesejaveis troco as barras por espaços e por fim transformo ela em lista
nasc = str(input('Digite a sua data de nascimento: ')).strip().replace('/', ' ').split()
#  DD/MM/YYYY
data_nasc = datetime.date(int(nasc[2]), int(nasc[1]), int(nasc[0]))
data_alistamemnto = datetime.date((int(nasc[2]))+18, 12, 1)
print("""Seu ano de nascimento: {}.
Seu ano de alistamento: {}
E o ano atual: {}.""".format(data_nasc.year, data_alistamemnto.year, datetime.date.today().year))

if datetime.date.today().year == data_alistamemnto.year:
    print('\033[1;32mse fodeu kkkkkkkkk vai ter que se alistar kkkkkkkkkkkkkkkkkkkkk')
elif datetime.date.today().year > data_alistamemnto.year:
    print('\033[1;31mMano se deixou passar o ano de alistamento... se fodeu muito kkkkkkkkkkk')
else:
    print('\033[1;34mRelaxa voce ainda tem {} anos de vida'. format(data_alistamemnto.year - datetime.date.today().year))

