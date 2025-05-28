valor = int(input("Digite o valor de n:"))
i = 0 
resultado = 1

while valor > 0:
	resultado = resultado * valor 
	valor = valor - 1

print(resultado)