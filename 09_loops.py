# Bucles

# While

mi_condicional = 0

while mi_condicional < 10:
    print(mi_condicional)
    mi_condicional += 2
else: # Es opcional 
    print('Mi condicion es mayor o igual que 10')

print('La ejecuccion continua')

while mi_condicional < 20:
    mi_condicional += 1
    if mi_condicional == 15:
        print('Se detiene la ejecucción')
        break
    print(mi_condicional)

print('La ejeccución continúa')

# For

mi_list = [35, 24, 62, 52, 30, 30, 17]

for element in mi_list:
    print(element)

mi_tupla = (35, 1.77, 'Samuel', 'Rubio')

for element in mi_tupla:
    print(element)

mi_set = {'Samuel', 'Dark', 45}

for element in mi_set:
    print(element)

mi_dict = {'Nombre':'Samuel', 'Apellido': 'Rubio', 'Edad': 18, 1:'Python'}

for element in mi_dict:
    print(element)
    if element == 'Edad':
        break
    print('Se ejecuta')
else:
    print('El bluce for para diccionario ha finalizado')

print('La ejeccución continúa')

for element in mi_dict:
    print(element)
    if element == 'Edad':
        continue 
    print('Se ejecuta')
else:
    print('El bluce for para diccionario ha finalizado')