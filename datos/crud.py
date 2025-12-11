from datos.conexion import sesion


def crear_objeto(objeto):
    sesion.add(objeto)
    sesion.commit()
    return objeto


def obtener_por_id(modelo, id):
    return sesion.query(modelo).get(id)


def obtener_todos(modelo):
    return sesion.query(modelo).all()


def actualizar():
    sesion.commit()


def eliminar_objeto(objeto):
    sesion.delete(objeto)
    sesion.commit()