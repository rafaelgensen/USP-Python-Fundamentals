print()
numero = input("Digite o número: ")
tamanho = len(numero)
numero = int(numero)
i = 1
anterior = 0
proximo = 0 

while(numero/10>1):

	while(tamanho > i):
		proximo = numero % (10**(tamanho-i))
		i = i + 1 
		print(proximo)
		
	numero = (numero - proximo) / 10
	tamanho = tamanho - 1
	i = 1
	
	if(anterior == proximo):
		print("O número tem dígitos em adjascentes iguais.")
		exit()
		
	anterior = proximo
	
if (numero == proximo):
	print("O número tem dígitos em adjascentes iguais.")
else:
	print("O número não tem dígitos adjascentes iguais.")