import random

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f'Pokemon {self.nombre} se ha creado con éxito')

    def clasificacion(self):
        print(f'Clasificación del Pokemon {self.nombre}:')
        print(f'Nombre: {self.nombre}')
        print(f'Tipo: {self.tipo}')
        print('PS, Ataque, Defensa, Ataque Especial, Defensa Especial y Velocidad')


