tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
animales = dict(tupla)
print(animales)

clave = 'aves'
valor = animales.pop(clave)
print(animales)

animales['gato'] = '🐈'
print(animales)

animales['perros'] = ['🐶','🐕']
del animales['perro']
print(animales)
