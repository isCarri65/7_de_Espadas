#2
print("Ingrese números enteros positivos")
num = 1
par = 0
impar = 0
while num != 0:
    num = int(input("> "))
    if num<0:
        print("El número ingresado no es válido, ingrese otro por favor")
    else:
        contador = 0
        cant = len(str(num))
        while contador != cant:
            if int(str(num)[contador])%2 == 0:
                par += 1
                contador += 1
            else:
                impar += 1
                contador += 1
print(f"Cantidad de dígitos pares ingresados: {par}\nCantidad de dígitos impares ingresados: {impar}")
