from super_heroes_data import superheroes

# 1
def buscar_capitan(lista):
    if len(lista) == 0:
        return False
    if lista[0]['name'] == "Captain America": 
        return True
    return buscar_capitan(lista[1:])

# 2
def listar_superheroes(lista):
    if len(lista) == 0:
        return
    print(lista[0]['name'])
    listar_superheroes(lista[1:])

print("Buscando al Capitán América")
if buscar_capitan(superheroes):
    print("El Captain America esta en la lista.")
else:
    print("El Captain America no esta en la lista.")

print("Lista de super heroes")
listar_superheroes(superheroes)


lista = superheroes

# 1
lista.sort(key=lambda x: x['name'])
print("Personajes ordenados por nombre")
for p in lista:
    print(p['name'])

# 2
print("Posiciones")
for i, p in enumerate(lista):
    if p['name'] == "The Thing":
        print(f"The Thing esta en la posicion: {i}")
    if p['name'] == "Rocket Raccoon":
        print(f"Rocket Raccoon esta en la posicion: {i}")

# 3
print("Villanos")
for p in lista:
    if p.get('is_villain') == True:
        print(p['name'])

# 4
print("Villanos aparecidos antes de 1980")
for p in lista:
    if p.get('is_villain') == True and p.get('first_appearance', 0) < 1980:
        print(f"{p['name']} ({p['first_appearance']})")

# 5
print("Superheroes que empiezan con B, G, My, W")
for p in lista:
    if not p.get('is_villain'):
        if p['name'].startswith(("B", "G", "My", "W")):
            print(p['name'])

# 6
def obtener_nombre_real(personaje):
    nombre = personaje.get('real_name')
    if nombre is None:
        return ""
    return nombre

lista.sort(key=obtener_nombre_real)

print("Ordenados por nombre real")
for p in lista:
    print(f"{p['name']} - {p['real_name']}")

# 7
lista.sort(key=lambda x: x['first_appearance'])
print("Ordenados por fecha de aparicion")
for p in lista:
    print(f"{p['name']} ({p['first_appearance']})")

# 8
for p in lista:
    if p['name'] == "Ant Man":
        p['real_name'] = "Scott Lang"
        print("Nombre real de Ant Man actualizado a:", p['real_name'])

# 9
print("Personajes con 'time-traveling' o 'suit' en su biografia")
for p in lista:
    bio = p.get('short_bio', '').lower()
    if "time-traveling" in bio or "suit" in bio:
        print(p['name'])

# 10
for nombre in ["Electro", "Baron Zemo"]:
    for p in lista:
        if p['name'] == nombre:
            print(f"Eliminando a: {p['name']}")
            print(f"Información: {p}") 
            lista.remove(p)
            break