# Este juego consiste en calcular una resistencia electrica mediante el codigo de colores
from PIL import Image # De el modulo de PIL e importa Imagen para poder mostrar imagenes

image_1 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\1ejercicio.jpg') # Con esto podemos mostrar una imagen
image_1.show()

print('En la imagen que se acaba de mostrar en tu visor de imagenes de Windows. Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r1 = int(input('Introduce un valor: ')) #4700

puntos = 100 # Creamos una variable que tenga de salida 100 puntos

# Funcion que identifica si los puntos que hemos elegido son correctos o no y en funcion de si esta bien o no 
# suma +10 o resta -10

def Valor(valorp,numrespuesta,puntos):
    if numrespuesta == valorp:
        puntos = 10 + puntos
        print('Has acertado')
        print(f'Tienes {puntos} puntos')
        return puntos
    else:
        puntos = 10 - puntos
        print('Lamentablemente no has acertado')
        puntos = puntos * -1 # Convierte un numero negativo a numero positivo, en caso que en la variable 'puntos' el numero sea ej: -567 pasa a 567
        print(f'Tienes {puntos} puntos')
        return puntos

punto_n_1 = Valor(4700,r1,100)

image_2 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\2ejercicio.jpg')
image_2.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r2 = int(input('Introduce un valor: ')) # 560000

punto_n_2 = Valor(560000,r2,punto_n_1)

image_3 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\3ejercicio.jpg')
image_3.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r3 = int(input('Introduce un valor: ')) # 47000

punto_n_3 = Valor(47000,r3,punto_n_2)

image_4 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\4ejercicio.jpg')
image_4.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r4 = int(input('Introduce un valor: ')) # 1000000

punto_n_4 = Valor(1000000,r3,punto_n_3)

image_5 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\5ejercicio.jpg')
image_5.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r5 = int(input('Introduce un valor: ')) # 1000

punto_n_5 = Valor(1000,r3,punto_n_4)

image_6 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\6ejercicio.jpg')
image_6.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r6 = int(input('Introduce un valor: ')) #22

punto_n_6 = Valor(22,r3,punto_n_5)

image_7 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\7ejercicio.jpg')
image_7.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r7 = int(input('Introduce un valor: ')) # 47

punto_n_7 = Valor(47,r3,punto_n_6)

image_8 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\8ejercicio.jpg')
image_8.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r8 = int(input('Introduce un valor: ')) # 390

punto_n_8 = Valor(390,r3,punto_n_7)

image_9 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\9ejercicio.jpg')
image_9.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r9 = int(input('Introduce un valor: ')) # 470

punto_n_9 = Valor(470,r3,punto_n_8)

image_10 = Image.open('D:\\Documentos\Samuel\\algo\\ProgramaJuego\\10ejercicio.jpg')
image_10.show()

print('Por sus colores ¿Qué valor tiene esta resistencia? (Sin tolerancia)')

r10 = int(input('Introduce un valor: ')) # 22000

punto_n_10 = Valor(22000,r3,punto_n_9)
# Imprime el resultado final del juego
print(f'Los puntos finales son {punto_n_10}')
