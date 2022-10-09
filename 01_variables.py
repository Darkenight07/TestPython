# Variables

mi_variable = 'Mi variable string'
print(mi_variable)

mi_int_variable = 5
print(mi_int_variable)
mi_bool_variable = True

mi_int_a_str_variable = str(mi_int_variable)
print(mi_int_a_str_variable)
print(type(mi_int_a_str_variable))

# Concatenacion de variables en un print
print(mi_variable, str(mi_int_a_str_variable), mi_bool_variable)

print('Este es el valor de:', mi_bool_variable)

# Algunas funciones del sistema

print(len(mi_variable)) # mide los caracteres de esa variable

# Variables en una sola linea, hay que tener cuidado!
name, surname, alias, age = 'Samuel', 'Rubio', 'Darkenight07', 18
print('Me llamo: ', name, surname, 'Mi edad es', age, "y mi alias es: ", alias)

# Inputs
""" 
nombre = input("Cual es tu nombre?: ")
edad = input("Cuantos años tienes?: ")

print("Tu nombre es " + nombre)
print('Tu edad es ' + edad)

"""



# ¿Forzamos el tipo?
address: str = "Mi direcciom"
address = 32
print(type(address))