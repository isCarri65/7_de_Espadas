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


#--------------------Ejercicio 5--------------------

vocales= ["a", "e", "i", "o", "u"]

letra= input("Por favor, ingrese una letra cualquiera: ").lower()
if (len(letra) > 1):
    exit("No se pudo procesar el dato, por favor, ingrese solamente una letra")
else:
    if letra in vocales:
        print("Es vocal")
    else:
        print("No es vocal")


# Ejercicio 7
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))
if (num1 < num2):
    menor = num1
elif (num2 < num3):
    menor = num2
else:
    menor = num3
print(f"Menor: {menor}")


#Ejercicio 8
#Se me pide que comprube si usuario y contraseña son correctos para acceder a camelot
usuario = str(input("Ingrese nombre de usuario: "))
contrasenia = str(input("Ingresa la contraseña: "))
if usuario == "Gwenevere" and contrasenia == "excalibur":                   #compruebo que ambos valores ingresados sean correctos para permitir el ingreso
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


#Ej 9
name = input("Ingrese su nombre: ")
sexo = input("Escriba si usted es Hombre(H) o Mujer(M): ")
nombre = name.lower()
sexo_l = sexo.lower()

if nombre[0] <= "m" and sexo_l == "m" or sexo_l == "mujer":
    print(" ")
    print("Perteneces al grupo A")
elif nombre[0] >= "n" and sexo_l == "h" or sexo_l == "hombre":
    print(" ")
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")


#Ejercicio 10
edad = int(input("Ingrese la eadad del cliente: "))
if edad < 4 :
    print("Entrada gratis")
elif edad >= 4 and edad <=18 :
    print("Valor de la entrada: $500")
elif edad > 18 : 
    print("Valor de la entrada: $1000")


#Ejercicio 11
eleccion=input('Desea usted una pizza vegetariana? ingrese S para si y N para no: ')
eleccion=eleccion.upper()
if (eleccion=='S'):
    print('Los ingredientes que usted puede elegir para esta pizza son Pimiento y Tofu')
    ingrediente=input('Ingrese el Ingrediente deseado: (la letra A para seleccionar Pimiento o B para seleccionar Tofu) ')
    ingrediente=ingrediente.upper()
    if (ingrediente=='A'):
        ingrediente_elegido='pimiento'
        print('Su pizza elegida es vegetariana')
        print('Los ingredientes de su pizza son: mozzarella, tomate y',ingrediente_elegido)
    elif (ingrediente=='B'):
        ingrediente_elegido='tofu' 
        print('Su pizza elegida es vegetariana')
        print('Los ingredientes de su pizza son: mozzarella, tomate y',ingrediente_elegido)
    else:
        print('Ingrese una opción válida')
elif(eleccion=='N'):
    print('Los ingredientes para esta pizza son Peperoni, Jamón y Salmón')
    ingrediente=input('Ingrese el Ingrediente deseado: (la letra A para seleccionar Peperoni, B para seleccionar Jamón o C para seleccionar Salmón) ')
    ingrediente=ingrediente.upper()
    if (ingrediente=='A'):
        ingrediente_elegido='peperoni'
        print('Su pizza elegida no es vegetariana')
        print('Los ingredientes de su pizza son mozarella, tomate y',ingrediente_elegido)
    elif(ingrediente=='B'):
        ingrediente_elegido='jamón'
        print('Su pizza elegida no es vegetariana')
        print('Los ingredientes de su pizza son mozarella, tomate y',ingrediente_elegido)
    elif(ingrediente=='C'):
        ingrediente_elegido='salmón'
        print('Su pizza elegida no es vegetariana')
        print('Los ingredientes de su pizza son mozarella, tomate y',ingrediente_elegido)
    else:
        print('Ingrese una opción válida')
else:
    print('Error, ingrese una opcion correcta')


#--------------------Ejercicio 12--------------------

anio_actual= int(input("Ingrese el año actual: "))
anio_random= int(input("Ingrese un año cualquiera: "))
cociente= 0

