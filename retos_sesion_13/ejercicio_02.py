#Imprimir los 20 primeros números primos
numero = 2
cantidad_primos = 0
while cantidad_primos < 20:
    cont_div = 0
    for j in range(1, (numero//2)+1):
        if numero % j == 0:
            cont_div += 1
    if cont_div == 1:
        print(numero, end=", ")
        cantidad_primos += 1
    numero += 1

