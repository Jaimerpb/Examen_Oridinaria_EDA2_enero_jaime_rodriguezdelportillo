class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"Se ha creado el Pokémon {self.nombre} de tipo {self.tipo} con éxito.")

    def clasificacion(self):
        clasificacion_dict = {
            "Agua": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"],
            "Fuego": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"],
            "Tierra": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"],
            "Eléctrico": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"],
            "Normal": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"],
            "Fantasma": ["PS", "Ataque", "Defensa", "Ataque Especial", "Defensa Especial", "Velocidad"]
        }
        if self.tipo in clasificacion_dict:
            print("Clasificación:")
            for atributo in clasificacion_dict[self.tipo]:
                print("-", atributo)
        else:
            print("Tipo de Pokémon desconocido.")




