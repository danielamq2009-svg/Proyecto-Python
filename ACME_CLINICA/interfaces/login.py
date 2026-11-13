from usuarios import validar_login


def iniciar_sesion(datos):
    print("=" * 50)
    print("   CLÍNICA ACME - INICIO DE SESIÓN")
    print("=" * 50)

    while True:
        email = input("Usuario (e-mail) o 'salir': ").strip()
        if email.lower() == "salir":
            return None
        contrasena = input("Contraseña: ").strip()

        usuario = validar_login(datos, email, contrasena)
        if usuario is not None:
            print("\nBienvenido/a,", usuario["nombres"], usuario["apellidos"])
            return usuario
        
        print("Usuario o contraseña incorrectos. Intente de nuevo")
