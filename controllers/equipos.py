import utils.validateData as validate
import utils.corefiles as core
import utils.dataHandler as dataHandler
import os
import json


def registrar_equipo():
    equipos = core.read_json(dataHandler.equipos_path)
    if not isinstance(equipos, list):
        equipos = []

    while True:
        id_equipo = input("Ingrese ID del equipo (4 dígitos): ")
        if validate.validar_id_unico(id_equipo, equipos):
            break

    nombre = input("Nombre del equipo: ")
    fundacion = input("Fecha de fundación (YYYY-MM-DD): ")
    pais = input("País: ")

    nuevo_equipo = {
        "id": id_equipo,
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais
    }

    equipos.append(nuevo_equipo)
    core.write_json(dataHandler.equipos_path, equipos)
    print(f"Equipo {nombre} registrado con éxito.")

def listar_equipos():
    equipos = core.read_json(dataHandler.equipos_path)
    if not equipos:
        print("No hay equipos registrados.")
        return

    print("Listado de equipos registrados:")
    for equipo in equipos:
        print(f"ID: {equipo.get('id')}, Nombre: {equipo.get('nombre')}, Fundación: {equipo.get('fundacion')}, País: {equipo.get('pais')}, Liga ID: {equipo.get('liga_id')}")
