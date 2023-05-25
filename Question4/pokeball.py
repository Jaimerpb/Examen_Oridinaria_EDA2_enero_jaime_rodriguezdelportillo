import csv
from datetime import datetime

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print("¡Se ha creado una Pokeball con éxito!")

    def __str__(self):
        return f"Información de la Pokeball:\n" \
               f"Peso: {self.peso}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Precio: {self.precio}\n" \
               f"Fecha de fabricación: {self.fecha_fabricacion}\n"

# Crear algunas Pokeballs
pokeball1 = Pokeball(50, "Ultra Ball", 200, datetime(2023, 5, 1))
pokeball2 = Pokeball(30, "Great Ball", 100, datetime(2023, 4, 15))
pokeball3 = Pokeball(20, "Poke Ball", 50, datetime(2023, 6, 1))

pokeballs = [pokeball1, pokeball2, pokeball3]

# Mostrar los datos de las Pokeballs ordenadas por su fecha de fabricación
sorted_pokeballs = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)
for pokeball in sorted_pokeballs:
    print(pokeball)

# Modificar el precio de una Pokeball
pokeball1.precio = 250
print("Precio de la Pokeball 'Ultra Ball' modificado.")

# Crear un archivo CSV con los datos de las Pokeballs
csv_filename = "pokeballs.csv"
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Peso", "Nombre", "Precio", "Fecha de fabricación"])  # Escribir encabezados
    for pokeball in pokeballs:
        writer.writerow([pokeball.peso, pokeball.nombre, pokeball.precio, pokeball.fecha_fabricacion])

print(f"Se ha creado el archivo CSV '{csv_filename}' con los datos de las Pokeballs.")

