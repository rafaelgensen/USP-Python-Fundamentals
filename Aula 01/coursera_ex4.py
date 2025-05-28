print()
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_total = int(segundos_str)

dias = segundos_total//(3600*24)
segundos_restantes = segundos_total % (3600*24)
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60
 
 
print()
print(dias, "dias,", horas, " horas,", minutos, " minutos e", segundos_final, " segundos.")
print("")
