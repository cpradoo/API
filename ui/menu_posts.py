from negocio.posts import crear_post, editar_post, eliminar_post
from servicios.datos_api import listar_posts


def menu_posts():
    while True:
        print("\n========= Posts =========")
        print("[1] Ver todos los posts")
        print("[2] Crear post")
        print("[3] Editar post")
        print("[4] Eliminar post")
        print("[0] Volver atras")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            listar_posts()
        elif opcion == "2":
            user_id = input("ID de usuario: ")
            title = input("Titulo: ")
            body = input("Contenido: ")
            if crear_post(int(user_id), title, body):
                print("\nCreado correctamente.")
        elif opcion == "3":
            id = input("ID del post: ")
            nuevo_titulo = input("Titulo: (o Presione ENTER para mantenerlo sin cambios)")
            nuevo_body = input("Contenido: (o Presione ENTER para mantenerlo sin cambios)")
            if editar_post(int(id), nuevo_titulo, nuevo_body):
                print("\nEditado correctamente.")
        elif opcion == "4":
            id = input("ID del post: ")
            if eliminar_post(int(id)):
                print("\nEliminado correctamente.")
            else:
                print("\nPost no encontrado.")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")