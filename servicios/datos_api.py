from datos.crud import crear_objeto, obtener_por_id, obtener_todos
from modelos.modelos import Post, Comment
from servicios.conexion_api import obtener_posts, obtener_comments


def importar_datos_api():
    posts = obtener_posts()
    comments = obtener_comments()
    for post in posts:
        post = Post(id=post["id"], userId=post["userId"], title=post["title"], body=post["body"])
        crear_objeto(post)
    for comment in comments:
        comment = Comment(id=comment["id"], postId=comment["postId"], name=comment["name"], email=comment["email"], body=comment["body"])
        crear_objeto(comment)
    print("Posts y Comments importados correctamente.")


def listar_posts():
    posts = obtener_todos(Post)
    if not posts:
        return print("No hay posts.")
    for post in posts:
        print(f"[{post.id}] {post.title}: {post.body[:25]}")


def listar_comments(post_id):
    post = obtener_por_id(Post, post_id)
    if not post:
        print("ID invalida.")
        return
    print(f'\nComentarios del post nº{post.id}: "{post.title}"\n')
    if not post.comments:
        print("Este post no tiene comentarios.")
        return
    for comment in post.comments:
        print(f"- [{comment.id}] {comment.name}: {comment.body[:25]}...")