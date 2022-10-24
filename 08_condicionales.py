# Condicionales

mi_condicional = False

if mi_condicional: # Es lo mismo if mi_condicional == False:
    print('Se ejecuta la condicion del if')

mi_condicional = 5 * 5

if mi_condicional > 10 and mi_condicional < 20:
    print('Es mayor que 10 y menor que 20')
elif mi_condicional == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor que 20 o igual que 20 o distinto de 25')


print('La ejecuccion continua')


mi_string = ''

if not mi_string:
    print('Mi cadena de texto es vacia ')

if mi_string == 'Mi cadena de textooooooo':
    print('Estas cadenas de texto coinciden')