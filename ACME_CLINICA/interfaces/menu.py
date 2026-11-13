from usuarios import registrar_usuario
from pacientes import registrar_paciente, buscar_paciente
from diagnosticos import crear_diagnostico, fecha_valida
from historia_clinica import mostrar_historia


# ---------- Funciones auxiliares de entrada ----------

def pedir_texto(mensaje):
    """Pide un texto y no deja continuar si está vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("El campo no puede estar vacío.")


def pedir_entero(mensaje):
    """Pide un entero mayor que cero."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Ingrese un número entero mayor que cero.")


def pedir_opcion(mensaje, opciones):
    """Muestra opciones numeradas y devuelve el texto de la elegida."""
    print(mensaje)
    for i in range(len(opciones)):
        print(" ", i + 1, "-", opciones[i])
    while True:
        valor = input("Seleccione una opción: ").strip()
        if valor.isdigit() and 1 <= int(valor) <= len(opciones):
            return opciones[int(valor) - 1]
        print("Opción no válida.")


def pedir_si_no(mensaje):
    while True:
        valor = input(mensaje + " (s/n): ").strip().lower()
        if valor == "s":
            return True
        if valor == "n":
            return False
        print("Responda con 's' o 'n'.")


# ---------- Opciones del menú ----------

def opcion_registrar_usuario(datos):
    print("\n--- REGISTRO DE USUARIO ---")
    identificacion = pedir_texto("No. de identificación: ")
    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")
    telefono = pedir_texto("Teléfono: ")
    email = pedir_texto("E-mail corporativo: ")
    direccion = pedir_texto("Dirección: ")
    rol = pedir_opcion("Tipo de usuario:", ["medico", "administrativo"])

    ok, mensaje, contrasena = registrar_usuario(datos, identificacion, nombres,
                                                apellidos, telefono, email,
                                                direccion, rol)
    print(mensaje)
    if ok:
        print("\n*** CREDENCIALES DEL NUEVO USUARIO ***")
        print("Usuario (e-mail):", email.lower())
        print("Contraseña generada:", contrasena)
        print("Entréguesela al usuario; no se volverá a mostrar.")


def opcion_registrar_paciente(datos):
    print("\n--- REGISTRO DE PACIENTE ---")
    identificacion = pedir_texto("No. de identificación: ")
    nombres = pedir_texto("Nombres: ")
    apellidos = pedir_texto("Apellidos: ")
    telefono = pedir_texto("Teléfono: ")
    email = pedir_texto("E-mail: ")
    direccion = pedir_texto("Dirección: ")
    genero = pedir_opcion("Género:", ["Masculino", "Femenino"])
    estado_civil = pedir_opcion("Estado civil:", ["Soltero/a", "Casado/a",
                                "Unión libre", "Divorciado/a", "Viudo/a"])

    ok, mensaje = registrar_paciente(datos, identificacion, nombres, apellidos,
                                    telefono, email, direccion, genero,
                                    estado_civil)
    print(mensaje)


def opcion_diagnosticar(datos, usuario):
    print("\n--- DIAGNOSTICAR PACIENTE ---")

    if usuario["rol"] != "medico":
        print("Solo los médicos pueden diagnosticar pacientes.")
        return

    identificacion = pedir_texto("Identificación del paciente: ")
    paciente = buscar_paciente(datos, identificacion)
    if paciente is None:
        print("El paciente no está registrado. Regístrelo primero.")
        return
    print("Paciente:", paciente["nombres"], paciente["apellidos"])

    fecha = pedir_texto("Fecha de la consulta (AAAA-MM-DD): ")
    while not fecha_valida(fecha):
        print("Formato de fecha no válido.")
        fecha = pedir_texto("Fecha de la consulta (AAAA-MM-DD): ")

    # 1. Síntomas
    print("\nSíntomas (deje vacío y presione Enter para terminar):")
    sintomas = []
    while True:
        sintoma = input("  Síntoma " + str(len(sintomas) + 1) + ": ").strip()
        if sintoma == "":
            if len(sintomas) == 0:
                print("Debe registrar al menos un síntoma.")
                continue
            break
        sintomas.append(sintoma)

    # 2. Diagnóstico
    diagnostico = pedir_texto("\nDiagnóstico (patología o enfermedad): ")

    # 3. Prescripción médica
    print("\nPrescripción médica:")
    medicamentos = []
    while True:
        nombre = pedir_texto("  Medicamento: ")
        cantidad = pedir_entero("  Cantidad (unidades): ")
        dosis = pedir_texto("  Dosis diaria (ej: 1 tableta cada 8 horas): ")
        dias = pedir_entero("  Tiempo de aplicación (días): ")
        medicamentos.append({
            "medicamento": nombre,
            "cantidad": cantidad,
            "dosis": dosis,
            "dias_tratamiento": dias,
        })
        if not pedir_si_no("¿Agregar otro medicamento?"):
            break

    ruta = crear_diagnostico(datos, paciente, usuario, fecha, sintomas,
                            diagnostico, medicamentos)
    print("\nDiagnóstico registrado. Prescripción generada en:", ruta)


def opcion_historia_clinica(datos):
    print("\n--- HISTORIA CLÍNICA ---")
    identificacion = pedir_texto("Identificación del paciente: ")
    mostrar_historia(datos, identificacion)


# ---------- Menú principal ----------

def menu_principal(datos, usuario):
    while True:
        print("\n" + "=" * 50)
        print("   CLÍNICA ACME - MENÚ PRINCIPAL")
        print("   Usuario:", usuario["nombres"], "(" + usuario["rol"] + ")")
        print("=" * 50)
        print("1. Registrar usuario")
        print("2. Registrar paciente")
        print("3. Diagnosticar paciente")
        print("4. Historia clínica")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_registrar_usuario(datos)
        elif opcion == "2":
            opcion_registrar_paciente(datos)
        elif opcion == "3":
            opcion_diagnosticar(datos, usuario)
        elif opcion == "4":
            opcion_historia_clinica(datos)
        elif opcion == "5":
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")