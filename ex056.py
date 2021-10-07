# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

repeticoes = int(input('{}\nQuantidade pessoas a ser analizada: '.format('==-*-=='*10)))
homem_mais_velho = -1
media_idade = 0
mulheres_sub20 = 0
for c in range(1, repeticoes + 1):
    leia_nome = str(input('Nome: '))
    leia_sexo = int(input("""(1). masculino
(2). feminino 
Sexo: """))
    leia_idade = int(input('Idade: '))
    print('==-*-=='*10)
    if leia_sexo == 1:
        if homem_mais_velho < leia_idade:
            nome_homem_mais_velho = leia_nome
            idade_homem_mais_velho = leia_idade

    media_idade += leia_idade

    if leia_sexo == 2:
        mulheres_sub20 = 0
        if leia_idade > 20:
            mulheres_sub20 += 1

print('Homem mais velho é {} com {:.0f} anos'.format(nome_homem_mais_velho, idade_homem_mais_velho))
print('media da idade {:.0f}'.format(media_idade/repeticoes))
print(f'mulheres com menos de 20 anos {mulheres_sub20}')
