from persistencia import guardar_datos, cargar_datos
from usuarios import email_valido


def buscar_paciente(datos, identificacion):
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            return paciente
    return None


def registrar_paciente(datos, identificacion, nombres, apellidos, telefono,
                    email, direccion, genero, estado_civil):
    if not email_valido(email):
        return False, "El e-mail no tiene un formato válido (ej: ana@correo.com)."
    if buscar_paciente(datos, identificacion) is not None:
        return False, "Ya existe un paciente con esa identificación."

    datos["pacientes"].append({
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email.lower(),
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil,
    })
    guardar_datos(datos)

    # Verifica que realmente quedó guardado en el archivo
    datos_archivo = cargar_datos()
    if buscar_paciente(datos_archivo, identificacion) is None:
        return False, "Error: el paciente no se pudo guardar en datos.json."

    return True, "Paciente registrado y guardado correctamente."