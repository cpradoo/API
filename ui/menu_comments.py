from negocio.comments import crear_comment, editar_comment, eliminar_comment
from servicios.datos_api import listar_comments


def menu_comments():
    while True:
        print("\n========= Comments =========")
        print("[1] Ver todos los comments de un post")
        print("[2] Crear comment")
        print("[3] Editar comment")
        print("[4] Eliminar comment")
        print("[0] Volver atras")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            post_id = int(input("ID del post: "))
            listar_comments(post_id)
        elif opcion == "2":
            post_id = int(input("ID del post: "))
            name = input("Nombre: ")
            email = input("Email: ")
            body = input("Contenido: ")
            if crear_comment(post_id, name, email, body):
                print("\nCreado correctamente.")
        elif opcion == "3":
            id = int(input("ID del comment: "))
            nuevo_body = input("Nuevo contenido (o Presione ENTER para mantenerlo sin cambios): ")
            if editar_comment(id, nuevo_body):
                print("\nEditado correctamente.")
        elif opcion == "4":
            id = int(input("ID del comentario: "))
            if eliminar_comment(id):
                print("\nEliminado correctamente.")
            else:
                print("\nComentario no encontrado.")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")