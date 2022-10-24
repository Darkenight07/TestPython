# Funciones

def MiFuncion ():
    print('Esto es una funcion')

MiFuncion()

def sum_dos_valores (primer_valor, segundo_valor):
    print(primer_valor + segundo_valor)

sum_dos_valores(5, 7)
sum_dos_valores(5232, 7334)
sum_dos_valores(1.4, 5.2)

def sum_dos_valores_con_return (primer_valor, segundo_valor):
    mi_sum = primer_valor + segundo_valor
    return mi_sum

mi_resultado = sum_dos_valores(1.4, 5.2)
print(mi_resultado)

mi_resultado = sum_dos_valores_con_return(10, 5)
print(mi_resultado)

def print_name (name, surname):
    print(f'{name} {surname}')

print_name(surname ='Rubio', name ='Samuel')

def print_name_con_default (name, surname, alias = 'Sin alias'):
    print(f'{name} {surname} {alias}')

print_name_con_default('Samuel', 'Rubio')

def print_uppertexts(*texts): # Con (*) se puede utilizar parametros ilimitados
    for text in texts:
        print(text.upper())

print_uppertexts('Hola', 'Python', 'Dark')
print_uppertexts('Samuel')