# Clases

class MyEmptyPerson:
    pass # Hace que no hay error con class, cunado no hay contenido

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name} {surname} {alias}' # Propiedad publica
        self._name = name # Propiedad privada

    def get_name (self):
        return self._name

    def walk (self):
        print(f'{self.full_name} está caminando')

mi_person = Person('Samuel', 'Dark')
print(mi_person.full_name)
print(mi_person.get_name())
mi_person.walk()

mi_otra_persona = Person('Samuel', 'Rubio','Dark' )
print(mi_otra_persona.full_name)
mi_otra_persona.walk()


mi_otra_persona.full_name = 'Hector de Leon El loco de los perros' 
print(mi_otra_persona.full_name)

mi_otra_persona.full_name = 545  # Puedes cambiar el dato como nos de la gana.
print(mi_otra_persona.full_name)