if anio_actual > anio_random:
    cociente= anio_actual - anio_random
    print(f"Han pasado {cociente} años desde ese año.")
else:
    cociente= anio_random - anio_actual
    print(f"Faltan {cociente} años para llegar al {anio_random}.")


#Ejercicio 13
num1=int(input("Ingrese un numero entero: "))
num2=int(input("Ingrese otro numero entero: "))

if num1 <=0 or num2 <=0:
    print("Numero incorrecto.")
else:
    mayor=max(num1, num2)
    menor=min(num1, num2)

if mayor % menor ==0:
    print(f"{mayor} es multiplo de {menor}")
else:
    print(f"{mayor} no es multiplo de {menor}")


# Ejercicio 14
print("--- Ecuacion de primer grado ---")
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

if a != 0:
    x = (-b) / a
    solucion = a * x + b
    print("La ecuacion tiene una solucion unica")
elif b == 0:
    print("La ecuacion tiene varias soluciones")
else:
    print("La ecuacion no tiene solucion")



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


#Ej 16

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
operacion_pedir = input("Ingrese una de las siguientes opciones: 1(Suma), 2(Multiplicacion), 3(Resta), 4(Division)")
if len(operacion_pedir) > 1:
    print("Por Favor, ingrese solo un numero")
else:
    print(" ")
    print("Calculando...")
    print(" ")
operacion = int(operacion_pedir)
if operacion == 1:
    c = a + b
    print(f"El resultado es: {c}")
elif operacion == 2:
    d = a * b
    print(f"El resultado es: {d}")
elif operacion == 3:
    e = a - b
    print(f"El resultado es: {e}")
elif operacion == 4:
    g = a / b
    print(f"El resultado es: {g}")


#Ejercicio 17
dia = input("Ingrese un día de la semana: ").lower()
if dia == "lunes" :
    print("A empezar la semana :(")
elif dia == "viernes" :
    print("Inicio del fin de semana!")
elif dia == "sabado" or dia == "domingo":
    print("¡Fin de semana!")
else :
    print("Otro dìa de semana...")


#Ejercicio 18
horas_trabajadas=float(input('Ingrese su cantidad de horas trabajadas: '))
salario=float(input('Iingrese su salario por hora: '))
horas_jornada_completa=48
if (horas_trabajadas>horas_jornada_completa):
    horas_extras=horas_trabajadas - horas_jornada_completa
    horas_normales=horas_jornada_completa
else:
    horas_extras=0
    horas_normales=horas_trabajadas
salario_total= (horas_normales * salario)+(horas_extras * salario *1.1)
print('Su cantidad de horas extras trabajadas es de: ',horas_extras, ' horas')
print('Su salario total es de: $',salario_total)


#--------------------Ejercicio 19--------------------

cantidad= int(input("Ingrese la cantidad de productos que desea comprar: "))
descuento= 0.07
costo_x_uni= 60
costo_final= 0

if cantidad > 1000:
    costo_final= (1000 * costo_x_uni) - ((1000 * costo_x_uni)*descuento)
    cantidad-= 1000
    costo_final+= (cantidad * costo_x_uni)
    print(f"El precio final con un descuento aplicado a parte del precio original es de ${costo_final}")
else:
    if cantidad == 1000:
        costo_final= (cantidad * costo_x_uni) - ((cantidad * costo_x_uni)*descuento)
        print(f"El precio final, con un descuento del 7%, es de ${costo_final}")
    else:
        if cantidad < 1000:
            costo_final= cantidad * costo_x_uni
            print(f"El precio final a pagar es de ${costo_final}")

#Ejercicio 20

nota1=float(input("Ingrese la primer nota:"))
nota2=float(input("Ingrese la segunda nota:"))
nota3=float(input("Ingrese la tercer nota:"))
nota4=float(input("Ingrese la cuarta nota:"))

prom=(nota1+nota2+nota3+nota4)/4

if prom >6:
    print("Alumno aprobado")
else:
    print("Alumno reprobado.")
