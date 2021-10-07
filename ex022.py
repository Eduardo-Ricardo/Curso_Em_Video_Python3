# Crie um agoritmo que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras tem ao tod0 Sem considerar espaços.
# Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome? ')).strip()
print('Em maiúsculo fica:', nome.upper())
print('Em minúsculo fica:', nome.lower())
nome = nome.split()
print('o seu primeiro nome tem {} letras'.format(len(nome[0])))
print('e ao todo tem {} letras'.format(len(''.join(nome))))
