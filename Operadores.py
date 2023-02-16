  ####### OPERADORES #######
#Aritmeticas basicas
print(3 + 4)
print(3 * 4)
print(3 - 4)
print(3 / 4)

#Especiales
print(10 % 2) #Esto es para sacar el modulo, aqui nos daria 0
print(10 // 3) #Aquí tenemos una flour division
# Lo que hace es dividir los nros y redondea el resultado decimal a un numero entero
# Daria como respuesta 3
print(2 ** 3) #Calcula un exponente, 2 elevado al cubo
# Daria como respuesta 8
print(2 ** 3 + 7 - 9 / 3 // 20 * 35) # Podemos hacer operaciones combinadas
# Esta nos daria 15.0

print("Hola" + 5) #Esto nos daria error 
#Entre tipos de datos diferentes no se puede programar
print("Hola" + str(5))
"""
Si al 5 le ponemos " se convierte en string
Si lo hacemos con la funcion str va a dar 5
"""
print("Hola " * 5)
# Hola Hola Hola Hola Hola
print("Hola " * (2 * 5) ) # Multiplicar un string por un numero entero
# Hola Hola Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2 # Tengo un dato flotante 5.00
print("Hola " * int(my_float)) # Convierto el flotante en entero
# Respuesta = Hola Hola Hola Hola Hola

#Operadores comparativos

print(3 > 4) # 3 es mayor que 4
print(3 < 4) # 3 es menor que 4
print(3 >= 4) # 3 es mayor o igual a 4
print(4 <= 4) # 4 es menor o igual a 4
print(3 == 4) # 3 es igual a 4
print(3 != 4) # 3 es distinto de 4

## Operaciones con cadenas de texto ##
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
# El programa ordena alfabeticamente en cada uno de los arrays
# Ordena alfabeticamente que tiene en cuenta las mayusculas
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python") 
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))









