from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime 

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")

    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar estudiante")

        generar_numero_control_estudiante = escuela.generar_numero_control_estudiante()
        print(generar_numero_control_estudiante)

        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante(numero_control=generar_numero_control_estudiante, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante)

    elif opcion =="2":
        print("\nSeleccionaste la opcion para registrar maestro")
        
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano = int(input("Ingresa el año de nacimiento del maestro: "))
        rfc = input("Ingresa la rfc del maestro: ")
        sueldo = input("Ingresa el sueldo del maestro: ")

        maestro = Maestro(numero_control="",nombre=nombre, ano_nacimiento=ano, apellido=apellido, rfc=rfc, sueldo=sueldo)
        
        generar_numero_control_maestro = escuela.generar_numero_control_maestro(maestro)
        maestro.numero_control=generar_numero_control_maestro

        escuela.registrar_maestro(maestro)

        print(generar_numero_control_maestro)
        
    elif opcion =="3":
        pass
    elif opcion =="4":
        pass
    elif opcion =="5":
        pass
    elif opcion =="6":
        print("\nHasta luego")
        break