"""Vamos ver como fazer acesso a arquivos usando o Python."""
from utilidadesCeV.edit import *
from utilidadesCeV.dado import leia_int

titulo('Menu Principal')

try:
    while True:
        resp = leia_int(menu('Ver pessoas cadastradas.', 'Cadastras nova pessoa.', 'Apagar registo.', 'Sair'))
        if resp == 1:
            titulo(f'Ver pessoas cadastradas', 'blue2')

            arquivo = open('arquivo.txt', 'r')
            print(arquivo.read())

        elif resp == 2:
            titulo(f'Cadastrar nova pessoa', 'blue2')

            arquivo = open('arquivo.txt', 'r')
            conteudo = arquivo.readlines()

            dados = str(input('Nome: '))
            txt = dados
            dados = str(input('Idade: '))
            txt = f'{len(conteudo) - 1}   {txt:<10}    {dados:>6}\n'

            conteudo.append(txt)


            arquivo = open('arquivo.txt', 'w')
            arquivo.writelines(conteudo)
            arquivo.close()

        elif resp == 3:
            titulo(f'Programa Finalizado', 'blue2')
            break
        else:
            print(f'{edit("underline", "red")}Valor invalido', edit())
except(ValueError, TypeError, KeyboardInterrupt):
    print('Erro')
