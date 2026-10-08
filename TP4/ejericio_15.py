from list_ import List

class Pokemon:
    def __init__(self, name, level, type_, subtype):
        self.name = name
        self.level = level
        self.type = type_
        self.subtype = subtype

    def __str__(self):
        return f"{self.name} (Nv {self.level}) - {self.type}/{self.subtype}"

class Trainer:
    def __init__(self, name, tournaments_won, battles_lost, battles_won):
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_lost = battles_lost
        self.battles_won = battles_won
        
        # Sublista TDA
        self.pokemons = List()
        # Claves únicas para no pisar el diccionario general de list_.py
        self.pokemons.add_criterion('poke_name', lambda x: x.name)
        self.pokemons.add_criterion('poke_level', lambda x: x.level)

    def __str__(self):
        return f"[{self.name}] Torneos: {self.tournaments_won} | Batallas (G: {self.battles_won}, P: {self.battles_lost})"

# Inicializamos lista principal
entrenadores = List()
entrenadores.add_criterion('trainer_name', lambda x: x.name)
entrenadores.add_criterion('trainer_tournaments', lambda x: x.tournaments_won)

# Datos de prueba
t1 = Trainer("Ash", 5, 20, 100)
t1.pokemons.append(Pokemon("Pikachu", 90, "Eléctrico", ""))
t1.pokemons.append(Pokemon("Charizard", 85, "Fuego", "Volador"))
t1.pokemons.append(Pokemon("Wingull", 20, "Agua", "Volador"))

t2 = Trainer("Red", 10, 5, 200)
t2.pokemons.append(Pokemon("Venusaur", 90, "Planta", "Veneno"))
t2.pokemons.append(Pokemon("Charizard", 92, "Fuego", "Volador"))
t2.pokemons.append(Pokemon("Pikachu", 10, "Eléctrico", "")) # Pikachu repetido

t3 = Trainer("Misty", 2, 10, 45)
t3.pokemons.append(Pokemon("Starmie", 60, "Agua", "Psíquico"))
t3.pokemons.append(Pokemon("Wingull", 30, "Agua", "Volador"))

entrenadores.append(t1)
entrenadores.append(t2)
entrenadores.append(t3)

print("--- EJERCICIO 15 ---")

print("\na. Cantidad de Pokémons de Ash:")
idx = entrenadores.search("Ash", "trainer_name")
if idx is not None: print(entrenadores[idx].pokemons.size())

print("\nb. Entrenadores con más de 3 torneos ganados:")
for t in entrenadores:
    if t.tournaments_won > 3: print(t.name)

print("\nc. Pokémon de mayor nivel del entrenador con más torneos:")
entrenadores.sort_by_criterion("trainer_tournaments")
mejor = entrenadores[-1] # Como ordena ascendente, el último es el mayor
mejor.pokemons.sort_by_criterion("poke_level")
print(f"{mejor.name} -> {mejor.pokemons[-1]}")

print("\nd. Datos de Misty y sus Pokémons:")
idx = entrenadores.search("Misty", "trainer_name")
if idx is not None:
    print(entrenadores[idx])
    entrenadores[idx].pokemons.show()

print("\ne. Entrenadores con batallas ganadas > 79%:")
for t in entrenadores:
    total_batallas = t.battles_won + t.battles_lost
    if total_batallas > 0:
        win_rate = (t.battles_won / total_batallas) * 100
        if win_rate > 79: print(f"{t.name} ({win_rate:.1f}%)")

print("\nf. Entrenadores con (Fuego y Planta) O (Agua/Volador):")
for t in entrenadores:
    fuego = planta = agua_volador = False
    for p in t.pokemons:
        if p.type.lower() == "fuego": fuego = True
        if p.type.lower() == "planta": planta = True
        if p.type.lower() == "agua" and p.subtype.lower() == "volador": agua_volador = True
    if (fuego and planta) or agua_volador:
        print(t.name)

print("\ng. Promedio de nivel de Pokémons de Red:")
idx = entrenadores.search("Red", "trainer_name")
if idx is not None:
    t = entrenadores[idx]
    if t.pokemons.size() > 0:
        promedio = sum(p.level for p in t.pokemons) / t.pokemons.size()
        print(f"{promedio:.1f}")

print("\nh. Cuántos entrenadores tienen a Pikachu:")
contador = 0
for t in entrenadores:
    if t.pokemons.search("Pikachu", "poke_name") is not None:
        contador += 1
print(contador)

print("\ni. Entrenadores con Pokémons repetidos:")
for t in entrenadores:
    nombres_vistos = set()
    for p in t.pokemons:
        if p.name in nombres_vistos:
            print(t.name)
            break
        nombres_vistos.add(p.name)

print("\nj. Entrenadores con Tyrantrum, Terrakion o Wingull:")
buscados = ["Tyrantrum", "Terrakion", "Wingull"]
for t in entrenadores:
    for p in t.pokemons:
        if p.name in buscados:
            print(t.name)
            break # Si ya encontramos uno, pasamos al siguiente entrenador

print("\nk. Comprobar si Ash tiene a Charizard:")
entrenador_x = "Ash"
pokemon_y = "Charizard"

idx_t = entrenadores.search(entrenador_x, "trainer_name")
if idx_t is not None:
    t = entrenadores[idx_t]
    idx_p = t.pokemons.search(pokemon_y, "poke_name")
    if idx_p is not None:
        print("¡Lo tiene!")
        print(t)
        print(t.pokemons[idx_p])
    else:
        print("No lo tiene.")