# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for tempo in range(10, -1, -1):
    sleep(1)
    print('\033[1;{}m{}'.format(tempo+29, tempo))
for x in range(31, 34):
    print("""\033[1;{}m　　　　　＼　　　　　　☆
　　　　　　　　　　　　　|　　　　　☆
　　　　　　　　　　(⌒ ⌒ヽ　　　/
　　　　＼　　（´⌒　　⌒　　⌒ヾ　　　／
　　　　　 （’⌒　;　⌒　　　::⌒　　）      
　　　　　（´　　　　　）　　　　　:::　）　／
　　☆─　（´⌒;:　　　　::⌒`）　:;　　）       
　　　　　（⌒::　　　::　　　　　::⌒　）
　　 　／　（　　　　ゝ　　ヾ　丶　　　─
""".format(x))
    sleep(0.8)
print('Feliz ano novo ai parcero.')
