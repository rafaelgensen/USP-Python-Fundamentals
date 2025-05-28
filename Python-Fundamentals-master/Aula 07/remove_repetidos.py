
def remove_repetidos(lista):
        lista.sort()
        i = 0
        while i + 1 < len(lista):
                if lista[i] == lista[i+1]:
                        del lista[i+1]
                else:
                        i = i + 1
        return(lista)