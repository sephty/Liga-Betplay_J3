'''
Nombre: Joseph Garcia Jimenez
fecha: 2025-07-28
Descripción: Gestion de Torneos BetPlay.
'''


import controllers.equipos as equiposController
import controllers.jugadores as jugadoresController
import controllers.torneos as torneosController
import utils.screenController as screenController


def main():
    while True:
        screenController.limpiar_pantalla()
        print("=== GESTOR DE TORNEOS BETPLAY ===")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Administrar torneos")
        print("5. Transferencia de jugador (venta o préstamo)")
        print("6. Ver estadísticas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                equiposController.registrar_equipo()
            case "2":
                equipos = equiposController.listar_equipos()
                if not equipos:
                    print("No hay equipos registrados.")
                else:
                    for equipo in equipos:
                        print(f"ID: {equipo.get('id', 'N/A')}, Nombre: {equipo.get('nombre', 'N/A')}")
            case "3":
                jugadoresController.registrar_jugador()
            case "4":
                jugadores = jugadoresController.listar_jugadores()
                if not jugadores:
                    print("No hay jugadores registrados.")
            case "5":
                torneosController.menu_torneos()
                
            case "6":
                pass
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida.\n")

if __name__ == "__main__":
    main()
