productos = ["Leche", "Pan", "Huevo", "Arroz", "Cereal"]
precios = [5.60, 0.50, 0.60, 10.80, 22.90]
#Agregar 5 productos nuevos al final de las listas
productos.extend(["Dulce", "Chocolate", "Papitas", "Refresco", "Chisitos"])
precios.extend([0.80, 15.5, 10, 13, 15])
#precio de les papitas
print("El precio de las papitas es de: ",precios[productos.index("Papitas")])
#Eliminar el producto con el nombre "Leche" de las listas
precios.remove(precios[productos.index("Leche")])#Elimino el precio de la leche para no variar los demas precios 
productos.remove("Leche")
#¿Cuanto cuesta el producto "Pan" y "Huevo"?
print("El precio del Pan es: ", precios[productos.index("Pan")])
print("El precio del Huevo es: ", precios[productos.index("Huevo")])
#¿Cual es el producto más caro y más barato?
print("El producto mas caro es: ", productos[precios.index(max(precios))])
print("El producto mas barato es: ", productos[precios.index(min(precios))])
#¿Cuántos productos tienes en total?
print(f"Tengo {len(productos)} productos en total")
#¿Cuanto cuesta el total de los productos?
print("El costo total de los productos es : ", sum(precios), "Bs.")
#Ordena los productos alfabéticamente y precios si es posible
productos.sort()
precios.sort()
print(productos)
print(precios)
#Eliminar todo
productos.clear()
precios.clear()
print(productos)
print(precios)