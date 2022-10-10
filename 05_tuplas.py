# Tuplas, son listas pero no son modificables 

mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (35, 1.77, 'Samuel', 'Rubio')
mi_otra_tupla = (35, 60, 30)

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla.count('Samuel'))

print(mi_tupla.index('Rubio')) # te dice en que posicion esta

# mi_tupla[1] = 1.80  no deja, no es posible con una tupla

mi_sum_tupla = mi_tupla + mi_otra_tupla
print(mi_sum_tupla)

print(mi_sum_tupla[3:6])

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla[3] = 'Darkenight07'
mi_tupla.insert(1, 'Azul')
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

del mi_tupla
# print(mi_tupla)