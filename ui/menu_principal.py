from negocio.usuarios import registrar_usuarios, iniciar_sesion
from servicios.datos_api import importar_datos_api
from ui.menu_comments import menu_comments
from ui.menu_posts import menu_posts


def menu_login():
    while True:
        print("=================")
        print("{JSON}Placeholder")
        print("=================")
        print("[1] Registrarse")
        print("[2] Iniciar Sesión")
        print("[0] Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print()
            nombre = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            registrar_usuarios(nombre, contrasena)
        elif opcion == "2":
            print()
            nombre = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            usuario = iniciar_sesion(nombre, contrasena)
            if usuario:
                menu_principal()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")


def menu_principal():
    while True:
        print("\n========= Menu =========")
        print("[1] Posts")
        print("[2] Comentarios")
        print("[3] Importar datos API")
        print("[0] Cerrar sesion")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            menu_posts()
        elif opcion == "2":
            menu_comments()
        elif opcion == "3":
            importar_datos_api()
        elif opcion == "0":
            print("Cerrando sesion...")
            break
        else:
            print("Opcion invalida.")