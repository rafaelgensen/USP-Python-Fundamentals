print("")
segundos_str = input("Digite a quantidade de segundos que deseja converter: ")
print("")

segundos_total = int(segundos_str)
horas = segundos_total // 3600
segundos_restantes = segundos_total % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print(horas, " horas, ", minutos, " minutos e ", segundos_final, " segundos.")
print("")
