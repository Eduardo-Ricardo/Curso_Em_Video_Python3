# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos

n1 = int(input('n1 = '))
razao = int(input('r = '))
n = int(input('n = '))
menu = 0
continuacao = True
count = 0
while menu !='n':
    if continuacao:
        for n1 in range(n1, n*razao+n1, razao):
            count += 1
            #  1° termo ↑   ↑n=repetições   ↑ razão
            print(f'{n1} = n{count}')
    menu = str(input('Deseja mostrar mais algumas repetições [Se sim quantas: /n]: ')).strip().lower()
    if int(menu) > 0:
        n = int(menu)
        n1 += razao
        continuacao = True
    elif menu != 'n':
        print('\nATENÇÃO!\nOpção inválida.')
        continuacao = False
print('Fim.')
