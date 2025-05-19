class DatosView:
    @staticmethod
    def mostrar_menu():
        print("""Menú:
1. Listar datos locales
2. Agregar dato
3. Actualizar dato
4. Eliminar dato
5. Traer datos desde API
0. Salir""")

    @staticmethod
    def mostrar_lista(datos):
        for d in datos:
            print(d)

    @staticmethod
    def mostrar_api(datos):
        for d in datos:
            print(d)