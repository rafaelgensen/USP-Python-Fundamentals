def primo(x):
        
        if x == 1:
               return True
        else:
                count = 2
                while x % count != 0:
                        count = count + 1
                if x == count:
                        return True
                else:
                        return False


def maior_primo(x):
        
        resultado = 0
        i = 1
        
        while i <= x:
                if (primo(i)):     
                        resultado = i
                        i = i + 1
                else: 
                        i = i + 1
                        
        return (resultado)



