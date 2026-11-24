import json

# Rutas relativas: ejecutar main.py desde la carpeta ACME_CLINICA.
RUTA_DATOS = "DATOS/datos.json"
RUTA_DATOS_MEDICO = "DATOS/reporte_carga_medicos.json"
CARPETA_DIAGNOSTICOS = "DATOS/diagnosticos/"

# Estructura inicial con el usuario administrador del enunciado.
def _datos_iniciales():
    return {
        "usuarios": [
            {
                "identificacion": "0000",
                "nombres": "Admin",
                "apellidos": "Administrador",
                "telefono": "555 000111",
                "email": "admin@acmeclinic.com",
                "direccion": "Cl 185 # 26 – 85",
                "rol": "administrativo",
                "contrasena": "admin123",
            }
        ],
        "pacientes": [],
        "diagnosticos": [],
    }

# Guarda los datos en el archivo JSON.
def guardar_datos(datos):
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Carga los datos. Si el archivo no existe, lo crea con el admin.
def cargar_datos():
    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        datos = _datos_iniciales()
        guardar_datos(datos)
        return datos

# Guarda una prescripción médica como archivo JSON independiente."""
def guardar_prescripcion(nombre_archivo, prescripcion):
    ruta = CARPETA_DIAGNOSTICOS + nombre_archivo
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(prescripcion, archivo, indent=4, ensure_ascii=False)
    return ruta

def guardar_datos_medicos(datos):
    with open(RUTA_DATOS_MEDICO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)