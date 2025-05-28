def fatorial(x):
	resultado = 1
	while x > 0:
		resultado = resultado * x
		x = x - 1
	return(resultado)

x = int(input("X: "))
y = int(input("Y: "))

def binomial(x,y):
	resultado = fatorial(x)/(fatorial(y)*fatorial(x-y))
	return (resultado)
	
print()
print(binomial(x,y))