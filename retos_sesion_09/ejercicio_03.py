#Crear una lista de personas con 10 nombres de personas
personas = ["Juan", "María", "Juan", "Ana", "Luis", "Sofía", "Carlos", "Ariel", "Fabri", "Ghilmar"]
#Obten una sub lista de 2 a 7 
sub_lista = personas[2:7]
print(sub_lista)
#Buscar si existe el nombre "Jhon" en la lista original
print("Jhon" in personas)
#Ordenar la sub lista alfabéticamente
sub_lista.sort()
print(sub_lista)
#Ordenar la lista original alfabéticamente de forma descendente
personas.sort(reverse=True)
print(personas)