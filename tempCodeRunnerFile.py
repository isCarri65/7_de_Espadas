#Ejerccicio 7
 #
respuesta = -1
print("Eliga una opción")
print("1-Primera opción \n2-Segunda opción \n3-Tercera opción")
while respuesta != 0:
    respuesta = int(input("> "))
    if respuesta==0:
        print("programa finalizado")
    elif respuesta==1:
        print("Has elegido la opcion 1")
    elif respuesta == 2:
        print("Has elegido la opcion 2")
    elif respuesta == 3:
        print("Has elegido la opcion 3")
    else:
        print("No has elegido ninguna opción")
