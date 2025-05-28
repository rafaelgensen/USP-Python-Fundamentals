
lista = [] 
i = 0
laco = 1
impressao = 0

while laco != 0:
        print()
        i = int(input("Digite um número: "))
        lista.append(i)
        if i == 0:
                impressao = len(lista)-1
                print()
                while impressao >= 0:
                        print(lista[impressao], end = '\t')

                        impressao = impressao - 1
                print()
