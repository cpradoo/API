from modelos.modelos import Comment
from datos.crud import crear_objeto, obtener_por_id, actualizar, eliminar_objeto


def crear_comment(postId, name, email, body):
    comment = Comment(postId=postId, name=name, email=email, body=body)
    return crear_objeto(comment)


def editar_comment(id, nuevo_body=None):
    comment = obtener_por_id(Comment, id)
    if not comment:
        return None
    if nuevo_body:
        comment.body = nuevo_body
    actualizar()
    return comment


def eliminar_comment(id):
    comment = obtener_por_id(Comment, id)
    if not comment:
        return None
    eliminar_objeto(comment)
    return True