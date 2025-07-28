
import json
from corefiles import read_json

def validar_nombre_equipo(nombre):
    if not isinstance(nombre, str) or len(nombre.strip()) < 2:
        return False, "El nombre del equipo debe tener al menos 2 caracteres."
    return True, ""

def validar_fecha(fecha):
    # Formato esperado: dd/mm/aaaa
    if not isinstance(fecha, str):
        return False, "La fecha debe ser texto en formato dd/mm/aaaa."
    partes = fecha.split("/")
    if len(partes) != 3:
        return False, "La fecha debe tener el formato dd/mm/aaaa."
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False, "Día, mes y año deben ser números."
    if not (1 <= int(dia) <= 31):
        return False, "El día debe estar entre 1 y 31."
    if not (1 <= int(mes) <= 12):
        return False, "El mes debe estar entre 1 y 12."
    if len(anio) != 4:
        return False, "El año debe tener 4 dígitos."
    return True, ""

def validar_pais(pais):
    if not isinstance(pais, str) or len(pais.strip()) < 2:
        return False, "El nombre del país debe tener al menos 2 caracteres."
    return True, ""

def validar_nombre_jugador(nombre):
    if not isinstance(nombre, str) or len(nombre.strip()) < 2:
        return False, "El nombre del jugador debe tener al menos 2 caracteres."
    return True, ""

def validar_posicion(posicion):
    posiciones_validas = ['Portero', 'Defensa', 'Centrocampista', 'Delantero']
    if posicion not in posiciones_validas:
        return False, f"La posición debe ser una de: {', '.join(posiciones_validas)}."
    return True, ""

def validar_numero_dorsal(dorsal):
    if not dorsal.isdigit():
        return False, "El número dorsal debe ser un número entero."
    num = int(dorsal)
    if not (1 <= num <= 99):
        return False, "El número dorsal debe estar entre 1 y 99."
    return True, ""

def validar_id_equipo(id_equipo, lista_equipos):
    if id_equipo not in lista_equipos:
        return False, f"El ID de equipo '{id_equipo}' no existe."
    return True, ""

def validar_tipo_transferencia(tipo):
    tipos_validos = ['venta', 'prestamo']
    if tipo.lower() not in tipos_validos:
        return False, f"Tipo de transferencia inválido. Debe ser: {', '.join(tipos_validos)}."
    return True, ""

def validar_opcion_menu(opcion, opciones_validas):
    if opcion not in opciones_validas:
        return False, "Opción no válida."
    return True, ""

def validar_id_unico(id_str, equipos):
    if not id_str.isdigit() or len(id_str) != 4:
        print("Error: El ID debe ser un número de 4 dígitos.")
        return False
    for equipo in equipos:
        if equipo.get("id") == id_str:
            print(f"Error: El ID '{id_str}' ya existe.")
            return False
    return True


def validar_liga_existente(liga_id, ligas_path="data/ligas.json"):
    ligas = read_json(ligas_path)
    if not isinstance(ligas, list):
        return False, "No se pudo leer el archivo de ligas."
    if any(liga.get("id") == liga_id for liga in ligas):
        return True, ""
    return False, f"La liga con ID '{liga_id}' no existe."

