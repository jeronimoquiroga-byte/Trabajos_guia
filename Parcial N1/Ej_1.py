from super_heroes_data import superheroes

lista_heroes = superheroes[:15]


def buscar_capitan_america(lista, indice=0):
    if indice == len(lista):
        return False
    if lista[indice]["name"] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)


def listar_heroes(lista, indice=0):
    if indice == len(lista):
        return
    print(f"{indice + 1}. {lista[indice]['name']}")
    listar_heroes(lista, indice + 1)


if __name__ == "__main__":
    print("=" * 45)
    print("   LISTA DE 15 SUPERHÉROES (RECURSIVA)")
    print("=" * 45)
    listar_heroes(lista_heroes)

    print()
    print("=" * 45)
    print("   BÚSQUEDA DE CAPTAIN AMERICA (RECURSIVA)")
    print("=" * 45)

    encontrado = buscar_capitan_america(lista_heroes)

    if encontrado:
        print("Captain America SÍ está en la lista.")
    else:
        print("Captain America NO está en la lista.")