print("")
horas_str = input("Digite a quantidade de horas que deseja converter: ")
horas_int = int(horas_str)
print("")

print("")
minutos_str = input("Digite a quantidade de minutos que deseja converter: ")
minutos_int = int(minutos_str)
print("")

segundos_horas = horas_int * 3600
segundos_minutos = minutos_int * 60
segundos_total = segundos_horas + segundos_minutos

print("O valor informado corresponde a: ", segundos_total, " segundos")
print("")
