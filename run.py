from app import app, db
from app.controllers import datos_controller as controller
import subprocess

with app.app_context():
    db.create_all()

with app.app_context():
    while True:
        print("\nMenú:")
        print("1. Listar datos locales")
        print("2. Agregar entidad")
        print("3. Actualizar entidad")
        print("4. Eliminar entidad")
        print("5. Traer datos desde API")
        print("6. Mostrar frecuencia de publicación por entidad")
        print("7. Ejecutar Pruebas Unitarias")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            datos = controller.listar()
            if datos:
                print("\n--- Datos Locales ---")
                for dato in datos:
                    print(dato)
                print("-----------------------\n")
            else:
                print("\nNo hay datos locales.\n")
        elif opcion == '2':
            entidad = input("Ingrese la entidad: ")
            tema = input("Ingrese el tema: ")
            fecha = input("Ingrese la fecha de actualización: ")
            controller.agregar(entidad, tema, fecha)
            print("Dato agregado correctamente.")
        elif opcion == '3':
            id_editar = input("Ingrese el ID del dato a actualizar: ")
            entidad = input("Ingrese la nueva entidad: ")
            tema = input("Ingrese el nuevo tema: ")
            fecha = input("Ingrese la nueva fecha de actualización: ")
            controller.actualizar(id_editar, entidad, tema, fecha)
            print("Dato actualizado correctamente.")
        elif opcion == '4':
            id_eliminar = input("Ingrese el ID del dato a eliminar: ")
            controller.eliminar(id_eliminar)
            print("Dato eliminado correctamente.")
        elif opcion == '5':
            controller.importar_desde_api()
        elif opcion == '6':
            controller.mostrar_frecuencia_entidades()
        elif opcion == '7': # Manejo de la nueva opción
            print("\nEjecutando pruebas unitarias...")
            try:
                # Usa subprocess para ejecutar pytest en la terminal
                # Si estás en Windows, a veces es mejor usar shell=True
                # Asegúrate de que pytest esté instalado en tu entorno virtual
                result = subprocess.run(['pytest', 'tests/test_datos.py'], capture_output=True, text=True, check=True)
                print(result.stdout)
                if result.stderr:
                    print("Errores durante las pruebas:")
                    print(result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Las pruebas fallaron con el código de salida {e.returncode}")
                print(e.stdout)
                if e.stderr:
                    print("Errores durante las pruebas:")
                    print(e.stderr)
            except FileNotFoundError:
                print("Error: 'pytest' no encontrado. Asegúrate de que pytest esté instalado y en tu PATH.")
            print("Pruebas unitarias finalizadas.\n")
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    pass