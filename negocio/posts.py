from modelos.modelos import Post
from datos.crud import crear_objeto, obtener_por_id, actualizar, eliminar_objeto


def crear_post(userId, title, body):
    post = Post(userId=userId, title=title, body=body)
    return crear_objeto(post)


def editar_post(id, nuevo_titulo=None, nuevo_body=None):
    post = obtener_por_id(Post, id)
    if not post:
        return None
    if nuevo_titulo:
        post.title = nuevo_titulo
    if nuevo_body:
        post.body = nuevo_body
    actualizar()
    return post


def eliminar_post(id):
    post = obtener_por_id(Post, id)
    if not post:
        return None
    eliminar_objeto(post)
    return True