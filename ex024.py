# Crie um algoritmo que analiza se o nome da cidade começa com 'santo'

cidade = input('Digite o nome da sua cidade: ')
cidade = (cidade.lower()).split()
print('santo' in cidade[0])
