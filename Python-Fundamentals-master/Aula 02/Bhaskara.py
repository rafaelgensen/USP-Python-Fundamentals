import math

print()
print("Por favor, informe os valores na sequência abaixo")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b ** 2 - 4 * a * c

print()
print("delta: ", delta)

print()
if(delta < 0):

	print("Não existem raízes reais.")
	
else:
		x1 = (-b + math.sqrt(delta))/(2 * a)

		x2 = (-b - math.sqrt(delta))/(2 * a)
		
if(delta == 0):
	
	print("Existe apenas uma raíz real:")
	print("x: ", x1)
	
if(delta > 0):

	print("A duas raízes reais são as seguintes:")
	print("x1: ", x1, "x2: ", x2)

