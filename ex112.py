"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
 valores que seja monetários.
"""
from utilidadesCeV.dado import leia_dinheiro
from utilidadesCeV.moeda import resumo


num = leia_dinheiro(input('Digite um preço: '))
resumo(num, 10, 50)

