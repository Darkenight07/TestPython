# Este juego consiste en calcular una resistencia electrica mediante el codigo de colores
from PIL import Image # Importa el modulo de PIL e importa Imagen para poder mostrar imagenes

puntos = 100 # Creamos una variable que tenga de salida 100 puntos

image_1 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\1ejercicio.jpg') # Con esto podemos mostrar una imagen
image_1.show()

print('En la imagen que se acaba de mostrar en tu visor de imagenes de Windows. Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r1 = int(input('Introduce un valor: '))

if r1 == 4700:
    puntos = 10 + puntos
    print('¡Has acertado! ')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1 # Convierte un numero negativo a numero positivo, en caso que en la variable 'puntos' el numero sea ej: -567 pasa a 567

image_2 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\2ejercicio.jpg')
image_2.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r2 = int(input('Introduce un valor: '))

if r2 == 560000:
    puntos = 10 + puntos
    print('¡Has acertado! ')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

image_3 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\3ejercicio.jpg')
image_3.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r3 = int(input('Introduce un valor: '))

if r3 == 47000:
    puntos = 10 + puntos
    print('¡Has acertado!' )
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

image_4 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\4ejercicio.jpg')
image_4.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r4 = int(input('Introduce un valor: '))

if r4 == 1000000:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

image_5 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\5ejercicio.jpg')
image_5.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r5 = int(input('Introduce un valor: '))

if r5 == 1000:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

image_6 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\6ejercicio.jpg')
image_6.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r6 = int(input('Introduce un valor: '))

if r6 == 22:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

image_7 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\7ejercicio.jpg')
image_7.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r7 = int(input('Introduce un valor: '))

if r7 == 47:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1


image_8 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\8ejercicio.jpg')
image_8.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r8 = int(input('Introduce un valor: '))

if r8 == 390:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1


image_9 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\9ejercicio.jpg')
image_9.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r9 = int(input('Introduce un valor: '))

if r9 == 470:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1


image_10 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\10ejercicio.jpg')
image_10.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r10 = int(input('Introduce un valor: '))

if r10 == 22000:
    puntos = 10 + puntos
    print('¡Has acertado!')
    print(puntos)
else:
    puntos = 10 - puntos
    print('Lamentablemente no has acertado')
    print(puntos)
    puntos = puntos * -1

print(f'Los puntos finales son {puntos}') 
