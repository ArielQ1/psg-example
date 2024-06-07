#Crea un ciclo infinito que reciba un número por teclado y verifique si es un número primo, termina la ejecución si se ingresa el número 0
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    cont_div = 0
    for j in range(1, (numero//2)+1):
        if numero % j == 0:
            cont_div += 1
    if cont_div == 1:
        print(f"El numero {numero}, es primo!")