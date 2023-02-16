####### Variables #######

my_int_variable = 5
print(my_int_variable)
#Definimos una variable de tipo numerica

my_int_to_str_variable = str(my_int_variable) #el tipo de variable para guardar texto se llama string (str)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

"""
5
5
<class 'str'>
"""

my_bool_variable = False
print(my_bool_variable)

"""El print es capaz de pillar todas esas variables 
#Imprimir un resultado en la consola, 
por lo tanto imprimiria el resultado de una serie 
de acciones realizadas a ese mismo dato"""

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)
"""
La concatenacion nos sirve para muchas cosas,
en especial para mostrar resultados matematicos
"""

# Algunas funciones del sistema
print(len(my_string_variable)) #print no tiene un tipo de dato al ser una funcion
#len cuenta los caracteres de la variable, aqui seria por ejemplo 18

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
"""
Podemos mezclar tipos de datos
"""
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ') #le pedimos el nombre al usuario
print(name) #imprimimos su nombre
print(age) #imprimimos su edad


firts_name = input("Cual es tu nombre?: ")
age = input("How old are you: ")

print(firts_name)
print(age)

#Respuesta

"""
Cual es tu nombre?: Julian
How old are you: 19
Julian
19
"""

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

name = "Julian"
age = 20
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
#Usamos el str o el int para guiarnos
address = True
address = 5
address = 1.2
print(type(address))
