#Crear una función anónima para obtener el área de un círculo con radio 5
area_circulo = lambda radio: 3.1416 * radio ** 2
radio = 5
area = area_circulo(radio)
print(f"El área de un círculo con radio {radio} es: {area}")