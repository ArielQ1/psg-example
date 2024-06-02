numero_1 = int(input("Numero 1 : "))
numero_2 = int(input("Numero 2 : "))
operacion  = input("Operacion(+,-,x,/): ")
print("-------------")
if numero_1 or numero_2:
    if operacion == "+":
        print("El resultado es : ", numero_1 + numero_2)
    elif operacion == "x":
        print("El resultado es : ", numero_1 * numero_2)
    elif operacion == "-":
        print("El resultado es : ", numero_1 - numero_2)
    elif operacion == "/":
        if numero_2 != 0:
            print("El resultado es : ", numero_1 / numero_2)
        else:
            print("No se puede dividir entre cero")
else:
    print("Ingrese Numeros Validos")