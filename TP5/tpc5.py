def listar(cinema):
    print("Filmes em exibição:")
    for sala in cinema:
        print(f" - {sala[2]}") 

def disponivel(cinema, filme, lugar):
    lugar_disponivel = True  
    sala_encontrada = False  

    for sala in cinema:
        if sala[2] == filme:  
            sala_encontrada = True  
            if lugar in sala[1]: 
                lugar_disponivel = False
            
    if not sala_encontrada:
        print("Filme não encontrado.")
    
    return lugar_disponivel 

def vendebilhete(cinema, filme, lugar):
    sala_encontrada = False  
    lugar_vendido = False  

    for i in range(len(cinema)):
        sala = cinema[i]
        if sala[2] == filme: 
            sala_encontrada = True  
            if lugar not in sala[1]:  
                nova_vendidos = sala[1] + [lugar]  
                nova_sala = (sala[0], nova_vendidos, sala[2])  
                cinema[i] = nova_sala 
                lugar_vendido = True  
            else:
                print(f"O lugar {lugar} já está ocupado.")

    if not sala_encontrada:
        print("Filme não encontrado.")
    
    if lugar_vendido:
        print(f"Bilhete vendido para o lugar {lugar} no filme '{filme}'.")

    return cinema

def listardisponibilidades(cinema):
    """Lista o filme em exibição e o total de lugares disponíveis em cada sala."""
    print("Disponibilidades:")
    for sala in cinema:
        lugares_disponiveis = sala[0] - len(sala[1]) 
        print(f" - {sala[2]}: {lugares_disponiveis} lugares disponíveis")

def inserirSala(cinema, sala):
    """Adiciona uma nova sala ao cinema, se a sala não existir."""
    sala_existente = False  

    for s in cinema:
        if s[2] == sala[2]: 
            sala_existente = True
            print(f"A sala exibindo '{sala[2]}' já existe.")

    if not sala_existente:  
        cinema.append(sala)  
        print(f"Sala com filme '{sala[2]}' adicionada.")
    
    return cinema

def menu():
    print("------------ MENU --------------")
    print("1 - Listar filmes em exibição")
    print("2 - Verificar disponibilidade de lugar")
    print("3 - Vender bilhete")
    print("4 - Listar disponibilidades")
    print("5 - Inserir nova sala")
    print("0 - Sair")
    print("--------------------------------")

def main():
    cinema = []  

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            listar(cinema)
        elif opcao == 2:
            filme = input("Digite o nome do filme: ")
            lugar = int(input("Digite o número do lugar: "))
            if disponivel(cinema, filme, lugar):
                print(f"O lugar {lugar} está disponível para o filme '{filme}'.")
            else:
                print(f"O lugar {lugar} não está disponível para o filme '{filme}'.")
        elif opcao == 3:
            filme = input("Digite o nome do filme: ")
            lugar = int(input("Digite o número do lugar: "))
            cinema = vendebilhete(cinema, filme, lugar)
        elif opcao == 4:
            listardisponibilidades(cinema)
        elif opcao == 5:
            nlugares = int(input("Digite o número de lugares na sala: "))
            filme = input("Digite o nome do filme: ")
            sala = (nlugares, [], filme)  
            cinema = inserirSala(cinema, sala)
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

