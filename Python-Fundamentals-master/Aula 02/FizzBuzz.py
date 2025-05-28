print()
entrada = int(input("Informe o número: "))

resultado1 = entrada % 5
resultado2 = entrada % 3 

print()
if(resultado1 == 0 and resultado2 ==0):
	print("FizzBuzz")
else:
	print(entrada)