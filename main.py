from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Registrar pacientes")
    print("2. Registrar medico")
    print("3. Mostrar pacientes")
    print("4. Mostar medicos")
    print("5. Eliminar pacientes")
    print("6. Eliminar medicos")
    print("7. Mostrar paciente menor de edad")
    print("8. Mostrar paciente mayor de edad")
    print("9. Salir")

    opcion_usuario = input("Ingresa la opción que deseas: ")

    if opcion_usuario == "1":
        print("Seleccionaste la opcion para registrar un paciente")

        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        peso = float(input("Ingresa el peso: "))
        estatura = float(input("Ingresa la estatura: "))
        direccion = input("Ingresa la direccion: ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)

        print("Paciente registrado correctamente")

    elif opcion_usuario == "2":
        print("Seleccionaste la opcion para registrar medico")

        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        rfc = input("Ingresa el RFC: ")
        direccion = input("Ingresa la direccion: ")
       
        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)

        print("Medico registrado correctamente")

    elif opcion_usuario == "3":
        print("\n**PACIENTES EN EL SISTEMA**")
        hospital.mostrar_pacientes()

    elif opcion_usuario == "4":
        print("\n**MEDICOS EN EL SISTEMA**")
        hospital.mostrar_medicos()

    elif opcion_usuario == "5":
        paciente_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(paciente_a_eliminar)

    elif opcion_usuario == "6":
        medico_a_eliminar = int(input("Ingresa el ID del medico a eliminar: "))
        hospital.eliminar_medico(medico_a_eliminar)

    elif opcion_usuario == "7":
        print("\n**PACIENTES MENORES DE EDAD EN EL SISTEMA**")
        hospital.mostrar_pacientes_menores()

    elif opcion_usuario == "8":
        print("\n**PACIENTES MAYORES DE EDAD EN EL SISTEMA**")
        hospital.mostrar_pacientes_mayores()

    elif opcion_usuario == "9":
        print("\nSalio del sistema")
        break
    else:
        print("\nOpción no disponible")
        break