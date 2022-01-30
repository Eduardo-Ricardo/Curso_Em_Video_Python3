# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até
# vinte. O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros_p_extenso = ("zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "sete", "oito",
                     "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
                     "dezessete", "dezoito", "dezenove", "vinte")
while True:
    usuario = int(input("Digite um número: "))
    if 0 <= usuario <= 20:
        print(numeros_p_extenso[usuario])
        break
    else:
        print("Resposta Invalida, tente novamente. ", end="")