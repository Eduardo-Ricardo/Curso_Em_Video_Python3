frase_UM = 'ola'
print(frase_UM)
frase_DOIS = 'eduardo'
print(frase_DOIS)
for c in range(1, 3):
    frase_soma = frase_UM + frase_DOIS
    print(frase_soma)
    frase_UM = frase_soma + frase_UM
    print(frase_UM)