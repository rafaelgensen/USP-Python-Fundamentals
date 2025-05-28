
print()
quantidade = int(input("Digite a quantidade de números: "))
print()

resultado = 0

while(quantidade>0):
	valor = int(input("valor:" ))
	resultado = resultado + valor
	print()
	print(resultado)
	print()
	quantidade = quantidade - 1 

print("Resultado final: ", resultado)