from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print("BIENVENIDO AL SISTEMA HOSPITAL")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Mostrar paciente")
    print("4. Mostrar medico")
    print("5. Eliminar paciente")
    print("6. Eliminar medico")
    print("7. Mostrar paciente menor de edad")
    print("8. Mostrar paciente mayor de edad")
    print("9. Salir")

    opcion_usuario = input("Selecciona la opcion deseada: ")

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
        rfc = int(input("Ingresa el RFC: "))
        direccion = input("Ingresa la direccion: ")
       
        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)

    elif opcion_usuario == "3":
        print("AAAAAAAAAAAAAAAAAAAA")

    elif opcion_usuario == "4":
        hospital.mostrar_medicos()