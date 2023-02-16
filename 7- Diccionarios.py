                                      ##### Diccionarios #######

my_dic = dict()
my_other_dict = {}

# Ya tenes un tipo de dato dict

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
# Tenemos una relacion de clave-->valor asi como en sql
# ------- una estructura para relacionar datos, como un JSON
# Tenemos una gran facilidad para acceder a los datos
my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    # Con las claves accedemos a los datos para consultarlos
    "Lenguajes": {"Python", #Estos serian como los sub objetos en js
                  "Swift", 
                  "Kotlin"}, 
    1: 1.77 
}

print(my_dic["Nombre"]) # Imprime Brais
print(my_dic["Apellido"]) # Imprime Moure
print(my_dic["Edad"]) # Imprime 35
print(my_dic[1]) # Imprime 1.77

my_dic["Nombre"] = "Julian" # Modifico el valor de la clave nombre
my_dic["Calle"] = "JuliDev" # Agrego un nuevo campo con un nuevo valor
del my_dic["Calle"] # Cuando le paso del al dic accediendo al elemento el mismo se borra

print("Moure" in my_dic)
# Siempre va a buscar por clase y no por valor
print("Apellido" in my_dic)
# Nos retorna el valor false

my_dic.items() # Tenemos un listado con cada uno de los items
my_dic.keys() # Imprime solo las claves como apellido, edad, etc
my_dic.values() # Imprime los valores de las claves como Brais, 35, etc

## USO del Fromkeys

my_new_dic = dict.fromkeys(("Nombre", 1, "Piso"))
# Creamos un nuevo diccionario usando la palabra reservada

## Otras operaciones

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

# Cuando transformamos el diccionario en una lista solo tenemos las claves, no el valor

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values()) 
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
