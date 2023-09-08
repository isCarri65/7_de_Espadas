'''Trabajo Práctico N 4'''


#Ejercicio 1
#Se requiere un programa que muestre por pantalla el incremento de una variable x por ciclo
x = 0
while x <= 30:
    x += 1
    if x == 15:
        break                                   #Concluye el ciclo si el valor de x es igual a 15
    if x ==4 or x==6 or x==10:                  #Cuando la variable tome el valor de 4, 6 o 10 se salteará su impresion por pantalla
        print(f"El valor {x} de x fue omitido")
        continue
    else:
        print(f"El valor del ciclo es:  {x}")

print(f"Se rompió la ejecucuión del bucle cuando x valia: {x}")     	#Muestra el valor final de x una vez termina el ciclo



 #Ejerccicio 7
 #Se me solicita que con un bucle while pueda elegir multiples opciones y que imprima en cada reiteracion la opción elegida
respuesta = -1                              #Inicializo la variable en -1
print("Eliga una opción")
print("1-Primera opción \n2-Segunda opción \n3-Tercera opción")
while respuesta != 0:
    respuesta = int(input("> "))            #Pido al usuario que eliga una opción
    if respuesta==0:
        print("\nprograma finalizado")      #Si ingresa cero, finaliza el bucle
        break
    elif respuesta==1:                      #Si elige una de las opciones, imprimirá la que ha elegido
        print("\nHas elegido la opcion 1")
    elif respuesta == 2:
        print("\nHas elegido la opcion 2")
    elif respuesta == 3:
        print("\nHas elegido la opcion 3")
    else:                                           #si no se da ningun un caso, mostrara por pantalla que no ha elegido ninguna opcion
        print("\nNo has elegido ninguna opción") 
    print("\nIngrese otra opción")



    


