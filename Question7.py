import random

class PokemonManager:
    def __init__(self):
        self.tipos = ['Agua', 'Fuego', 'Tierra', 'Eléctrico', 'Normal', 'Fantasma']
        self.tabla_hash1 = {}
        self.tabla_hash2 = {}

    def generar_pokemon(self):
        self.pokemon = []
        for i in range(800):
            tipo = random.choice(self.tipos)
            nivel = random.randint(1, 100)
            pokemon = Pokemon(tipo, nivel)
            self.pokemon.append(pokemon)

    def cargar_pokemon(self):
        for pokemon in self.pokemon:
            ultimos_digitos = str(pokemon.nivel)[-3:]
            if ultimos_digitos not in self.tabla_hash1:
                self.tabla_hash1[ultimos_digitos] = []
            self.tabla_hash1[ultimos_digitos].append(pokemon)

            inicial_tipo = pokemon.tipo[0]
            if inicial_tipo not in self.tabla_hash2:
                self.tabla_hash2[inicial_tipo] = []
            self.tabla_hash2[inicial_tipo].append(pokemon)

    def eliminar_pokemon(self, tipo, nivel):
        for pokemon in self.pokemon:
            if pokemon.tipo == tipo and pokemon.nivel == nivel:
                ultimos_digitos = str(pokemon.nivel)[-3:]
                self.tabla_hash1[ultimos_digitos].remove(pokemon)
                inicial_tipo = pokemon.tipo[0]
                self.tabla_hash2[inicial_tipo].remove(pokemon)
                self.pokemon.remove(pokemon)
                return True
        return False

    def obtener_pokemon_por_digitos(self, digitos):
        if digitos in self.tabla_hash1:
            return self.tabla_hash1[digitos]
        else:
            return []

    def obtener_pokemon_por_tipo(self, tipo):
        if tipo in self.tabla_hash2:
            return self.tabla_hash2[tipo]
        else:
            return []

    def asignar_mision(self, digitos, mision):
        pokemon_digitos = self.obtener_pokemon_por_digitos(digitos)
        for pokemon in pokemon_digitos:
            pokemon.asignar_mision(mision)

    def buscar_pokemon(self, tipo, nivel):
        for pokemon in self.pokemon:
            if pokemon.tipo == tipo and pokemon.nivel == nivel:
                return True
        return False

class Pokemon:
    def __init__(self, tipo, nivel):
        self.tipo = tipo
        self.nivel = nivel
        self.mision = None

    def asignar_mision(self, mision):
        self.mision = mision

manager = PokemonManager()


manager.generar_pokemon()
manager.cargar_pokemon()

if manager.buscar_pokemon('Fantasma', 187):
    manager.eliminar_pokemon('Fantasma', 187)

manager.asignar_mision('78', 'Misión de Asalto')
manager.as
