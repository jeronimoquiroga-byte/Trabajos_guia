# TRABAJOS GUIA_RECURSIVIDAD.

# Ejercicio 5 de la guia.

valores = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000
    }

def romano_a_decimal(romano):
    if len(romano) == 0:
        return 0
    
    if len(romano) == 1:
        return valores[romano[0]]

    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return -valores[romano[0]] + romano_a_decimal(romano[1:])

numero = "XIV"
print(f"El número {numero} en decimal es: {romano_a_decimal(numero)}")

# Ejercicio 22 de la guia.

def usar_la_fuerza(mochila, contador=0):
    if len(mochila) == 0:
        return False, contador
    
    contador += 1

    if mochila[0] == "sable de luz":
        return True, contador
    else:
        return usar_la_fuerza(mochila[1:], contador)

mi_mochila = ["comida", "botella", "mapa", "sable de luz", "capa"]

encontrado, cantidad = usar_la_fuerza(mi_mochila)

if encontrado:
    print(f"Jedi, encontraste tu sable, sacaste {cantidad} objetos.")
else:
    print("El sable no está en la mochila.")


#TRABAJOS GUIA_PILAS.

#La clase pila.

class Pila:
    def __init__(ser):
        ser.__elementos = []

    def empujar(ser, valor):
        ser.__elementos.append(valor)

    def estallido(ser):
        return ser.__elementos.pop()

    def tamaño(ser):
        return len(ser.__elementos)
        
    def en_arriba(ser):
        if ser.tamaño() > 0:
            return ser.__elementos[-1]
        

#Ejercicio 20 de la guia.

def registrar_recorrido():
    historial = Pila()
    
    historial.empujar({"pasos": 10, "direccion": "norte"})
    historial.empujar({"pasos": 5, "direccion": "este"})
    historial.empujar({"pasos": 12, "direccion": "noreste"})
    historial.empujar({"pasos": 7, "direccion": "sur"})
    
    return historial


def camino_regreso(pila_movimientos):
    print("Regreso del robot...")
    
    contrarios = {
        "norte": "sur", 
        "sur": "norte",
        "este": "oeste", 
        "oeste": "este",
        "noreste": "suroeste", 
        "suroeste": "noreste",
        "noroeste": "sureste", 
        "sureste": "noroeste"
    }
    
    while pila_movimientos.tamaño() > 0:
        ultimo = pila_movimientos.estallido() 
        
        pasos = ultimo["pasos"]
        dir_ida = ultimo["direccion"]
        
        dir_vuelta = contrarios[dir_ida]
        
        print(f"Mover {pasos} pasos hacia el {dir_vuelta}")
        
    print("El robot volvio al punto de partida.")

mi_camino = registrar_recorrido()
camino_regreso(mi_camino)


# Ejercicio 24 de la guia.

def resolver_ejercicio_marvel(pila_mcu):
    aux = Pila()
    
    pos = 1
    pos_rocket = -1
    pos_groot = -1
    pelis_widow = 0
    
    print("Personajes con mas de 5 peliculas")
    
    while pila_mcu.tamaño() > 0:
        pj = pila_mcu.estallido()
        
        nombre = pj["nombre"]
        pelis = pj["peliculas"]
        
        if nombre == "Rocket Raccoon":
            pos_rocket = pos
        if nombre == "Groot":
            pos_groot = pos
            
        if pelis > 5:
            print(f"- {nombre} aparece en {pelis} peliculas")
            
        if nombre == "Black Widow":
            pelis_widow = pelis
            
        letra = nombre[0].upper()
        if letra in ["C", "D", "G"] and nombre != "Groot": 
            pass
            
        aux.empujar(pj)
        pos += 1

    print("Personajes que empiezan con C, D o G")
    while aux.tamaño() > 0:
        pj = aux.estallido()
        nombre = pj["nombre"]
        letra = nombre[0].upper()
        
        if letra in ["C", "D", "G"]:
            print(f"- {nombre}")
            
        pila_mcu.empujar(pj)

   
    print(" Otros resultados")
    print(f"Rocket Raccoon esta en la posicion: {pos_rocket}")
    print(f"Groot esta en la posicion: {pos_groot}")
    print(f"Black Widow participo en {pelis_widow} peliculas")


p = Pila()
# Cargamos datos de prueba.
p.empujar({"nombre": "Iron Man", "peliculas": 10})
p.empujar({"nombre": "Captain America", "peliculas": 9})
p.empujar({"nombre": "Black Widow", "peliculas": 8})
p.empujar({"nombre": "Groot", "peliculas": 4})
p.empujar({"nombre": "Doctor Strange", "peliculas": 6})
p.empujar({"nombre": "Rocket Raccoon", "peliculas": 5}) 

resolver_ejercicio_marvel(p)