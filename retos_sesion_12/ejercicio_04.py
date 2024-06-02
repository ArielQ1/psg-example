cliente = input("Nombre del Cliente: ")
edad = int(input("Edad del Cliente: "))
cantidad_compra = float(input("Monto de compra: "))

if edad >= 18 and cantidad_compra > 1000:
    print(f"{cliente} se le aplico un descuendo del 10%, debe cancelar {cantidad_compra-cantidad_compra*0.1}")
elif edad <= 18 and cantidad_compra > 500:
    print(f"{cliente} se le aplico un descuendo del 5%, debe cancelar {cantidad_compra-cantidad_compra*0.05}")
else:
    print(f"{cliente} se le aplico un descuendo del 2%, debe cancelar {cantidad_compra-cantidad_compra*0.02}")