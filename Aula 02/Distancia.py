import math

print()
print("Informe a posição nos pontos no plano cartesiano: ")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia = ((x1-x2)**2)+((y1-y2)**2)

print()
if(math.sqrt(distancia) >= 10):
	print("longe")
else:
	print("perto")