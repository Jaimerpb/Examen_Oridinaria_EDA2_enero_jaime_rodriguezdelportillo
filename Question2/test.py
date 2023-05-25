import unittest
from pokemon import pokemon  
class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"Se ha creado el Pokémon {self.nombre} de tipo {self.tipo} con éxito.")
