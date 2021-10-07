# Faça um algoritmo que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Qual o seu nome? '))
print('Seu nome é:'+nome)
nome = nome.split()
print('Seu primeiro nome é: '+nome[0])
print('Seu ultimo nome é: '+nome[len(nome)-1])
