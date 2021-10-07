# Um algoritmo que le e escolhe uma ordem aleatória de nomes

import random

nome1 = input('digite o 1° nome: ')
nome2 = input('digite o 2° nome: ')
nome3 = input('digite o 3° nome: ')
nome4 = input('digite o 4° nome: ')

print(random.sample([nome1, nome2, nome3, nome4], k=4))
