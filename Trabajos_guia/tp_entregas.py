# TRABAJOS GUIA_RECURSIVIDAD-ENTREGAS.

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