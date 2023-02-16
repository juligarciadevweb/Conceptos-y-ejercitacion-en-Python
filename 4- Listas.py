### Listas ###

"""
Son una forma de agrupación de datos
Son como superconjuntos de arreglos
"""
#Tenemos 2 formas de definirlas
my_list = list()
my_other_list = []

print(len(my_list))

# Aquí hacemos como una lista de edades
my_list = [
    35,
    24,
    62,
    97,
    15,
    54,
    10, 
] #Aquí tenemos 7 numeros enteros

print(my_list)
print(len(my_list)) # Cuento todos los elementos de la lista
# Como los arreglos en js empezamos desde el 0
 
my_other_list= [
    35, # Edad
    "Brais", # Nombre
    1.8, # Altura
    "Moure" # Apellido
] 
# No es necesario que guardemos siempre los mismos tipos de datos

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError
print(type(my_other_list))
# Tenemos un tipo lista

    # Comandos/acciones en las listas
print(my_other_list[0]) # En caso de querer acceder a cierto valor especifico usamos el indice
# El 0 seria el 35, el 1 el nombre, 2 la altura y el 3 el apellido 

my_other_list.append("MoureDev")
print(my_other_list) #Agrego un nuevo elemento al final de la lista

my_other_list.insert(1, "JuliDev")
print(my_other_list) # Inserta un nuevo elemento pero en un indice especifico

my_other_list[1] = "Fenomenal" # Cambio el valor anterior

my_other_list.remove("JuliDev")
print(my_other_list) # Borro x elemento de la lista, puede ser por el indice o con el array especifico

my_other_list.pop() # Pilla el ultimo elemento y lo elimina
print(my_other_list.pop) # Muestra el ultimo elemento de la lista
 
my_other_list.pop(2) 
# Le paso aquí el indice del elemento que yo quiero desapilar especificamenente

my_pop_element = my_other_list.pop(2) # Guardo el elemento que saque de la lista, hago como un retorno de la lista

del my_list [2] # Borra un elemento buscandolo por el indice

my_list.clear #Borra la lista completa, queda vacia la misma 

my_new_list = my_list.copy # Copio la lista en una nueva variable

my_new_list.reverse()
# Copia la lista de derecha a izquierda

my_new_list.sort() #Ordena la lista de menor a mayor o alfabeticamente en caso de que sean arrays


