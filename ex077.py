# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Palavras', 'Povo', 'Tempo', 'Confortavel', 'Madrugada', 'Estrada')
for c in range(0, len(palavras)):
    print(f'A palavra selecionada é {palavras[c]}:', end="")
    for d in range(0, len(palavras[c])):
        if 'a' in str(palavras[c][d]).lower() or 'e' in str(palavras[c][d]).lower() \
                or 'i' in str(palavras[c][d]).lower() or 'o' in str(palavras[c][d]).lower() \
                or 'u' in str(palavras[c][d]).lower():
            print(f' {palavras[c][d]};', end="")
    print('')
