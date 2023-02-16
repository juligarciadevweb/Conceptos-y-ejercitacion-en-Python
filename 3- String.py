                                                      #####Strings######

mi_string = "Mi string"
my_other_string= "Mi otra cadena"

print(len(mi_string))
# Cuenta los caracteres que tiene
print(len(my_other_string))

print(mi_string + " " + my_other_string)
# Realizamos una concatenacion con un espacio en el medio

new_string_con_salto = "Voy a saltar\nla linea" # Pegamos todo asi no queden espacios
print(new_string_con_salto)
"""
Da como respuesta:
Voy a saltar
la linea
"""
tab_string = "\tEste es un string de tabulacion"
print(tab_string) # Deja un espacio al lado 
"""
Da como respuesta: 
    Este es un string de tabulacion
"""

scape_str = "\tEste es un strinng escapado\nde la linea"
print(scape_str)
"""
Da como respuesta:
    Este es un strinng escapado
de la linea 
"""

# Formateo

name, surname, age = "Brais", "Moure", 18
print("Mi nombre es {}, mi apellido es {} y mi edad es {}". format(name, surname, age))
# Con el %s le paso la primera cadena de texto
# Uso el %d para numeros enteros 
# Se usan las llaves si quiero imprimir directamente el objeto como lo tengo estructurado al principio
# Lo que hacemos es ir sustituyendo el nombre, el apellido y la edad dentro de un string
print("Mi nombre es %s, mi apellido es %s y mi edad es %d" %(name, surname, age))
# Le debemos pasar el dato especifico que nos pide

# Inferencia de datos

print(f"Mi nombre es {name}, mi apellido es {surname} y mi edad es {age}")
"""
Formatted string literals (también llamados f-strings para abreviar) 
le permiten incluir el valor de las expresiones de Python 
dentro de una cadena prefijando la cadena con f o F y escribiendo expresiones como {expresion}.
Es de las formas mas factibles de realizar esto
"""

# Desempaquetado de paquetes

"""
Esto me hace acordar al conteo de indices en js
empezamos desde 0 pero en vez de eso va poniendo las letras
"""

lenguage = "python"
a, b, c, d, e, f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

"""
Nos da como respuesta:

p
y
t
h
o
n
"""

# Division

language_style = lenguage[1:3]
print(language_style)
"""
Nos da como respuesta:
yt
"""
language_style = lenguage[1:]
print(language_style)
"""
Empezamos a contar desde el 0(P)
Nos da como respuesta:
ython
"""
language_style = lenguage[-2]
print(language_style)
# Nos acaba imprimiendo la o
    
# Reverse

reversed_lan = lenguage[::-1]
print(reversed_lan)
"""
Nos da como respuesta nohtyP
"""

# Funciones del lenguaje

print(lenguage.capitalize())
#Pone la primera letra del string en mayuscula
print(lenguage.upper())
#Aparece el string completamente en mayuscula
print(lenguage.count("t"))
# Cuantas x letras tiene
print(lenguage.isnumeric())
# Pregunta si la variable es un numero, res con false or true
print("1".isnumeric())
print(lenguage.lower())
# Hace todas las letras minusculas
print(lenguage.lower().isupper())
# Isupper es para comprobar si esta en mayuscula, es verdadero
"""
Salidas por consola:

Python
PYTHON
1
False
True
python
False
"""
print(lenguage.startswith("Py"))
# 
print("Py" == "py")  # No es lo mismo

