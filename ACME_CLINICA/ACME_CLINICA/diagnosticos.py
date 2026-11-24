from persistencia import guardar_datos, guardar_prescripcion


def fecha_valida(fecha):
    if len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
        return False
    anio, mes, dia = fecha[0:4], fecha[5:7], fecha[8:10]
    if not (anio.isdigit() and mes.isdigit() and dia.isdigit()):
        return False
    return 1 <= int(mes) <= 12 and 1 <= int(dia) <= 31


def crear_diagnostico(datos, paciente, medico, fecha, sintomas,
                    diagnostico, medicamentos):
    """Guarda el diagnóstico en datos.json y genera el JSON de la prescripción."""
    consecutivo = len(datos["diagnosticos"]) + 1

    registro = {
        "fecha": fecha,
        "id_paciente": paciente["identificacion"],
        "id_medico": medico["identificacion"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos,
    }
    datos["diagnosticos"].append(registro)
    guardar_datos(datos)

    # Archivo de prescripción asociado a fecha, paciente y médico.
    prescripcion = {
        "fecha": fecha,
        "paciente": {
            "identificacion": paciente["identificacion"],
            "nombre": paciente["nombres"] + " " + paciente["apellidos"],
        },
        "medico": {
            "identificacion": medico["identificacion"],
            "nombre": medico["nombres"] + " " + medico["apellidos"],
        },
        "diagnostico": diagnostico,
        "medicamentos": medicamentos,
    }
    nombre = (fecha + "_" + paciente["identificacion"] + "_"
            + medico["identificacion"] + "_" + str(consecutivo) + ".json")
    return guardar_prescripcion(nombre, prescripcion)