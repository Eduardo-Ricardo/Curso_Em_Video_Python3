# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
x, y = int(input('Digite o valor a se formar a tabuada: ')), int(input('Até que numero vai essa tabuada? '))
for count in range(1, y+1):
    print(f'{x} x {count} = {x*count}')
