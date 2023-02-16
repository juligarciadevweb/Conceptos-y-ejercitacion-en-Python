                                      ###### Loops ######

# Son como los ciclos, bucles, etc. 
# Nos sirven para pasar por el mismo codigo varias veces

## While ##

my_condition = 0

while my_condition < 10: # Esta atado a que se cumpla una condicion
    print(my_condition)
    my_condition += 2 
    # Imprimira numeros de 2 en 2 hasta llegar al 10 y se cumpla la condicion llegando a 8
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")
    # Vamos controlando lo que hace el while
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15: # Vamos mezclando los ciclos
        print("Se detiene la ejecución")
        break # El 15 es el break point, ahi termina la ejecucion del ciclo
    print(my_condition)

print("La ejecución continúa")

### For ###

# Nos sirve para realizar ciertas acciones en un grupo de elementos

my_list = [35, 24, 62, 52, 31, 30, 17]

for element in my_list:
   print(element)
   # El for se repetira tantas veces como elementos tengamos iterables

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
   print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
   print(element)
   
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

# Cuando le metemos un for a un diccionario va imprimiendo todos los valores
# Solo con el siguiente ciclo
for element in list(my_dict.values()): 
   print(element) # Imprime los valores
   
for element in my_dict:
   print(element) # Ahora imprime las llaves

for element in my_dict:
    print(element)
    if element == "Edad": # Si aparece esta clave se para el ciclo
        break
    # Cuando rompemos el bucle el else no significa nada
else:
    print("El bluce for para diccionario ha finalizado")
    
for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Aunque encuentre la llave edad, el ciclo va a continuar
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
    # Si no encuentra la llave imprimira esto
    
