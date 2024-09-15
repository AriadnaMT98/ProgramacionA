"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Av. Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Av. Madero") # 5
paciente_tres = Paciente("Rodrigo", 2010, 56, 1.60, "Av. Reforma")

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo")
medico_dos = Medico("Carlos", 1980, "JHK9834IRDPO", "Av. Puebla") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)

hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico=medico_dos)

while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Mostrar pacientes")
    print("2. Mostar medicos")
    print("3. Eliminar pacientes")
    print("4. Eliminar medicos")
    print("5. Salir")

    opcion = input("Ingresa la opción que deseas: ")

    if opcion == "1":
        hospital.mostrar_pacientes()
    elif opcion == "2":
        hospital.mostrar_medicos()
    elif opcion == "3":
        paciente_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(paciente_a_eliminar)
    elif opcion == "4":
        medico_a_eliminar = int(input("Ingresa el ID del medico a eliminar: "))
        hospital.eliminar_medico(medico_a_eliminar)
    elif opcion == "5":
        print("\nSalio del sistema")
        break
    else:
        print("\nOpción no disponible")
        break


#hospital.registrar_consulta(id_paciente=1, id_medico=1)