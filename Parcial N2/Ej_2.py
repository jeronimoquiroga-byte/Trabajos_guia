from star_wars_data import personajes_sw, relaciones_sw

class Grafo:
    def __init__(self, dirigido=False):
        self.elements = []
        self.dirigido = dirigido

    def insert_vertex(self, dato):
        if not self.buscar_vertice(dato):
            self.elements.append({"info": dato, "aristas": []})

    def buscar_vertice(self, dato):
        for v in self.elements:
            if v["info"] == dato:
                return v
        return None

    def insert_edge(self, origen, destino, peso):
        v_origen = self.buscar_vertice(origen)
        v_destino = self.buscar_vertice(destino)
        if v_origen and v_destino:
            if not any(e["destino"] == destino for e in v_origen["aristas"]):
                v_origen["aristas"].append({"destino": destino, "peso": peso})
            if not self.dirigido:
                if not any(e["destino"] == origen for e in v_destino["aristas"]):
                    v_destino["aristas"].append({"destino": origen, "peso": peso})

    def prim(self, origen):
        """Árbol de Expansión Mínimo (MST) utilizando el algoritmo de Prim"""
        bosque = []
        if not self.buscar_vertice(origen):
            return bosque
        
        visitados = [origen]
        aristas = []
        
        for v in self.elements:
            if v["info"] == origen:
                for a in v["aristas"]:
                    aristas.append((a["peso"], origen, a["destino"]))
        
        aristas.sort(key=lambda x: x[0])
        
        while aristas:
            peso, desde, hasta = aristas.pop(0)
            if hasta not in visitados:
                visitados.append(hasta)
                bosque.append((desde, hasta, peso))
                for v in self.elements:
                    if v["info"] == hasta:
                        for a in v["aristas"]:
                            if a["destino"] not in visitados:
                                aristas.append((a["peso"], hasta, a["destino"]))
                aristas.sort(key=lambda x: x[0])
        return bosque

    def dijkstra(self, inicio, fin):
        """Algoritmo de Dijkstra para hallar el camino más corto"""
        no_visitados = [v["info"] for v in self.elements]
        distancias = {v["info"]: float('inf') for v in self.elements}
        caminos = {v["info"]: [] for v in self.elements}
        
        distancias[inicio] = 0
        caminos[inicio] = [inicio]

        while no_visitados:
            actual = min(no_visitados, key=lambda v: distancias[v])
            if distancias[actual] == float('inf'):
                break
            if actual == fin:
                break
            no_visitados.remove(actual)

            v_obj = self.buscar_vertice(actual)
            for a in v_obj["aristas"]:
                vecino = a["destino"]
                if vecino in no_visitados:
                    # Usamos el inverso del peso o costo directo para evaluar la relación
                    nueva_dist = distancias[actual] + (1 / a["peso"])
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        caminos[vecino] = caminos[actual] + [vecino]
        return caminos[fin], distancias[fin]

# --- Inicialización y carga del Grafo ---
grafo = Grafo(dirigido=False)

# Cargar vértices
for p in personajes_sw:
    grafo.insert_vertex(p["nombre"])

# Cargar aristas desde la lista de relaciones (peso, personaje_1, personaje_2)
for peso, p1, p2 in relaciones_sw:
    grafo.insert_edge(p1, p2, peso)

# --- 1. Árbol de Expansión Mínimo desde C-3PO, Yoda y Leia ---
print("=== ÁRBOL DE EXPANSIÓN MÍNIMO (MST) ===")
for personaje_inicio in ["C-3PO", "Yoda", "Leia"]:
    mst = grafo.prim(personaje_inicio)
    print(f"\nDesde {personaje_inicio}:")
    total_peso = 0
    for desde, hasta, peso in mst:
        print(f"  {desde} --({peso} episodios)--> {hasta}")
        total_peso += peso
    print(f"  Peso total acumulado: {total_peso}")

# --- 2. Número máximo de episodios compartidos y sus pares ---
print("\n=== MÁXIMO DE EPISODIOS COMPARTIDOS ===")
max_episodios = max(r[0] for r in relaciones_sw)
pares_maximos = [(r[1], r[2]) for r in relaciones_sw if r[0] == max_episodios]

print(f"Número máximo de episodios: {max_episodios}")
print("Pares de personajes:")
for p1, p2 in pares_maximos:
    print(f"  - {p1} y {p2}")

# --- 3. Caminos más cortos solicitados ---
print("\n=== CAMINOS MÁS CORTOS ===")
consultas_dijkstra = [("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")]
for inicio, fin in consultas_dijkstra:
    camino, costo = grafo.dijkstra(inicio, fin)
    print(f"Camino de {inicio} a {fin}: {' -> '.join(camino)} (Costo: {costo:.2f})")

# --- 4. Personajes que aparecieron en los nueve episodios ---
print("\n=== PERSONAJES EN LOS NUEVE EPISODIOS ===")
for p in personajes_sw:
    if p["episodios"] == 9:
        print(f"  - {p['nombre']}")