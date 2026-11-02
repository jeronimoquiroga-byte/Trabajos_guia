from list_pokemones import lista_pokemons, Pokemon

class NodoArbol:
    def __init__(self, clave, dato):
        self.info = clave
        self.datos = [dato] if not isinstance(dato, list) else dato
        self.izq = None
        self.der = None
        self.altura = 0

def altura(raiz):
    if raiz is None:
        return -1
    return raiz.altura

def actualizar_altura(raiz):
    if raiz is not None:
        raiz.altura = max(altura(raiz.izq), altura(raiz.der)) + 1

def rotar_simple_izq(raiz):
    aux = raiz.der
    raiz.der = aux.izq
    aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    return aux

def rotar_simple_der(raiz):
    aux = raiz.izq
    raiz.izq = aux.der
    aux.der = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    return aux

def rotar_doble_izq(raiz):
    raiz.der = rotar_simple_der(raiz.der)
    return rotar_simple_izq(raiz)

def rotar_doble_der(raiz):
    raiz.izq = rotar_simple_izq(raiz.izq)
    return rotar_simple_der(raiz)

def balancear(raiz):
    if raiz is None:
        return raiz
    if altura(raiz.izq) - altura(raiz.der) == 2:
        if altura(raiz.izq.izq) >= altura(raiz.izq.der):
            raiz = rotar_simple_der(raiz)
        else:
            raiz = rotar_doble_der(raiz)
    elif altura(raiz.izq) - altura(raiz.der) == -2:
        if altura(raiz.der.der) >= altura(raiz.der.izq):
            raiz = rotar_simple_izq(raiz)
        else:
            raiz = rotar_doble_izq(raiz)
    actualizar_altura(raiz)
    return raiz

def insertar(raiz, clave, dato):
    if raiz is None:
        return NodoArbol(clave, dato)
    if clave < raiz.info:
        raiz.izq = insertar(raiz.izq, clave, dato)
    elif clave > raiz.info:
        raiz.der = insertar(raiz.der, clave, dato)
    else:
        if dato not in raiz.datos:
            raiz.datos.append(dato)
    return balancear(raiz)

def buscar(raiz, clave):
    if raiz is None or raiz.info == clave:
        return raiz
    if clave < raiz.info:
        return buscar(raiz.izq, clave)
    return buscar(raiz.der, clave)

def busqueda_proximidad(raiz, aproximacion):
    resultado = []
    if raiz is not None:
        if aproximacion.lower() in str(raiz.info).lower():
            resultado.append((raiz.info, raiz.datos))
        resultado.extend(busqueda_proximidad(raiz.izq, aproximacion))
        resultado.extend(busqueda_proximidad(raiz.der, aproximacion))
    return resultado

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        for d in raiz.datos:
            print(f"Clave: {raiz.info} -> #{d.numero} {d.nombre}")
        inorden(raiz.der)

def por_nivel(raiz):
    if raiz is None:
        return
    cola = [raiz]
    while cola:
        actual = cola.pop(0)
        for d in actual.datos:
            print(f"Clave: {actual.info} -> #{d.numero} {d.nombre}")
        if actual.izq:
            cola.append(actual.izq)
        if actual.der:
            cola.append(actual.der)

# Inicialización de los tres árboles requeridos
arbol_nombre = None
arbol_numero = None
arbol_tipo = None

# Carga de datos en los árboles
for p in lista_pokemons:
    arbol_nombre = insertar(arbol_nombre, p.nombre, p)
    arbol_numero = insertar(arbol_numero, p.numero, p)
    for t in p.tipos:
        arbol_tipo = insertar(arbol_tipo, t, p)

# 1. Mostrar datos a partir de número y nombre (proximidad)
print("--- Búsqueda por número (25) ---")
res_num = buscar(arbol_numero, 25)
if res_num:
    for p in res_num.datos:
        print(f"#{p.numero} {p.nombre} - Tipos: {p.tipos}")

print("\n--- Búsqueda por proximidad en nombre ('bul') ---")
for clave, datos in busqueda_proximidad(arbol_nombre, "bul"):
    for p in datos:
        print(f"#{p.numero} {p.nombre}")

# 2. Mostrar nombres de Pokémons de tipos específicos: fantasma, fuego, acero y eléctrico
tipos_requeridos = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_requeridos:
    print(f"\n--- Pokémons de tipo {tipo} ---")
    res_t = buscar(arbol_tipo, tipo)
    if res_t:
        for p in res_t.datos:
            print(p.nombre)
    else:
        print("Ninguno encontrado.")

# 3. Listados en orden ascendente y por nivel
print("\n--- Listado ascendente por número ---")
inorden(arbol_numero)

print("\n--- Listado ascendente por nombre ---")
inorden(arbol_nombre)

print("\n--- Listado por nivel por nombre ---")
por_nivel(arbol_nombre)

# 4. Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum
objetivos_debilidad = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("\n--- Débiles frente a Jolteon, Lycanroc y Tyrantrum ---")
for p in lista_pokemons:
    if any(d in objetivos_debilidad for d in p.debilidades):
        print(f"{p.nombre} (Débil ante: {p.debilidades})")

# 5. Determinación de tipos, conteos, megaevoluciones y gigamax
conteo_tipos = {}
mega_count = 0
giga_count = 0

for p in lista_pokemons:
    if p.mega:
        mega_count += 1
    if p.gigamax:
        giga_count += 1
    for t in p.tipos:
        conteo_tipos[t] = conteo_tipos.get(t, 0) + 1

print(f"\nTotal de Pokémons cargados: {len(lista_pokemons)}")
print(f"Cantidad con Megaevolución: {mega_count}")
print(f"Cantidad con forma Gigamax: {giga_count}")
print(f"Conteo por tipos: {conteo_tipos}")