#Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palíndrome, termina la ejecución si se ingresa la palabra salir
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra.lower() == "salir":
        break
    if palabra.lower() == palabra.lower()[::-1]:
        print("La palabra es palíndroma")