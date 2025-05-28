
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
aux_largura = largura
aux_altura = altura

while aux_altura != 0: 
        while aux_largura != 0:
                if aux_altura == altura or aux_altura == 1:
                        print("#", end = "")
                else:
                        if aux_largura == largura or aux_largura == 1:
                                print("#", end = "")
                        else:
                                print(" ", end = "")
                aux_largura = aux_largura - 1
        aux_altura = aux_altura - 1
        aux_largura = largura
        print()
