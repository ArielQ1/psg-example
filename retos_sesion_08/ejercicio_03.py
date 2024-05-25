#Ingresa una cadena por teclado y almacena el valor en una tupla
mi_tupla = (input("Ingrese una cadena: "),)
#Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
tupla_concatenada = ('¡', ) + mi_tupla + ('!', )
#Imprime el resultado concatenado
print(tupla_concatenada)
#Repite la tupla final 3 veces e imprime el nuevo resultado
tupla_repetida = tupla_concatenada * 3
print(tupla_repetida)