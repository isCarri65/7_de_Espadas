import math
'''Trabajo Práctino N2'''

#Ejercicio 1
#Necesito saber si una computadora en nueva o vieja ingresando cuantos años tiene
computador_edad = int(input("Ingrese número de años de la computadora: "))  #Solicito que ingrese un número
if computador_edad <= 2:                                                    #Comparo el valor en un condicional, y despendiendo de ello imprimo una respuesta diferente
    print("El computador es nuevo")                                         
else:
    print("El computador es viejo")                                    


#Ej 2

computador_edad = float(input("Ingrese número de años de la computadora: "))

if computador_edad < 0:
    print("Por favor, ingrese numeros positivos")
elif computador_edad <= 2:
    print("Su computador es nuevo")
elif computador_edad > 2:
    print("Su computador es viejo")

#Ejercicio 3

primer_nombre = input("Ingrese el nombre de la primer persona: ").lower()
segundo_nombre = input("Ingrese el nombre de la segunda persona: ").lower()

if primer_nombre[0] == segundo_nombre[0] :
    print("Coincidencia")
else :
    print("No hay coincidencia")

#Ejercicio 4
print('Ingrese el candidato a votar según las opciones indicadas abajo')
print('A para votar por el partido rojo')
print('B para votar por el partido verdad')
print('C para votar por el partido azul')
candidato=input('Ingrese aqui su opcion a votar: ')
candidato=candidato.upper()
if(candidato=='A'):
    print('Usted ha votado por el partido rojo')
elif(candidato=='B'):
    print('Usted ha votdo por el partido verdad')
elif(candidato=='C'):
    print('Usted ha votado por el partido azul')
else:
    print('Usted ha ingresado una opcion errónea')


#Ejercicio 6

anio=int(input("Ingrese el año el cual desea saber si es o no bisiesto: "))

if (anio % 4==0 and anio % 100!=0) or (anio %400==0):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")


#Ejercicio 8
#Se me pide que comprube si usuario y contraseña son correctos para acceder a camelot
usuario = str(input("Ingrese nombre de usuario: "))
contrasenia = str(input("Ingresa la contraseña: "))
if usuario == "Gwenevere" and contrasenia == "excalibur":                   #compruebo que ambos valores ingresados sean correctos para permitir el ingreso
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


#Ejercicio 15
#Se me solicita que realice un programa que pregunte si quiera calcular el área de un triángulo o un círculo, y realizar dicha operacion
import math                                                         #importo biblioteca math para utilizar pi

print("Que desea calcular? Ingrese 't' o 'c' para elegir una de las opciones\nt) Área de un triángulo\nc) Área de un círculo") #Explico como selecionar una de las opciones
respuesta = str(input("> "))
respuesta = respuesta.lower()                                       #En caso de haber ingresado una letra mayúscula en la respuesta, la convierto en minúscula

if respuesta == "t" or respuesta == "c":                            #Confirmo de que haya elegido una respuesta válida
    if respuesta == "t":                                            #En caso de haber elegido t pido los datos para relizar el cálculo del área del triangulo
        base_t = float(input("Escriba la base del triángulo: "))
        altura_t = float(input("Escriba la altura del triángulo: "))
        area_t = base_t*altura_t/2
        print(f"El resultado del área es: {area_t}")
    else:
        radio = float(input("Ingrese el radio del circulo a calcular: ")) #En caso de no haber elegido t pido los datos para relizar el cálculo del área del círculo
        area_c = (radio**2)*math.pi
        print(f"El resultado del área del círculo es: {area_c}")
else:
    print("No a elegido ninguna de las dos opciones")                       #si no ha elegido una respuesta válido imprimo que no ha elegidido ninguna opción

        

