from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime 

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo") #no
    print("5. Registrar horario") #no
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")#no
    print("10. Eliiminar estudiante") 
    print("11. Eliminar maestro") #no TAREA
    print("12. Eliminar materia") #NO TAREA
    print("13. Salir")

    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar estudiante")

        generar_numero_control_estudiante = escuela.generar_numero_control_estudiante()
        print("Numero de control del estudiante:", generar_numero_control_estudiante)

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
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        rfc = input("Ingresa la rfc del maestro: ")
        sueldo = input("Ingresa el sueldo del maestro: ")

        maestro = Maestro(numero_control="",nombre=nombre, ano_nacimiento=ano_nacimiento, apellido=apellido, rfc=rfc, sueldo=sueldo)
        
        generar_numero_control_maestro = escuela.generar_numero_control_maestro(maestro)
        maestro.numero_control=generar_numero_control_maestro

        escuela.registrar_maestro(maestro)

        print("Numero de control del maestro:", generar_numero_control_maestro)
        
    elif opcion =="3":
        print("\nSeleccionaste la ocpion para registrar materia")

        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion: ")
        semestre = int(input("Ingresa el semestre: "))
        creditos = int(input("Ingresa los creditos: "))

        materia = Materia(id_materia="", nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)

        generar_id_materia = escuela.generar_id_materia(materia)
        materia.id_materia = generar_id_materia

        escuela.registar_materia(materia)

        print("ID de la materia:", generar_id_materia)

    elif opcion =="4":
        pass
    elif opcion =="5":
        pass
    elif opcion == "6":
        escuela.listar_estudiantes()
    elif opcion == "7":
        escuela.listar_maestros()
    elif opcion == "8":
        escuela.listar_materias()

    elif opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante")

        numero_control = input("Ingresa el numero de control del estudiante: ")
        
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("\nSeleccionaste la opcion para eliminar un maestro")

        numero_control = input("Ingresa el numero de control del maestro: ")
        
        escuela.eliminar_maestro(numero_control=numero_control)

    elif opcion == "12":
        print("\nSeleccionaste la opcion para eliminar un materia")

        id_materia = input("Ingresa el ID de la materia: ")
        
        escuela.eliminar_materia(id_materia=id_materia)

  
    elif opcion =="13":
        print("\nHasta luego")
        break