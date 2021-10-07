# Calcula o SENO, COSSENO e TANGENTE de um angulo.
import math

angulo = math.radians(float(input("Digite um angulo qualquer: ")))

seno = float(math.sin(angulo))
cosseno = float(math.cos(angulo))
tangente = float(math.tan(angulo))

print('+{}+{}+\n|{:^10}|{:^6.2f}|'.format('-'*10, '-'*6, 'SENO', seno))
print('+{}+{}+\n|{:^10}|{:^6.2f}|'.format('-'*10, '-'*6, 'COSSENO', cosseno))
print('+{}+{}+\n|{:^10}|{:^6.2f}|'.format('-'*10, '-'*6, 'TANGENTE', tangente))
print('+{}+{}+'.format('-'*10,'-'*6))