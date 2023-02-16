                                                            #######Sets#######

"""
El tipo set en Python es la clase utilizada por el lenguaje para representar los conjuntos. Un conjunto es 
una colección desordenada de elementos únicos, es decir, que no se repiten.
"""

my_set = set()
# Usamos la palabra reservada
my_other_set = {} # Tambien lo podemos definir de esta manera
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Juli", "Moure", 31}
print(type(my_other_set)) # Ya lo definimos

print(len(my_other_set)) # Len cuenta los elementos, aqui tenemos 3

## Operaciones propias del objeto

my_other_set.add("JuliDev")
print(my_other_set) # Da como salida = "JuliDev", "Juli", "Moure", 31
# Un set es una estructura desordenada, 
# No podemos acceder a cada elemento por separado, no podemos controlar cada dato

my_other_set.add("JuliDev")
print(my_other_set) # Un set no admite datos repetidos
# Ordena por una instruccion interna, puede quedar ordenado de casualidad

## Corroboracion de datos

print("JuliDev" in my_other_set) #True
# ¿Se encuentra x dato en el set? 
print("Julidev" in my_other_set) #False

## Eliminacion de datos

my_other_set.remove("Moure") 
# Se imprimiria = "JuliDev", "Juli", 31

my_other_set.clear() # Vacia todos los elementos del set y queda a 0
print(my_other_set) # EL CLEAR NO BORRA EL SET

del my_other_set # Borra completamente el objeto
print(my_other_set) # my other set is not defined

## Conversion de set a lista

my_set = { "JuliDev", "Juli", "Moure", 31}
my_list = list(my_set)
print(my_list[1]) # No es recomendable hacer esto porque ejecutas el programa 2 veces
# El set cambiara el orden de los elementos y no podras ubicarlos

## Union de sets

my_other_set.union(my_set)

## Diferencia

print(my_other_set.difference(my_set))
# a my_other_set le estamos quitando los elementos de my_set
