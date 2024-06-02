nombre = input("Ingrese su nombre: ")
gustos_musicales = input("Gustos musicales separados por comas: ").split(",")

print(f"Hola {nombre}, nombre valido" if nombre else "No ingreso un nombre valido")

print('Te gusta el rock!' if 'rock' in gustos_musicales else "No te gusta el rock")