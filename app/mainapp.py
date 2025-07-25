'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-20
Descripción: Programa de gestión de equipos tipo BetPlay.
'''


# from tabulate import tabulate
import os

equipos = []
jugadores = []
partidos = []


def agregar_equipo():
    limpiar_pantalla()
    nombre = input("Nombre del equipo: ")
    equipo = (nombre, [0, 0, 0, 0, 0, 0, 0])  # (nombre, PJ, PG, PP, PE, GF, GC, TP)
    equipos.append(equipo)
    print(f"Equipo '{nombre}' agregado.\n")
    pausar()

def agregar_jugador():
    limpiar_pantalla()
    print("Equipos disponibles:")
    for e in equipos:
        print(f"- {e[0]}")
    print()
    nombre = input("Nombre del jugador: ")
    dorsal = input("Número en la espalda: ")
    edad = input("Edad: ")
    equipo = input("Equipo al que pertenece: ")
    if not any(e[0] == equipo for e in equipos):
        print(f"El equipo '{equipo}' no existe. Agregue el equipo primero.\n")
        pausar()
        return
    jugador = (nombre, dorsal, edad, equipo, 0)
    jugadores.append(jugador)
    print(f"Jugador '{nombre}' agregado al equipo '{equipo}'.\n")
    pausar()

def registrar_partido():
    limpiar_pantalla()
    print("Registrar nuevo partido:")
    eq1 = input("Equipo 1: ")
    eq2 = input("Equipo 2: ")
    fecha = input("Fecha del partido (dd/mm/yy): ")
    try:
        goles1 = int(input(f"Goles de {eq1}: "))
        goles2 = int(input(f"Goles de {eq2}: "))
    except ValueError:
        print("Ingrese un número válido para los goles.\n")
        pausar()
        return

    goleadores = []
    # Goles del equipo 1
    print(f"\nGoleadores de {eq1}")
    for i in range(goles1):
        nombre = input(f"Gol {i+1} de {eq1}. ¿Quién lo hizo?: ")
        goleadores.append(nombre)
        for j in range(len(jugadores)):
            if jugadores[j][0] == nombre:
                jugador = list(jugadores[j])
                jugador[4] += 1 
                jugadores[j] = tuple(jugador)

    # Goles del equipo 2
    print(f"\nGoleadores de {eq2}")
    for i in range(goles2):
        nombre = input(f"Gol {i+1} de {eq2}. ¿Quién lo hizo?: ")
        goleadores.append(nombre)
        for j in range(len(jugadores)):
            if jugadores[j][0] == nombre:
                jugador = list(jugadores[j])
                jugador[4] += 1
                jugadores[j] = tuple(jugador)

    partidos.append((eq1, eq2, fecha, goles1, goles2, goleadores))
    actualizar_estadisticas(eq1, eq2, goles1, goles2)
    print("Partido registrado exitosamente.\n")
    pausar()

def actualizar_estadisticas(eq1, eq2, goles1, goles2):
    for i in range(len(equipos)):
        nombre, stats = equipos[i]
        if nombre == eq1:
            stats[0] += 1  # PJ
            stats[4] += goles1  # GF
            stats[5] += goles2  # GC
            if goles1 > goles2:
                stats[1] += 1  # PG
                stats[6] += 3  # TP
            elif goles1 < goles2:
                stats[2] += 1  # PP
            else:
                stats[3] += 1  # PE
                stats[6] += 1  # TP
        elif nombre == eq2:
            stats[0] += 1  # PJ
            stats[4] += goles2  # GF
            stats[5] += goles1  # GC
            if goles2 > goles1:
                stats[1] += 1  # PG
                stats[6] += 3  # TP
            elif goles2 < goles1:
                stats[2] += 1  # PP
            else:
                stats[3] += 1  # PE
                stats[6] += 1  # TP
        equipos[i] = (nombre, stats)

def mostrar_estadisticas():
    limpiar_pantalla()
    for nombre, datos in equipos:
        print(f"{nombre} => PJ:{datos[0]} PG:{datos[1]} PP:{datos[2]} PE:{datos[3]} GF:{datos[4]} GC:{datos[5]} TP:{datos[6]}")
    print()
    print('PJ: Partidos Jugados, PG: Partidos Ganados, PP: Partidos Perdidos, PE: Partidos Empatados, GF: Goles a Favor, GC: Goles en Contra, TP: Total de Puntos')
    pausar()

def mostrar_partidos():
    limpiar_pantalla()
    for partido in partidos:
        eq1, eq2, fecha, g1, g2, goleadores = partido
        print(f"{fecha}: {eq1} {g1} - {g2} {eq2}")
        print("Goleadores:", ", ".join(goleadores))
    print()
    pausar()

def mostrar_jugadores():
    limpiar_pantalla()
    for j in jugadores:
        print(f"{j[0]} | Dorsal: {j[1]} | Edad: {j[2]} | Equipo: {j[3]} | Goles: {j[4]}")
    print()
    pausar()

def main():
    while True:
        limpiar_pantalla()
        print("=== MENÚ PRINCIPAL DE TORNEOS ===")
        print("1. Administrar equipo")
        print("2. Administrar jugador")
        print("3. Registrar partido")
        print("4. Mostrar estadísticas de equipos")
        print("5. Mostrar partidos jugados")
        print("6. Mostrar jugadores")
        print("7. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.\n")
            pausar()
            continue

        if opcion == 1:
            agregar_equipo()
        elif opcion == 2:
            agregar_jugador()
        elif opcion == 3:
            registrar_partido()
        elif opcion == 4:
            mostrar_estadisticas()
        elif opcion == 5:
            mostrar_partidos()
        elif opcion == 6:
            mostrar_jugadores()
        elif opcion == 7:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.\n")
            pausar()

if __name__ == "__main__":
    main()