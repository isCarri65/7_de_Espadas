''' Ejercicos de bucle for - while''' 
#1
#Tengo que encriptar mensajes recibidos con el método "la cifra del cesar" en el que el usuario pueda elegir cuantas letras saltarse
abcd2 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"               #Creo un string que contenga el abecedario en mayúscula
total_mensajes = []                                 
mensaje_encriptados = []

#Pido al usuario que ingrese 5 mensajes y lo guardo en una lista
for i in range(5):
  print("Ingrese el mensaje Nº", i+1, ": ")
  mensaje = str(input(">"))
  total_mensajes.append(mensaje.upper())    #Agrego cada mensaje en mayúscula a la lista


print(total_mensajes)
corrimiento = int(input("Ingrese la cantidad de lugares que se correran las letras: "))  #El usuario elige el la cantidad de letras que se saltatra para formar el mensaje encriptado

for palabra in total_mensajes:
    palabra_final = ""                  #Inicializo la  variable como string
    long_p = len(palabra)               #Averiguo la longitid en caracteres de cada mensaje

    for k in range(long_p):             #recorro uno por uno los caracteres del mensaje
        posicion_abc = abcd2.find(palabra[k])           #Busco si se encuentra en el abecedario
        if posicion_abc == -1 :                         #En caso de que no, no se modifica y se concatena con el mensaje encriptado
            palabra_final = palabra_final+palabra[k]
        else:                                           #En el caso de que si, se modifica y concatena con el mensaje encriptado
            if posicion_abc+corrimiento > 27:                                           #En caso de que sila suma del coorimiento supera la las letras del abecedari este vuelve a comenzar desde la letra "a"
                palabra_final = palabra_final+abcd2[(posicion_abc+corrimiento)%27]    
            else:
                palabra_final = palabra_final+abcd2[posicion_abc+corrimiento]
            
      
    mensaje_encriptados.append(palabra_final)           #Se agregan el mensaje encriptado a una lista
print(f"Devolviendo los mensajes encriptados\n{mensaje_encriptados}")


#2

#Se me solicita cree un programa para que el usuario ingrese numeros enteros positivos repetidamente hasta que ingrese el cero, y contar la cantidad de digitos pares e impares de cada número ingresado
print("Ingrese números enteros positivos")

#inicializo unas variables
num = 1
par = 0
impar = 0

#Creo un bucle while que se repetirá mientras que el ususario no ingrese el cero
while num != 0:
    num = int(input("> "))
    if num<0:                                                               #Se repite el bucle sin modificaciones si el número es negativo
        print("El número ingresado no es válido, ingrese otro por favor")
    else:
        contador = 0                                #Cominezo el contador en cero en cada bucle
        cant = len(str(num))                        #averiguo la longitud en caracterres del numero ingresado
        while contador != cant:                     #comienzo otro bucle que se repetira en relacion con la longitud en caracteres del número
            if int(str(num)[contador])%2 == 0:      #Averiguo si es par o impar cada digito del del número
                par += 1
                contador += 1
            else:
                impar += 1
                contador += 1

#Imprimo el mensaje con la sumatoria de digitos pares  e impares
print(f"Cantidad de dígitos pares ingresados: {par}\nCantidad de dígitos impares ingresados: {impar}")

    

  