#Ejercicio 20
fecha = ""
fecha = str(input("Ingrese fecha de nacimiento en formato DDMMAAAA: "))
fecha = fecha[4:1]+"/"+fecha[2:4]+"/"+fecha[4:]
print(f"Fecha: {fecha}")
