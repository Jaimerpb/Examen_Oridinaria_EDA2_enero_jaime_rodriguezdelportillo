import unittest
from Pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self):
        # Crear una lista de Pokémon
        self.pokemon_list = [
            Pokemon("Squirtle", "Agua"),
            Pokemon("Charmander", "Fuego"),
            Pokemon("Bulbasaur", "Planta")
        ]

    def test_clasificacion(self):
        # Recorrer los elementos de la lista y probar el método clasificacion
        for pokemon in self.pokemon_list:
            with self.subTest(pokemon=pokemon):
                self.assertIsNotNone(pokemon)
                pokemon.clasificacion()

if __name__ == "__main__":
    unittest.main()
