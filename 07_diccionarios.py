# Diccionarios

mi_dict = dict()
mi_otro_dict = {}

print(type(mi_dict))
print(type(mi_otro_dict))

mi_otro_dict = {'Nombre':'Samuel', 'Apellido': 'Rubio', 'Edad': 18, 1:'Python'}


mi_dict = {
    'Nombre':'Samuel',
    'Apellido': 'Rubio',
    'Edad': 18,
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.77
    }

print(mi_otro_dict)
print(mi_dict['Nombre']) #Prueba antes
mi_dict['Nombre'] = 'Pedro' # Renombra el valor de la clave

print(mi_dict['Nombre']) 

print(mi_dict[1])

mi_dict['Calle'] = 'Calle Dark' # Añade un nueva clave, valor
print(mi_dict)

del mi_dict['Calle']
print(mi_dict)

print('Samuel' in mi_dict) # Estamos buscando la clave, no valor
print('Apellido' in mi_dict)

print(mi_dict.items()) # Muestra agrupadando las claves y valores entre ()
print(mi_dict.keys()) # Muestra solo las claves
print(mi_dict.values()) # Muestra solo los valores


mi_nuevo_dict = dict.fromkeys(("Nombre", 1, 'Piso'))
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(mi_dict)
print(mi_nuevo_dict)

mi_nuevo_dict = dict.fromkeys(mi_dict, 'Samuel')
print(mi_nuevo_dict)

mi_values = mi_nuevo_dict.values()
print(type(mi_values))

print(mi_nuevo_dict.values())
print(list(mi_nuevo_dict.values()))
print(tuple(mi_nuevo_dict))
print(set(mi_nuevo_dict))