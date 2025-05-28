def troca(x, y):
    aux = x
    x = y
    y = aux
    return (x, y)

x = 10
y = 20

x = troca(x,y)
print("x=", x, "y=",y)
