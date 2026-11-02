# Lista de personajes con la cantidad de episodios totales en los que aparecen
personajes_sw = [
    {"nombre": "Luke Skywalker", "episodios": 6},
    {"nombre": "Darth Vader", "episodios": 6},
    {"nombre": "Yoda", "episodios": 6},
    {"nombre": "Boba Fett", "episodios": 3},
    {"nombre": "C-3PO", "episodios": 9},  # Apareció en los 9
    {"nombre": "Leia", "episodios": 7},
    {"nombre": "Rey", "episodios": 3},
    {"nombre": "Kylo Ren", "episodios": 3},
    {"nombre": "Chewbacca", "episodios": 7},
    {"nombre": "Han Solo", "episodios": 5},
    {"nombre": "R2-D2", "episodios": 9},  # Apareció en los 9
    {"nombre": "BB-8", "episodios": 3}
]

# Lista de relaciones: (episodios_compartidos, personaje_1, personaje_2)
relaciones_sw = [
    (6, "C-3PO", "R2-D2"),
    (5, "Luke Skywalker", "Leia"),
    (4, "Han Solo", "Chewbacca"),
    (3, "Yoda", "Luke Skywalker"),
    (2, "Darth Vader", "Luke Skywalker"),
    (3, "Rey", "Kylo Ren"),
    (2, "BB-8", "Rey"),
    (4, "Leia", "C-3PO"),
    (3, "Boba Fett", "Darth Vader"),
    (2, "Yoda", "Chewbacca"),
    (1, "Darth Vader", "C-3PO"),
    (1, "Yoda", "Darth Vader") # Relación necesaria para el Dijkstra del parcial
]