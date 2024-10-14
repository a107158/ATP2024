
def menu():
    print("------------MENU--------------")
    print("Opção 1 - Criar Lista")
    print("Opção 2 - Ler Lista")
    print("Opção 3 - Soma")
    print("Opção 4 - Média")
    print("Opção 5 - Maior")
    print("Opção 6 - Menor")
    print("Opção 7 - estaOrdenada por ordem crescente")
    print("Opção 8 - estaOrdenada por ordem decrescente")
    print("Opção 9 - procura um elemento")
    print("Opção 0 - Sair")
    print("--------------------------------")

def criarLista():
    import random
    N = int(input("Quantos números deseja que tenha a sua lista?"))
    lista = []
    for i in range(N):
        x= random.randint(1,101)
        lista.append(x)
    return lista


def leLista():
    res = []
    N = int(input("Quantos elementos deseja que a sua lista tenha?"))
    for elem in range(N):
        x = int(input("Introduza um número."))
        res.append(x)
    return res

def somaLista(lista):
    soma = 0
    for elem in lista:
        soma = soma + elem
    return soma

def mediaLista(lista):
    if len(lista) == 0:
        media = 0
    else:
        media = somaLista(lista)/len(lista)
    return media

def maiorLista(lista):
    maior = lista[0]
    for elem in lista[1:]:
        if elem > maior:
            maior = elem
    return maior

def menorLista(lista):
    menor = lista[0]
    for elem in lista[1:]:
        if elem <  menor:
            menor = elem
    return menor

def estaOrdenadaC(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return "Não"
        else:
            return "Sim"
        
def estaOrdenadaD(lista):
    for i in range(len(lista) -1):
        if lista[i] < lista[i + 1]:
            return "Não"
        else:
            return "Sim"
        
def procuraElem(lista):
    x = int(input("Que elemento deseja procurar na lista?"))
    if x in lista:
        return lista.index(x)
    else:
        return "-1"
        


cond = True

while cond:
    menu()
    opcao = int(input("Introduza a opção pretendida."))
    
    if opcao == 1:
        lista = criarLista()
        print(lista)
    elif opcao == 2:
        lista = leLista()
        print(lista)
    elif opcao == 3:
        res = somaLista(lista)
        print(res)
    elif opcao == 4:
        res = mediaLista(lista)
        print(res)
    elif opcao == 5:
        res = maiorLista(lista)
        print(res)
    elif opcao == 6:
        res = menorLista(lista)
        print(res)
    elif opcao == 7:
        res = estaOrdenadaC(lista)
        print(res)
    elif opcao == 8:
        res = estaOrdenadaD(lista)
        print(res)
    elif opcao == 9:
        res = procuraElem(lista)
        print(res)
    elif opcao == 0:
        cond = False
        print("Até à proxima!")