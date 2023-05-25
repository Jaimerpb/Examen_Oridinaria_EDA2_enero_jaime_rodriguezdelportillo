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

def experimentacion(n):
    lista_pokemon = []
    tipos = ['Fuego', 'Agua', 'Planta', 'Eléctrico', 'Volador', 'Veneno']

    for _ in range(n):
        nombre = ''.join(random.choices(string.ascii_uppercase, k=5))
        tipo = random.choice(tipos)
        pokemon = Pokemon(nombre, tipo)
        lista_pokemon.append(pokemon)

    for pokemon in lista_pokemon:
        pokemon.clasificacion()

    return lista_pokemon

a = experimentacion(5)
