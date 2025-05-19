from app import app, db
from app.controllers import datos_controller as controller

with app.app_context():
    db.create_all()

with app.app_context():
    while True:
        print("\nMenú:")
        print("1. Listar datos locales")
        print("2. Agregar dato")
        print("3. Actualizar dato")
        print("4. Eliminar dato")
        print("5. Traer datos desde API")
        print("6. Mostrar frecuencia de publicación por entidad")
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
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    pass