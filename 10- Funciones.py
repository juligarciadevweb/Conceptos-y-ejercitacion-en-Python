                                  ##### Functions ######

# Definicion
def my_function ():
   print("Esta es mi primera funcion")
   # Solo imprime un texto en la consola
   
my_function() # Estas invocando a la funcion
# Siempre la invocas fuera de la funcion

# No hace falta especificar el tipo de dato
def sum_two_values(first_number, second_number): # Parametro de entrada
   print(first_number + second_number) # Parametro de salida
   
sum_two_values(7, 5) # Pasas los parametros SIEMPRE con la PUTA ,
sum_two_values(888, 25) 
sum_two_values("6", "9") # Hace una concatenacion de strings

def sum_two_values_whith_return(first_number, second_number):
   return first_number + second_number
   
my_result = sum_two_values_whith_return(8, 9)
print(my_result) # Imprime el resultado desde la variable

def imprimir_Nombre(name, surname): # NUNCA te olvides de los :
   print(f"{name} {surname}")
   # Con la F le damos un formato, los interpretara como texto en este caso
   
imprimir_Nombre("Guille", "Garcia") # NUNCA te olvides de las "comillas" de los arrays
imprimir_Nombre(name = "Guille", surname ="Garcia")
# Podemos reordenar especificamente lo que imprime la consola

def imprimir_Nombre_default(name, surname, alias = "No tiene alias"): 
   # A alias le podemos dar un valor por defecto
   print(f"{name} {surname} {alias}")

imprimir_Nombre_default("Juli", "Galardino", ) # Se imprimira con "No tiene alias"
imprimir_Nombre_default("Juli", "Galardino", "JuliDev") # Se imprimira con el alias solicitado

# Funcion con for
def print_upper_texts(*texts): # Podemos repetir los parametros
   print(type(texts)) # Imprime el tipo
   # Internamente lo interpretara como una tupla xq 
   # Ya que le estamos pasando valores concatenados
   for text in texts: # Para los textos en la funcion 
      print(text.upper()) # Va a ponerlos a todos en mayuscula
   
print_upper_texts("Hola", "Java", "JuliDev")
