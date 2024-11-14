print("Pensa em um número entre 0 e 100, e eu vou tentar adivinhar!")

mínimo = 0
máximo = 100
t = 0
acertou = False 

while not acertou:
    adivinha = (mínimo + máximo) // 2
    t = t + 1
    print(f"Eu acho que é: {adivinha}")

    r = input("Introduza 'm' se for maior, 'n' se for menor ou 'c' se acertei: ")

    if r == 'c':
        print(f"Eu acertei! O número é {adivinha}. Necessitei de {t} tentativas.")
        acertou = True  
    elif r == 'm':
        mínimo = adivinha + 1
    elif r == 'n':
        máximo = adivinha - 1
    else:
        print("Resposta inválida. Por favor, use 'm', 'n' ou 'c'.")
