# Listas

mi_list = list() # 1 forma
mi_otra_lista = [] # 2 forma

print(len(mi_list))

mi_list = [18, 35, 52, 62, 30, 17, 18]

print(mi_list)
print(len(mi_list))


mi_otra_lista = [35, 1.77, "Samuel", 'Rubio']

print(type(mi_list))
print(mi_otra_lista[1])


print(mi_list.count(18)) # cuenta las veces que esta repetida el numero

age, altura, name, surname, = mi_otra_lista
print(name)

# Concatenar listas
"""

print(mi_list + mi_otra_lista)

"""

mi_otra_lista.insert(1, 'Azul') # lo mete en la posicion 1
print(mi_otra_lista)

mi_otra_lista.remove('Azul') # elimina azul, se puede numeros que coincidan
print(mi_otra_lista)

print(mi_list.pop()) # elimina el ultimo
print(mi_list)

print(mi_list.pop(2)) # elimina la posicion 2
print(mi_list)

del mi_list[2] # elimina en uno en concreto
print(mi_list)

mi_nueva_lista = mi_list.copy() # copia una lista y lo almacena en una variable
print(mi_nueva_lista)

mi_nueva_lista.sort() # ordena los numeros como el comando sort del cmd
print(mi_nueva_lista)

print(mi_nueva_lista[0:2])