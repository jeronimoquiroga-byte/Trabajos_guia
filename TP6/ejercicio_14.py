from graph import Graph

g = Graph(is_dir=False)

# a. Vértices (Ambientes)[cite: 3]
ambientes = [
    "cocina", "comedor", "cochera", "quincho", 
    "baño 1", "baño 2", "habitación 1", "habitación 2", 
    "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    g.add_vertex(ambiente)

# b. Aristas (Distancias en metros)[cite: 3]
# Regla: Al menos 3 aristas por vértice. Dos vértices con 5 aristas (Cocina y Sala de estar).[cite: 3]
conexiones = [
    # Cocina (5 conexiones)
    (4, "cocina", "comedor"), (6, "cocina", "cochera"), 
    (5, "cocina", "patio"), (3, "cocina", "baño 1"), (7, "cocina", "sala de estar"),
    # Sala de estar (5 conexiones - ya tiene 1 con cocina)
    (4, "sala de estar", "habitación 1"), (5, "sala de estar", "habitación 2"), 
    (3, "sala de estar", "baño 2"), (6, "sala de estar", "terraza"),
    # Resto (Para asegurar mínimo 3 por nodo)
    (5, "comedor", "quincho"), (4, "comedor", "patio"), 
    (6, "cochera", "patio"), (7, "cochera", "quincho"),
    (5, "quincho", "terraza"), 
    (2, "baño 1", "habitación 1"), (3, "baño 1", "habitación 2"),
    (4, "baño 2", "terraza"), (5, "baño 2", "patio"),
    (3, "habitación 1", "habitación 2"),
    (6, "terraza", "patio")
]

for metros, origen, destino in conexiones:
    g.add_edge(metros, origen, destino)

print("="*50)
print("c. Árbol de expansión mínima y metros de cable total[cite: 3]")
# Dependiendo de tu TDA, kruskal devuelve una lista o un string. 
# Lo imprimimos directamente para ver la estructura.
arbol_minimo = g.kruskal("cocina")
print(arbol_minimo)

# Si tu TDA devuelve una lista como ['A-B-2;C-D-3'], la procesamos para sumar:
try:
    if isinstance(arbol_minimo, list):
        conexiones_mst = arbol_minimo[0].split(';')
    else:
        conexiones_mst = arbol_minimo.split(';')
        
    metros_totales = 0
    for conexion in conexiones_mst:
        partes = conexion.split('-')
        if len(partes) == 3: # Origen - Destino - Peso
            metros_totales += int(partes[2])
    print(f"\nTotal de metros de cable necesarios: {metros_totales} metros.")
except:
    print("\nRevisar consola para sumar los pesos del Kruskal manualmente según la salida del TDA.")

print("\n" + "="*50)
print("d. Camino más corto: Habitación 1 a Sala de estar[cite: 3]")
# Reutilizamos la lógica de extracción de camino de Dijkstra
paths = g.dijkstra("habitación 1")
destino = "sala de estar"
peso_total = None
camino = []

while paths.size() > 0:
    paso = paths.pop()
    if paso[0] == destino:
        if peso_total is None:
            peso_total = paso[1]
        camino.append(paso[0])
        destino = paso[2]
        
camino.reverse()
print(f"Camino: {' -> '.join(camino)}")
print(f"Metros de cable de red necesarios: {peso_total} metros[cite: 3]")