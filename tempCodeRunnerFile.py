sueldo_base = float(input("Ingrese el sueldo base: "))
#cantidad_ventas = int(print("Ingrese cantidad de ventas:) "))
cantidad_ventas = 3
comision = 0.1*cantidad_ventas*sueldo_base
sueldo_total = sueldo_base + comision
print(f"Total de dinero en comisiones $ {comision} \nRemuneracion total de salario mas comision es: ${sueldo_total}")

#Ejercicio 15
hora_inicial = int(input("Ingrese la hora de salida: "))
minuto_inicial = int(input("ingrese el minuto de salida: "))
segundo_inicial = int(input("ingrse el segundo de salida: "))
tiempo_viaje = int(input("Ingrese en segundos el tiempo de viaje: "))
horas = tiempo_viaje//3600
minutos = (tiempo_viaje%3600)//60
segundos = tiempo_viaje%60
segundo_final = (segundo_inicial + segundos)%60
minuto_final = (minuto_inicial+ (segundo_inicial + segundos)//60+minutos)%60
hora_final = (hora_inicial+horas+(minuto_inicial+(segundo_inicial + segundos)//60+minutos)//60)%24
print(f"Hora de salida:   {hora_inicial} hs  {minuto_inicial} min {segundo_inicial} seg")
print(f"Hora de llegada:   {hora_final} hs {minuto_final} min {segundo_final} seg")
