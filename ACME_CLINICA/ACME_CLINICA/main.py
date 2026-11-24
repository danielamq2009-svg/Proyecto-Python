from persistencia import cargar_datos
from interfaces.login import iniciar_sesion
from interfaces.menu import menu_principal


def main():
    datos = cargar_datos()

    while True:
        usuario = iniciar_sesion(datos)
        if usuario is None:
            print("Cerrando el programa.")
            break
        menu_principal(datos, usuario)


main()