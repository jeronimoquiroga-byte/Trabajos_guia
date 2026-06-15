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
p.empujar({"nombre": "Iron Man", "peliculas": 10})
p.empujar({"nombre": "Captain America", "peliculas": 9})
p.empujar({"nombre": "Black Widow", "peliculas": 8})
p.empujar({"nombre": "Groot", "peliculas": 4})
p.empujar({"nombre": "Doctor Strange", "peliculas": 6})
p.empujar({"nombre": "Rocket Raccoon", "peliculas": 5}) 

resolver_ejercicio_marvel(p)

#TRABAJOS GUIA_COLA.

# Ejercicio 10 de la guia.

class Notificacion:
    def __init__(ser, hora, aplicacion, mensaje):
        ser.hora = hora
        ser.aplicacion = aplicacion
        ser.mensaje = mensaje


def eliminar_facebook(cola_noti):
    limite = cola_noti.tamaño()
    
    for i in range(limite):
        noti = cola_noti.atención()
        
        if noti.aplicacion.lower() != "facebook":
            cola_noti.llegar(noti)


def mostrar_twitter_python(cola_noti):
    limite = cola_noti.tamaño()
    
    print("\n--- NOTIFICACIONES DE TWITTER CON 'PYTHON' ---")
    for i in range(limite):
        noti = cola_noti.mover_al_final()
        
        if noti.aplicacion.lower() == "twitter" and "python" in noti.mensaje.lower():
            print("Hora: " + noti.hora + " | Mensaje: " + noti.mensaje)


def filtrar_por_hora_con_pila(cola_noti, pila_aux):
    limite = cola_noti.tamaño()
    contador = 0
    
    for i in range(limite):
        noti = cola_noti.atención()
        
        if noti.hora >= "11:43" and noti.hora <= "15:57":
            pila_aux.llegar(noti)
            contador = contador + 1
        else:
            cola_noti.llegar(noti)
            
    while pila_aux.tamaño() > 0:
        noti_temporal = pila_aux.atención()
        cola_noti.llegar(noti_temporal)
        
    print("\nCantidad de notificaciones en el rango: " + str(contador))

# Ejercicio 22 de la guia.

class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__elements)):
            value = self.move_to_end()
            print(value)

cola_mcu = Queue()
cola_mcu.arrive(["Tony Stark", "Iron Man", "M"])
cola_mcu.arrive(["Steve Rogers", "Capitán América", "M"])
cola_mcu.arrive(["Natasha Romanoff", "Black Widow", "F"])
cola_mcu.arrive(["Bruce Banner", "Hulk", "M"])
cola_mcu.arrive(["Thor Odinson", "Thor", "M"])
cola_mcu.arrive(["Clint Barton", "Hawkeye", "M"])
cola_mcu.arrive(["Carol Danvers", "Capitana Marvel", "F"])
cola_mcu.arrive(["Scott Lang", "Ant-Man", "M"])
cola_mcu.arrive(["Wanda Maximoff", "Scarlet Witch", "F"])
cola_mcu.arrive(["Stephen Strange", "Doctor Strange", "M"])


print("=" * 55)
print("a) Nombre del personaje de Capitana Marvel")
print("=" * 55)
personaje_encontrado = None
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[1] == "Capitana Marvel":
        personaje_encontrado = dato[0]

if personaje_encontrado is not None:
    print(f"   El personaje de Capitana Marvel es: {personaje_encontrado}")
else:
    print("   No se encontró a Capitana Marvel en la cola.")

print()
print("=" * 55)
print("b) Superhéroes femeninos")
print("=" * 55)
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[2] == "F":
        print(f"   {dato[1]}")

print()
print("=" * 55)
print("c) Personajes masculinos")
print("=" * 55)
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[2] == "M":
        print(f"   {dato[0]}")

print()
print("=" * 55)
print("d) Nombre del superhéroe de Scott Lang")
print("=" * 55)
superheroe_encontrado = None
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[0] == "Scott Lang":
        superheroe_encontrado = dato[1]

if superheroe_encontrado is not None:
    print(f"   El superhéroe de Scott Lang es: {superheroe_encontrado}")
else:
    print("   No se encontró a Scott Lang en la cola.")

print()
print("=" * 55)
print("e) Personajes/Superhéroes que comienzan con 'S'")
print("=" * 55)
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[0][0] == "S" or dato[1][0] == "S":
        print(f"   Personaje: {dato[0]} | Superhéroe: {dato[1]} | Género: {dato[2]}")

print()
print("=" * 55)
print("f) ¿Carol Danvers está en la cola?")
print("=" * 55)
carol_encontrada = False
nombre_super_carol = None
for i in range(cola_mcu.size()):
    dato = cola_mcu.move_to_end()
    if dato[0] == "Carol Danvers":
        carol_encontrada = True
        nombre_super_carol = dato[1]

if carol_encontrada:
    print(f"   Sí, Carol Danvers se encuentra en la cola.")
    print(f"   Su nombre de superhéroe es: {nombre_super_carol}")
else:
    print("   Carol Danvers NO se encuentra en la cola.")


