from pacientes import buscar_paciente
from usuarios import buscar_usuario_por_id


def mostrar_historia(datos, identificacion):
    """Imprime la historia clínica de un paciente por su identificación."""
    paciente = buscar_paciente(datos, identificacion)
    if paciente is None:
        print("No existe un paciente con esa identificación.")
        return

    # Encabezado: datos del paciente
    print("\n" + "=" * 50)
    print("HISTORIA CLÍNICA")
    print("=" * 50)
    print("Identificación:", paciente["identificacion"])
    print("Nombre:", paciente["nombres"], paciente["apellidos"])
    print("Teléfono:", paciente["telefono"])
    print("E-mail:", paciente["email"])
    print("Dirección:", paciente["direccion"])
    print("Género:", paciente["genero"])
    print("Estado civil:", paciente["estado_civil"])

    consultas = [d for d in datos["diagnosticos"]
                if d["id_paciente"] == identificacion]

    if len(consultas) == 0:
        print("\nEl paciente no tiene consultas registradas.")
        return

    # Cuerpo: una sección por consulta
    numero = 1
    for consulta in consultas:
        medico = buscar_usuario_por_id(datos, consulta["id_medico"])
        if medico is not None:
            nombre_medico = medico["nombres"] + " " + medico["apellidos"]
        else:
            nombre_medico = consulta["id_medico"]

        print("\n" + "-" * 50)
        print("Consulta", numero)
        print("Fecha:", consulta["fecha"])
        print("Médico:", nombre_medico)
        print("Síntomas:", ", ".join(consulta["sintomas"]))
        print("Diagnóstico:", consulta["diagnostico"])
        print("Medicamentos prescritos:")
        for med in consulta["medicamentos"]:
            print("  -", med["medicamento"],
                "| Cantidad:", med["cantidad"],
                "| Dosis:", med["dosis"],
                "| Días:", med["dias_tratamiento"])
        numero += 1
    print("=" * 50)