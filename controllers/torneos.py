import json
import random

import utils.corefiles as cf
import utils.screenController as sc
import utils.dataHandler as dataHandler




def menu_ligas():
    while True:
        sc.limpiar_pantalla()
        print("\nMENÚ DE LIGAS")
        print("1. Crear Liga")
        print("2. Listar Ligas")
        print("3. Añadir Equipo a Liga")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_liga()
        elif opcion == "2":
            listar_ligas()
        elif opcion == "3":
            anadir_equipo_a_liga()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            sc.pausar_pantalla()

def crear_liga():
    sc.limpiar_pantalla()
    print("\nCREAR NUEVA LIGA")

    nombre = input("Nombre de la liga: ").strip()
    locacion = input("Ubicación/país de la liga: ").strip()

    if len(nombre) < 2 or len(locacion) < 2:
        print("El nombre y la locación deben tener al menos 2 caracteres.")
        sc.pausar_pantalla()
        return

    ligas = cf.read_json(dataHandler.ligas_path)
    if not isinstance(ligas, list):
        ligas = []

    liga_id = str(random.randint(1000, 9999))
    while any(l.get("liga_id") == liga_id for l in ligas):
        liga_id = str(random.randint(1000, 9999))

    nueva_liga = {
        "liga_id": liga_id,
        "nombre": nombre,
        "locacion": locacion
    }

    ligas.append(nueva_liga)
    cf.write_json(dataHandler.ligas_path, ligas)

    print(f"Liga '{nombre}' registrada con ID: {liga_id}")
    sc.pausar_pantalla()

def listar_ligas():
    print("\nLISTADO DE LIGAS")

    ligas = cf.read_json(dataHandler.ligas_path)
    if not ligas:
        print("No hay ligas registradas.")
        sc.pausar_pantalla()
        return

    for liga in ligas:
        print(f"ID: {liga['liga_id']} | Nombre: {liga['nombre']} | Ubicación: {liga['locacion']}")

    sc.pausar_pantalla()

def anadir_equipo_a_liga():
    print("\nAÑADIR EQUIPO A LIGA")

    ligas = cf.read_json(dataHandler.ligas_path)
    equipos = cf.read_json(dataHandler.equipos_path)

    if not ligas:
        print("No hay ligas disponibles.")
        sc.pausar_pantalla()
        return

    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return

    print("\n--- Ligas disponibles ---")
    for liga in ligas:
        print(f"{liga['liga_id']}: {liga['nombre']} ({liga['locacion']})")

    liga_id = input("Ingrese el ID de la liga: ").strip()
    liga = next((l for l in ligas if l["liga_id"] == liga_id), None)

    if not liga:
        print("Liga no encontrada.")
        sc.pausar_pantalla()
        return

    print("\n--- Equipos disponibles ---")
    for equipo in equipos:
        print(f"{equipo['id']}: {equipo['nombre']}")

    equipo_id = input("Ingrese el ID del equipo a asignar: ").strip()
    equipo = next((e for e in equipos if e["id"] == equipo_id), None)

    if not equipo:
        print("Equipo no encontrado.")
        sc.pausar_pantalla()
        return

    equipo["liga_id"] = liga_id
    cf.write_json(dataHandler.equipos_path, equipos)

    print(f"\nEquipo '{equipo['nombre']}' añadido a la liga '{liga['nombre']}' correctamente.")
    sc.pausar_pantalla()


