import math
'''Ejercico en clase - Condicionales'''

print('Ingrese la fecha actual en formato “día, DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el número de mes"')

fecha_actual = str(input("Ingrese fecha: "))                #Ingresa el dia de la semena junto la fecha en una sola variable en formato string
dia = (fecha_actual[0:-7]).lower()                          #Separa el dia de la semana en una variable diferente y la tranforma en letra imprenta minúscula
fecha = fecha_actual[-5:]                                   #Separa la fecha 
fecha_mes = fecha[3:5]                                      #Separa el mes de la fecha
fecha_dia = fecha[0:2]                                      #separa el dia de la fecha

#cambiamos el dia y el mes al tipo de variable entero

if int(fecha_dia)==0:
    fecha_dia = int(fecha_dia[1])
else:
    fecha_dia = int(fecha_dia)
if int(fecha_mes)==0:
    fecha_mes = int(fecha_mes[1])
else:
    fecha_mes = int(fecha_mes)

#Confirmamos que todos los valores sean correctos, Si no fuera el caso imprimimos por pantalla un mensaje de error

if (dia == "lunes" or dia =="martes" or dia=="miercoles" or dia=="jueves" or dia =="viernes") and (fecha_dia<=31 and fecha_dia>=1 and fecha_mes<=12 and fecha_mes>=1):
    
    #primer condicional de la consigna,
    
    respuesta = ""                                                              #inicializamos una variable como string para posterirmente compararla con otra del mismo tipo, ya que podriamos no llegar a insertarle un valor
    
    #Comprobamos si hubo examen el dia indicado

    if dia == "lunes" or dia == "martes" or dia == "miercoles":
        print("Hubo examen?")
        respuesta = str(input("Ingrese 'si' o 'no': "))
        
        if respuesta == "si":                                                       #Dependiendo de la respuesta anterior es verdadera, preguntamos la cantidad de aprobados y desaprobados
            aprobados = int(input("Ingrese cuantos alumnos aprobaron: "))
            reprobados = int(input("Ingrese cuantos alumnos reprobaron: "))
            porcentaje_ap = aprobados*(aprobados+reprobados)/reprobados             #calculamos el porcentaje de aprobados
            print(f"El procentaje de aprobados es de {aprobados}%")                 #imprimimos el resultado

        #Segundo condicional de la consigna
    if dia == "jueves":                                                         #confirmamos si el dia es jueves
        porcentaje_asis = str(input("Ingrese el porcentaje de asistencias (ej. 12%): "))  #preguntamos por el porcentaje de asistencias
        if float(porcentaje_asis[:-1])>50:                                      #Si supera el 50% imprimimos "asistio la mayoria"
            print("asistió la mayoria")
        else: 
            print("No asistió la mayoria")                                          #Sino imprimimo "No asistio la mayoria"

        #Tercer condicional de la consigna
    if dia == "viernes":                                                        #Comprobamos si el dia escrito fue viernes
        if fecha_dia == 1 and (fecha_mes == 1 or fecha_mes == 7):               #Comprobamos Si la fecha concide con 01/01 o 01/07
            print("Comienzo de nuevo ciclo")                                    #si cumple la condicion, calcularemos los ingresos total con la cantidad de alumnos ingresados y el precio del arancel por persona
            cant_ingresados = int(input("inserte la cantidad de alumnos ingresados: "))
            arancel = float(input("Ingrese el precio del arancel en $: "))
            ingreso_total = arancel*cant_ingresados
            print(f"El dinero ingresado total es de: ${ingreso_total}")         #Imprimimos ingreso total

else:
    print("Se produjo un error con los datos ingresados")








