from graph import Graph

g = Graph(is_dir=False)

# a. Cargar nodos con sus tipos[cite: 2]
nodos = [
    ("Ubuntu", "pc"), ("Debian", "notebook"), ("Red Hat", "notebook"),
    ("Manjaro", "pc"), ("Fedora", "pc"), ("Parrot", "pc"), ("Arch", "notebook"),
    ("Guaraní", "servidor"), ("MongoDB", "servidor"),
    ("Switch 1", "switch"), ("Switch 2", "switch"),
    ("Router 1", "router"), ("Router 2", "router"), ("Router 3", "router"),
    ("Impresora", "impresora")
]

for nombre, tipo in nodos:
    g.add_vertex(nombre, other_values={"tipo": tipo})

# Cargar aristas (conexiones y distancias/pesos según la imagen)[cite: 2]
aristas = [
    (18, "Ubuntu", "Switch 1"), (17, "Debian", "Switch 1"),
    (22, "Switch 1", "Impresora"), (29, "Switch 1", "Router 1"),
    (25, "Red Hat", "Router 2"), (9, "Guaraní", "Router 2"),
    (37, "Router 2", "Router 1"), (50, "Router 2", "Router 3"),
    (43, "Router 1", "Router 3"), (40, "Manjaro", "Switch 2"),
    (12, "Parrot", "Switch 2"), (3, "Fedora", "Switch 2"),
    (56, "Arch", "Switch 2"), (5, "MongoDB", "Switch 2"),
    (61, "Switch 2", "Router 3")
]

for peso, origen, destino in aristas:
    g.add_edge(peso, origen, destino)

def extraer_camino(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        return None, float('inf')
    paths = grafo.dijkstra(origen)
    peso_total = None
    camino = []
    dest_actual = destino
    while paths.size() > 0:
        paso = paths.pop()
        if paso[0] == dest_actual:
            if peso_total is None:
                peso_total = paso[1]
            camino.append(paso[0])
            dest_actual = paso[2]
    camino.reverse()
    return camino, peso_total

print("="*50)
print("b. Barrido desde notebooks (Red Hat, Debian, Arch)[cite: 2]")
for nb in ["Red Hat", "Debian", "Arch"]:
    print(f"\n--- Desde {nb} ---")
    # Nota: Si tu TDA tiene depth_show, descomentalo. Por defecto usamos amplitude_show.
    # g.depth_show(nb) 
    g.amplitude_show(nb)

print("\n" + "="*50)
print("c. Camino más corto a la impresora desde Manjaro, Red Hat, Fedora[cite: 2]")
for origen in ["Manjaro", "Red Hat", "Fedora"]:
    camino, peso = extraer_camino(g, origen, "Impresora")
    print(f"Desde {origen}: {' -> '.join(camino)} (Costo: {peso})")

print("\n" + "="*50)
print("d. Árbol de expansión mínima[cite: 2]")
# Tomamos el Router 1 como origen cualquiera para el árbol
print(g.kruskal("Router 1"))

print("\n" + "="*50)
print("e. PC con el camino más corto al servidor Guaraní[cite: 2]")
pcs = [n for n, t in nodos if t == "pc"]
menor_peso = float('inf')
mejor_pc = ""
for pc in pcs:
    camino, peso = extraer_camino(g, pc, "Guaraní")
    if peso < menor_peso:
        menor_peso = peso
        mejor_pc = pc
print(f"La PC más cercana es {mejor_pc} con un costo de {menor_peso}")

print("\n" + "="*50)
print("f. Computadora del Switch 1 con camino más corto a MongoDB[cite: 2]")
# Las computadoras conectadas al Switch 1 son Ubuntu y Debian
comps_s1 = ["Ubuntu", "Debian"]
menor_peso_s1 = float('inf')
mejor_comp_s1 = ""
for comp in comps_s1:
    camino, peso = extraer_camino(g, comp, "MongoDB")
    if peso < menor_peso_s1:
        menor_peso_s1 = peso
        mejor_comp_s1 = comp
print(f"La computadora más cercana desde Switch 1 es {mejor_comp_s1} con un costo de {menor_peso_s1}")

print("\n" + "="*50)
print("g. Cambiar conexión de impresora a Router 2 y re-hacer punto b[cite: 2]")
g.delete_edge("Switch 1", "Impresora")
g.add_edge(20, "Router 2", "Impresora") # Asignamos un peso de 20 como ejemplo
for nb in ["Red Hat", "Debian", "Arch"]:
    print(f"\n--- Nuevo barrido desde {nb} ---")
    g.amplitude_show(nb)