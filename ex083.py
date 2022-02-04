# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. O seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

espressao = str(input('Digite a expressão')). strip().lower()
operacao = True
lista = []
parenteses = 0

for c in range(0, len(espressao)):

    # Parênteses_________________
    if '(' in espressao[c]:
        parenteses += 1
    elif ')' in espressao[c]:
        parenteses -= 1
    if parenteses < 0:
        operacao = False
        break
    if c == (len(espressao) - 1) and parenteses > 0:
        operacao = False
    # Parênteses_________________

    # Operadores_________________
    operadores = ['+', '-', '*', '/']
    if c > 0:
        if espressao[c] in operadores and espressao[c - 1] in operadores:
            operacao = False
            break
    # Operadores_________________
if operacao:
    print('Operação Valida')

else:
    print('Operação Invalida')
