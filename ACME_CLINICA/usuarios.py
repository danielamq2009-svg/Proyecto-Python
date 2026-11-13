import random
from persistencia import guardar_datos, cargar_datos

# Validación básica de formato de e-mail.
def email_valido(email):
    if " " in email or email.count("@") != 1:
        return False
    local, dominio = email.split("@")
    return (local != "" and "." in dominio
            and not dominio.startswith(".") and not dominio.endswith("."))


def buscar_usuario_por_id(datos, identificacion):
    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == identificacion:
            return usuario
    return None


def buscar_usuario_por_email(datos, email):
    for usuario in datos["usuarios"]:
        if usuario["email"] == email.lower():
            return usuario
    return None

# Genera una contraseña de 8 caracteres.
def generar_contrasena():
    caracteres = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    contraseña = ""
    for i in range(8):
        contraseña = contraseña + random.choice(caracteres)
    return contraseña

# Registra un usuario con contraseña generada.
def registrar_usuario(datos, identificacion, nombres, apellidos,
                    telefono, email, direccion, rol):
    if not email_valido(email):
        return False, "El e-mail no tiene un formato válido.", None
    if buscar_usuario_por_id(datos, identificacion) is not None:
        return False, "Ya existe un usuario con esa identificación.", None
    if buscar_usuario_por_email(datos, email) is not None:
        return False, "Ya existe un usuario con ese e-mail.", None

    contrasena = generar_contrasena()

    datos["usuarios"].append({
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email.lower(),
        "direccion": direccion,
        "rol": rol,
        "contrasena": contrasena,
    })
    guardar_datos(datos)

    # Verifica que realmente quedó guardado en el archivo
    datos_archivo = cargar_datos()
    if buscar_usuario_por_id(datos_archivo, identificacion) is None:
        return False, "Error: el usuario no se pudo guardar en datos.json.", None

    return True, "Usuario registrado y guardado correctamente.", contrasena

# Devuelve el usuario si las credenciales son correctas, si no None.
def validar_login(datos, email, contrasena):
    usuario = buscar_usuario_por_email(datos, email)
    if usuario is not None and usuario["contrasena"] == contrasena:
        return usuario
    return None