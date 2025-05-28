
valor = 1

while valor != 0:

        print()
        print()
        valor = int(input("Digite o valor de n: "))
        resultado = 1
        aux = valor 
	
        while aux > 0:
                resultado = resultado * aux 
                aux = aux - 1
                print(resultado, end = '\t')
