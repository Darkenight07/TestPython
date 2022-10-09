# Strings

from msilib.schema import PublishComponent
from re import A


mi_string = "Mi String"
mi_otro_string = 'Mi String'

print(len(mi_string))

nueva_lilnea_string = "Este es un string\ncon salto de linea"
print(nueva_lilnea_string) 

tab_string = "\tEste es un string con tabulador"
print(tab_string)

mi_scape_string = "\t Este es un string \n escapado"
print(mi_scape_string)

# Formateo

name, surname, age = 'Samuel Rubio', 'Darkenight07', 18

print("Mi nombre es {} mi alias es {} y tengo {}".format(name, surname, age))
print("Mi nombre es %s mi alias es %s y tengo %s" %(name, surname, age))
print(f"Mi nombre es {name} mi alias es {surname} y tengo {age}")


# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language

print(a)
print(b)

# Division

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reversa

reverse_language = language[::-1]
print(reverse_language)

# Funciones del sistema


print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
    # print("1".isnumeric()) para saber si es numerico
print(language.lower())
print(language.upper().isupper()) # isupper para saber si esta en mayusculas
print(language.startswith("py"))