print()
numero = input("Digite o número: ")
tamanho = len(numero)
numero = int(numero)
i = 1
soma = 0
resultado = 0

while(numero/10>1):

	while(tamanho > i):
		resultado = numero % (10**(tamanho-i))
		i = i + 1 
		print(resultado)
		
	soma = soma + resultado
	numero = (numero - resultado) / 10
	tamanho = tamanho - 1
	i = 1
	print("soma: ", soma)
	print("numero: ", numero)
	print("tamanho: ", tamanho)

soma = soma + numero

print("A soma final será: ", soma) 