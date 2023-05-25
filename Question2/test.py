import unittest
from pokemon import pokemon  
class TestPokemon(unittest.TestCase):
    def test_clasificacion_agua(self):
        pokemon = Pokemon("Squirtle", "Agua")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Agua")

    def test_clasificacion_fuego(self):
        pokemon = Pokemon("Charmander", "Fuego")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Fuego")

    def test_clasificacion_tierra(self):
        pokemon = Pokemon("Geodude", "Tierra")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Tierra")

    def test_clasificacion_electrico(self):
        pokemon = Pokemon("Pikachu", "Eléctrico")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Eléctrico")

    def test_clasificacion_normal(self):
        pokemon = Pokemon("Rattata", "Normal")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Normal")

    def test_clasificacion_fantasma(self):
        pokemon = Pokemon("Gengar", "Fantasma")
        self.assertEqual(pokemon.clasificacion(), "Clasificación: Fantasma")

    def test_clasificacion_desconocido(self):
        pokemon = Pokemon("Unknown", "Desconocido")
        self.assertEqual(pokemon.clasificacion(), "Tipo de Pokémon desconocido.")


if __name__ == '__main__':
    unittest.main()
