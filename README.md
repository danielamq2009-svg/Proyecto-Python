# Proyecto-Python
Sistema de clinica ACME
En este repositorio se encuentra el proyecto realizado en el curso de Python haciendo un sistema para una clinica.
La clínica ACME ha decidido sistematizar el proceso de diagnósticos de sus pacientes, ya que dicho proceso es llevado actualmente de manera manual, ralentizando el préstamo del servicio de salud. Los siguientes son los requerimientos que se deben plasmar en la aplicación:

 

Login
Es la interfaz que debe permitir el acceso a las opciones del sistema, donde debe aparecer una vez iniciado el programa para que el usuario, contando con un usuario y contraseña que se le asigna al momento del registro en la plataforma, pueda acceder al sistema.

 

Registro de usuarios
Los usuarios son las personas operarias de la clínica, las cuales pueden ser médicos o administrativos y son las encargadas de gestionar la información en el sistema. Los datos para registrar a una persona adentro del sistema son las siguientes:

Número de identificación, nombres, apellidos, número de teléfono, e-mail (corporativo) y dirección.



Estos usuarios podrán acceder al sistema mediante un nombre de usuario (que para este caso será el e-mail) y una contraseña asignada a la hora de hacer el registro de dicho usuario.



Nota: Dado a que el registro de usuario deben hacerlo los usuarios que se puedan autenticar en el sistema, se deberá crear (en el archivo de persistencia de datos) un primer usuario que tenga la siguiente información:

No. Identificación: 0000

Nombre: Admin

Apellidos: Administrador

No. De Teléfono: 555 000111

e-mail: admin@acmeclinic.com

Dirección: Cl 185 # 26 – 85

 

Registro de pacientes
Los pacientes son los usuarios finales de ACME, a los cuales se les atiende, se toman datos clínicos y se les hace un diagnostico de la enfermedad que padecen. Los datos para el registro de un paciente adentro del sistema son los siguientes: Número de identificación, nombres, apellidos, número de teléfono, e-mail, dirección, género y estado civil.

 

Diagnosticar pacientes
Para el diagnostico de un paciente, este deberá estar registrados en el sistema previamente para empezar el con el proceso de la siguiente manera:

Síntomas: El doctor realiza preguntas sobre las aflicciones al paciente y va registrando en el sistema estas.
Diagnóstico: Una vez que el médico conoce los síntomas que presenta el paciente, este describe la patología o enfermedad que presenta dicho paciente.
Prescripción médica: Cuando se tenga el diagnostico, el médico procederá a prescribir la medicación que ayude al paciente con sus síntomas, para lo cual debe registrarlos así: Medicamento, cantidad, dosis (cuanto del medicamento debe tomar diariamente), Tiempo de aplicación (días que demora el tratamiento con la medicación).
Una vez terminado el diagnostico, el sistema debe generar la prescripción medica en un archivo JSON, el cual estará asociado a una fecha, un paciente y a un médico.

 

Historia Clínica
Esta opción permitirá al usuario del sistema obtener el historial de consultas de un paciente, el cual se debe generar a través del número de identificación de este. Aquí deberá mostrar como encabezado del historial todos los datos del paciente y como cuerpo del historial la fecha de la consulta, el médico que atendió al paciente, los síntomas, el diagnostico y los medicamentos prescritos.

