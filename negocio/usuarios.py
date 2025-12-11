import bcrypt
from modelos.modelos import Usuario
from datos.conexion import sesion


def registrar_usuarios(nombre, contrasena):
    hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    nuevo_usuario = Usuario(nombre=nombre, contrasena=hash.decode('utf-8'))
    sesion.add(nuevo_usuario)
    sesion.commit()
    print("Registrado correctamente")


def iniciar_sesion(nombre, contrasena):
    usuario = sesion.query(Usuario).filter_by(nombre=nombre).first()
    if usuario is None:
        print("Usuario no existe.")
        return False
    if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        print("\nLogin exitoso")
        return True
    else:
        print("Contraseña incorrecta.")
        return False