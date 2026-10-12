from list_ import List

class Superhero:
    def __init__(self, name, year, house, bio):
        self.name = name
        self.year = year
        self.house = house
        self.bio = bio # Debe llamarse 'bio' para que list_.py lo filtre bien

    def __str__(self):
        return f"{self.name} ({self.house}) - {self.year}"

# Inicializamos el TDA y sus criterios
lista_heroes = List()
lista_heroes.add_criterion('name', lambda x: x.name)
lista_heroes.add_criterion('year', lambda x: x.year)

# Datos de prueba base para que el ejercicio corra
datos = [
    {"name": "Linterna Verde", "year": 1940, "house": "DC", "bio": "Anillo de poder."},
    {"name": "Wolverine", "year": 1974, "house": "Marvel", "bio": "Garras de adamantium."},
    {"name": "Dr. Strange", "year": 1963, "house": "DC", "bio": "Hechicero supremo."}, # Puesto en DC a propósito
    {"name": "Iron Man", "year": 1963, "house": "Marvel", "bio": "Armadura tecnológica."},
    {"name": "Capitana Marvel", "year": 1967, "house": "Marvel", "bio": "Poderes cósmicos."},
    {"name": "Mujer Maravilla", "year": 1941, "house": "DC", "bio": "Princesa amazona."},
    {"name": "Flash", "year": 1940, "house": "DC", "bio": "Hombre más rápido."},
    {"name": "Star-Lord", "year": 1976, "house": "Marvel", "bio": "Líder de los guardianes."},
    {"name": "Batman", "year": 1939, "house": "DC", "bio": "Traje de murciélago."},
    {"name": "Spiderman", "year": 1962, "house": "Marvel", "bio": "Sentido arácnido."}
]

for d in datos:
    lista_heroes.append(Superhero(d['name'], d['year'], d['house'], d['bio']))

print("--- EJERCICIO 6 ---")

print("\na. Eliminar Linterna Verde:")
lista_heroes.delete_value("Linterna Verde", 'name')
print("Eliminado.")

print("\nb. Año de aparición de Wolverine:")
idx = lista_heroes.search("Wolverine", 'name')
if idx is not None: print(f"Año: {lista_heroes[idx].year}")

print("\nc. Cambiar casa de Dr. Strange a Marvel:")
idx = lista_heroes.search("Dr. Strange", 'name')
if idx is not None:
    lista_heroes[idx].house = "Marvel"
    print(f"Dr. Strange ahora pertenece a: {lista_heroes[idx].house}")

print("\nd. Biografía con 'traje' o 'armadura':")
lista_heroes.filter_contain_on_bio(["traje", "armadura"])

print("\ne. Fecha de aparición anterior a 1963:")
for h in lista_heroes:
    if h.year < 1963:
        print(f"{h.name} - {h.house}")

print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    idx = lista_heroes.search(name, 'name')
    if idx is not None: print(f"{name}: {lista_heroes[idx].house}")

print("\ng. Información de Flash y Star-Lord:")
for name in ["Flash", "Star-Lord"]:
    idx = lista_heroes.search(name, 'name')
    if idx is not None: print(lista_heroes[idx])

print("\nh. Comienzan con B, M y S:")
lista_heroes.filter_start_with(('B', 'M', 'S'))

print("\ni. Cantidad por casa de cómic:")
conteo = {"Marvel": 0, "DC": 0}
for h in lista_heroes:
    if h.house in conteo:
        conteo[h.house] += 1
print(f"Marvel: {conteo['Marvel']} | DC: {conteo['DC']}")