# Sets

mi_set = set()
mi_otro_set = {} # diccionario inicialmente

print(type(mi_set))
print(type(mi_otro_set)) # inicialmente nos pone que es un diccionario

mi_otro_set = {'Samuel', 'Dark', 45} # De esta forma se puede cambiar a tipo set, poniendo datos
print(type(mi_otro_set))

print(len(mi_otro_set))

mi_otro_set.add('Darkenight') 

print(mi_otro_set) # Un set no es una estructura ordenada

mi_otro_set.add('Darkenight') # Un set no admite repetidos

print(mi_otro_set)

print('Dark' in mi_otro_set) # Para saber si hay uno en un set Dark en (set)
print('Darke' in mi_otro_set) 

mi_otro_set.remove("Dark")
print(mi_otro_set)

mi_otro_set.clear() # elimina el contenido, pero no elimina la variable
print(len(mi_otro_set))

del mi_otro_set  # elimina directamente la variable
#print(mi_otro_set)

mi_set = {'Samuel', 'Dark', 45} 
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[1])

mi_otro_set = {'Kotlin', 'Swift', 'Python'}

mi_nueva_set = mi_set.union(mi_otro_set) # Lo une
print(mi_nueva_set.union(mi_nueva_set).union(mi_set).union({'JavaScript', 'C#'})) # Puede añadir elementos nuevos, mirar el final

print(mi_nueva_set.difference(mi_set))