palabra = input("Escriba una frase: ")
print(palabra.lower()[::-1].strip().replace(" ", "") == palabra.lower().strip().replace(" ", ""))