# calculadorinha basiquinha

menu = 0
while 3 != menu:
    menu = int(input("""**********MENU**********
[ 1 ]. Calculadora;
[ 2 ]. Comparar;
[ 3 ]. Sair;
    Escolha: """))
    x = 0
    if menu == 1:
        # transforma todos os caracteres da operação em uma lista
        # ex: Calculadora: 12+12 retorna ['1', '2', '+', '1', '2']
        funcao = str(input('Calculadora: ')).strip()
        funcao = ' '.join(funcao).split()
        a = ''
        b = ''
        #Pega a primeira parte da função antes do sinal de operação
        while funcao[x] not in '+' and funcao[x] not in '-' and funcao[x] not in '*' and funcao[x] not in '/':
            a += str(funcao[x])
            x += 1
        # pega o sinal de operação
        operador = str(funcao[x])
        x += 1
        #pega a segunda parte da operação depois do operador
        for x in range(x, len(funcao)):
            b += str(funcao[x])
        # Executa a operação
        if operador == '+':
            print(int(a) + int(b))
        elif operador == '-':
            print(int(a) - int(b))
        elif operador == '*':
            print(int(a) * int(b))
        else:
            print(int(a) / int(b))
    elif menu == 2:
        media = 0
        a = '0'
        z = bool(True)
        while z:
            print('Digite "fim" para terminar.')
            a = str(input(f'{x+1}º número:')).strip().lower()
            if a != 'fim':
                media += int(a)
                x += 1
                print('media:', media/x)
            else:
                z = False
