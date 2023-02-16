                                                          ####### Tupla ########

"""
Una tupla es un conjunto ordenado e 
inmutable de elementos del mismo o diferente tipo
Como un contenedor de datos
"""

my_tuple = tuple
my_other_tuple = ()

my_tupla = (35, 1.80, "Juli", "Fenomenal")
print(my_tupla[-1]) # Da como resultado Fenomenal
print(type(my_tupla)) 

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError xq tiene 3 elementos
# print(my_tuple[-6]) IndexError no puede dar mas de una vuelta en un intervalo  

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

