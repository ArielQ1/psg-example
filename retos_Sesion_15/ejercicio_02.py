#Crear un programa para crear una canasta de frutas, solicitar frutas por teclado y almacenar en una lista, si se ingresa "salir" termina la ejecución. Solo se permiten las siguientes frutas caso contrario lanzar una excepción personalizada
#🍅🍇🍈🍉🍊🍌🍍🍑
class FrutaNoPermitidaException(Exception):
    pass

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []
    
while True:
    fruta = input("Ingrese una fruta: ")
        
    if fruta.lower() == "salir":
        print("¡Gracias por usar el programa!")
        break
        
    try:
        if fruta not in frutas_permitidas:
            raise FrutaNoPermitidaException(f"Error: {fruta} no es una fruta permitida.")
        canasta.append(fruta)
        print(f"Fruta {fruta} añadida a la canasta.")
    except FrutaNoPermitidaException as e:
        print(e)
    
print("Canasta final:", canasta)