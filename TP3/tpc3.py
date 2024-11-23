import random

def jogar():
    fosforos_restantes = 21  
    jogador = input("Se quiser jogar primeiro pressione 'H', caso queira que comece o computador pressione 'C': ").lower()

    if jogador == "h":
        while fosforos_restantes > 1:
            fosforos_h = int(input(f"Quantos fósforos quer tirar (1 a 4)? Restam {fosforos_restantes} fósforos: "))
            while fosforos_h < 1 or fosforos_h > 4: 
                print("Não pode retirar mais de 4 fósforos ou menos do que 1!")
                fosforos_h = int(input(f"Quantos fósforos quer tirar (1 a 4)? Restam {fosforos_restantes} fósforos: "))

            fosforos_restantes = fosforos_restantes - fosforos_h  
            print(f"Restam {fosforos_restantes} fósforos!")

            if fosforos_restantes == 1:
                print("Você perdeu!")
                return 

    
            fosforos_c = 5 - fosforos_h  
            fosforos_restantes = fosforos_restantes - fosforos_c
            print(f"O computador retirou {fosforos_c} fósforos, restam {fosforos_restantes} fósforos!")

            if fosforos_restantes == 1:
                print("Você ganhou!")
                return 

    elif jogador == "c":
        while fosforos_restantes > 1:
            if fosforos_restantes <= 5:
                fosforos_c = fosforos_restantes - 1 
            else:
                fosforos_c = random.randint(1, 4) 
            fosforos_restantes = fosforos_restantes - fosforos_c
            print(f"O computador retirou {fosforos_c} fósforos, restam {fosforos_restantes} fósforos!")

            if fosforos_restantes == 1:
                print("Você perdeu!")
                return 

            fosforos_h = int(input(f"Quantos fósforos quer tirar (1 a 4)? Restam {fosforos_restantes} fósforos: "))
            while fosforos_h < 1 or fosforos_h > 4: 
                print("Não pode retirar mais de 4 fósforos ou menos do que 1!")
                fosforos_h = int(input(f"Quantos fósforos quer tirar (1 a 4)? Restam {fosforos_restantes} fósforos: "))

            fosforos_restantes = fosforos_restantes - fosforos_h  
            print(f"Restam {fosforos_restantes} fósforos!")

            if fosforos_restantes == 1:
                print("Você ganhou!")
                return  

jogar(21)