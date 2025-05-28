
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
aux = largura

while altura != 0: 
        while aux != 0:
                print("#", end = "")
                aux = aux - 1
        altura = altura - 1
        aux = largura
        print()
