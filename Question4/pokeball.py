class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print("¡Se ha creado una Pokeball con éxito!")

    def __str__(self):
        return "Información de la Pokeball:\n" \
               "Peso: {}\n" \
               "Nombre: {}\n" \
               "Precio: {}\n" \
               "Fecha de fabricación: {}\n".format(self.peso, self.nombre, self.precio, self.fecha_fabricacion)


class TablaHashPokeballs:
    def __init__(self):
        self.pokeballs = {}

    def agregar_pokeball(self, pokeball):
        self.pokeballs[pokeball.nombre] = pokeball

    def mostrar_ordenado_por_fecha(self):
        sorted_list = sorted(self.pokeballs.values(), key=lambda x: x.fecha_fabricacion)
        for pokeball in sorted_list:
            print(pokeball)

    def modificar_precio(self, nombre, nuevo_precio):
        if nombre in self.pokeballs:
            self.pokeballs[nombre].precio = nuevo_precio
            print("El precio de la Pokeball '{}' se ha modificado con éxito.".format(nombre))
        else:
            print("No se encontró una Pokeball con el nombre '{}' en la tabla.".format(nombre))


tabla_pokeballs = TablaHashPokeballs()

pokeball1 = Pokeball(0.1, "Pokeball Roja", 200, "2023-05-20")
pokeball2 = Pokeball(0.2, "Pokeball Azul", 300, "2023-05-22")
pokeball3 = Pokeball(0.3, "Pokeball Verde", 250, "2023-05-25")

tabla_pokeballs.agregar_pokeball(pokeball1)
tabla_pokeballs.agregar_pokeball(pokeball2)
tabla_pokeballs.agregar_pokeball(pokeball3)

print("Pokeballs ordenadas por fecha de fabricación:")
tabla_pokeballs.mostrar_ordenado_por_fecha()


tabla_pokeballs.modificar_precio("Pokeball Azul", 350)

print("\nPokeballs ordenadas por fecha de fabricación (después de modificar el precio):")
tabla_pokeballs.mostrar_ordenado_por_fecha()
