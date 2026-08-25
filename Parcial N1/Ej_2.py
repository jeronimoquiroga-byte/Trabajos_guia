from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue

# 1. Definimos la clase para encapsular los datos
class Superhero:
    def __init__(self, name, alias, real_name, bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio  
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name} (Real: {self.real_name}) - Aparición: {self.first_appearance}"

# 2. Funciones de criterio para la clase List 
def by_name(item):
    return item.name

def by_real_name(item):
    # Algunos personajes como Sentinel tienen real_name en None
    return item.real_name if item.real_name is not None else ""

def by_first_appearance(item):
    return item.first_appearance

# 3. Inicializamos la Lista y agregamos los criterios
list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('real_name', by_real_name)
list_heroes.add_criterion('first_appearance', by_first_appearance)

# 4. Cargamos los datos del diccionario a la Lista TDA
for h in superheroes:
    list_heroes.append(
        Superhero(
            h["name"], 
            h["alias"], 
            h["real_name"], 
            h["short_bio"], 
            h["first_appearance"], 
            h["is_villain"]
        )
    )

print("=" * 60)
print("EJERCICIO 2 - REHECHO CON TDAs DE LA CÁTEDRA")
print(f"Total de personajes cargados: {list_heroes.size()}")
print("=" * 60)

# Punto 1: Listado ordenado ascendente por nombre
print("\n1. Listado ordenado por nombre (ascendente):")
list_heroes.sort_by_criterion('name')
list_heroes.show()

# Punto 2: Posición de The Thing y Rocket Raccoon
print("\n2. Posición en la lista (tras ordenar por nombre):")
for nombre in ["The Thing", "Rocket Raccoon"]:
    indice = list_heroes.search(nombre, 'name') 
    if indice is not None:
        print(f"   {nombre} está en la posición: {indice}")

# Punto 3: Listado de villanos
print("\n3. Villanos:")
for hero in list_heroes:
    if hero.is_villain:
        print(f"   {hero.name}")

# Punto 4: Villanos aparecidos antes de 1980
print("\n4. Villanos que aparecieron antes de 1980:")
cola_villanos = Queue()

for hero in list_heroes:
    if hero.is_villain:
        cola_villanos.arrive(hero)

tamanio_cola = cola_villanos.size()
for _ in range(tamanio_cola):
    v = cola_villanos.attention()
    if v.first_appearance < 1980:
        print(f"   {v.name} ({v.first_appearance})")
    
    cola_villanos.arrive(v)

# Punto 5: Superhéroes que comienzan con Bl, G, My, W
print("\n5. Superhéroes que comienzan con Bl, G, My o W:")
# Usamos el método nativo de la clase List 
list_heroes.filter_start_with(('Bl', 'G', 'My', 'W'))

# Punto 6: Ordenado por nombre real (ascendente)
print("\n6. Ordenado por nombre real:")
list_heroes.sort_by_criterion('real_name')
list_heroes.show()

# Punto 7: Ordenado por fecha de aparición
print("\n7. Ordenado por fecha de aparición:")
list_heroes.sort_by_criterion('first_appearance')
list_heroes.show()

# Punto 8: Modificar nombre real de Ant Man
print("\n8. Modificar nombre real de Ant Man:")
indice_antman = list_heroes.search("Ant Man", 'name')
if indice_antman is not None:
    print(f"   Antes: {list_heroes[indice_antman].real_name}")
    list_heroes[indice_antman].real_name = "Scott Lang"
    print(f"   Después: {list_heroes[indice_antman].real_name}")

# Punto 9: Biografías con 'time-traveling' o 'suit'
print("\n9. Personajes con 'time-traveling' o 'suit' en su biografía:")
# Método nativo de la clase List del profesor.
list_heroes.filter_contain_on_bio(['time-traveling', 'suit'])

# Punto 10: Eliminar Electro y Baron Zemo
print("\n10. Eliminar Electro y Baron Zemo:")
for villano in ["Electro", "Baron Zemo"]:
    eliminado = list_heroes.delete_value(villano, 'name')
    if eliminado:
        print(f"   Eliminado exitosamente: {eliminado.name}")
    else:
        print(f"   No se encontró a {villano} para eliminar.")

