import utils.corefiles as core
import utils.validateData as validate
import utils.dataHandler as dataHandler

def cargar_jugadores():
    jugadores = core.read_json(dataHandler.jugadores_path)
    if not isinstance(jugadores, list):
        return []
    return jugadores

def guardar_jugadores(jugadores):
    core.write_json(dataHandler.jugadores_path, jugadores)

def cargar_equipos():
    equipos = core.readson(dataHandler.equipos_path)
    if not isinstance(equipos, list):
        return []
    return equipos

def registrar_jugador():
    jugadores = cargar_jugadores()
    equipos = cargar_equipos()

    nombre = input("Nombre del jugador: ").strip()
    valido, mensaje = validate.validar_nombre_jugador(nombre)
    if not valido:
        print("Error:", mensaje)
        return

    posicion = input("Posición: ").strip()
    valido, mensaje = validate.validar_posicion(posicion)
    if not valido:
        print("Error:", mensaje)
        return

    dorsal = input("Número dorsal: ").strip()
    valido, mensaje = validate.validar_numero_dorsal(dorsal)
    if not valido:
        print("Error:", mensaje)
        return

    id_equipo = input("ID del equipo al que pertenece: ").strip()
    if not any(e['id'] == id_equipo for e in equipos):
        print("Error: El equipo no existe.")
        return

    if jugadores:
        ultimo_id = max(int(j['id']) for j in jugadores if 'id' in j)
        nuevo_id = str(ultimo_id + 1)
    else:
        nuevo_id = "1"

    nuevo_jugador = {
        "id": nuevo_id,
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "equipo_id": id_equipo
    }

    jugadores.append(nuevo_jugador)
    guardar_jugadores(jugadores)
    print(f"Jugador '{nombre}' registrado exitosamente con ID {nuevo_id}.")

def listar_jugadores():
    jugadores = cargar_jugadores()
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("\nListado de jugadores:\n")
    for jugador in jugadores:
        print(f"ID: {jugador.get('id', 'N/A')}")
        print(f"  Nombre: {jugador.get('nombre', 'N/A')}")
        print(f"  Posición: {jugador.get('posicion', 'N/A')}")
        print(f"  Dorsal: {jugador.get('dorsal', 'N/A')}")
        print(f"  Equipo ID: {jugador.get('equipo_id', 'N/A')}")
        print("-" * 30)
