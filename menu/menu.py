from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from datetime import datetime
from usuario.utils.roles import Rol


class Menu:
    escuela: Escuela = Escuela()

    ususario_estudiante: str = "juan123"
    contrasenia_estudiante: str = "12345*";

    ususario_maestro: str = "hilary123"
    contrasenia_maestro: str = "54321*";

    escuela = Escuela()

    def login(self):
        intentos = 0
        while intentos < 5:
            print("*** BIENVENIDO ***")
            print("Inicia sesión para Continuar")

            numero_control = input("Ingresa tu numero de control: ")
            contraseña_usuario = input("Ingresa tu contraseña: ")

            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contrasenia=contraseña_usuario)
               
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            else:
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else:
                    self.mostrar_menu()
                    intentos = 0
            

        print("Máximos intentos de inicio de sesión alcanzados")

    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("Usuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1
        


    def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion != 9:
            print("\n** MINDBOX **\n")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Ver maestros")
            print("4. Ver materias")
            print("5. Ver semestres")
            print("6. Ver carreras")
            print("7. Registrar horario")
            print("8. Ver mi informacion")#TAREA
            print("9. Salir")

            opcion = int(input("Ingrese una opcion: "))

            if opcion == 9:
                break

    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 9:
            print("\n** MINDBOX **\n")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print("5. Ver semestres")
            print("6. Ver carreras")
            print("7. Registar horario")
            print("8. Ver mi informacion")
            print("9. Salir")

            opcion = int(input("Ingrese una opcion: "))

            if opcion == 5:
                break


    def mostrar_menu(self):
        while True:
            print("** MINDBOX **")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo") 
            print("5. Registrar horario") #no
            print("6. Mostrar estudiantes")
            print("7. Mostrar maestros")
            print("8. Mostrar materias")
            print("9. Mostrar grupos")
            print("10. Eliiminar estudiante") 
            print("11. Eliminar maestro") 
            print("12. Eliminar materia") 
            print("13. Registrar carrera")
            print("14. Registrar semestre")
            print("15. Mostrar carrera")
            print("16. Mostrar semestre")
            print("17. Ver mi informacion")
            print("20. Salir")

            opcion = input("Ingresa una opción para continuar: ")

            if opcion == "1":
                print("\nSeleccionaste la opcion para registrar estudiante")

                generar_numero_control_estudiante = self.escuela.generar_numero_control_estudiante()
                print("Numero de control del estudiante:", generar_numero_control_estudiante)

                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)

                contrasenia = input("Ingresa la contraseña del estudiante: ")

                estudiante = Estudiante(numero_control=generar_numero_control_estudiante, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contrasenia=contrasenia)
                self.escuela.registrar_estudiante(estudiante)

            elif opcion =="2":
                print("\nSeleccionaste la opcion para registrar maestro")
                
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
                rfc = input("Ingresa la rfc del maestro: ")
                sueldo = input("Ingresa el sueldo del maestro: ")

                contrasenia = input("Ingresa la contraseña del estudiante: ")

                maestro = Maestro(numero_control="",nombre=nombre, ano_nacimiento=ano_nacimiento, apellido=apellido, rfc=rfc, sueldo=sueldo, contrasenia=contrasenia)
                
                generar_numero_control_maestro = self.escuela.generar_numero_control_maestro(maestro)
                maestro.numero_control=generar_numero_control_maestro

                self.escuela.registrar_maestro(maestro)

                print("Numero de control del maestro:", generar_numero_control_maestro)
                
            elif opcion =="3":
                print("\nSeleccionaste la ocpion para registrar materia")

                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripcion: ")
                semestre = int(input("Ingresa el semestre: "))
                creditos = int(input("Ingresa los creditos: "))

                materia = Materia(id_materia="", nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)

                generar_id_materia = self.escuela.generar_id_materia(materia)
                materia.id_materia = generar_id_materia

                self.escuela.registrar_materia(materia)

                print("ID de la materia:", generar_id_materia)

            elif opcion =="4":
                print("\nSeleccionaste la opcion para registrar un nuevo grupo: ")

                tipo = input("Ingresa el tipo de grupo (A/B): ")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")

                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion =="5":
                pass
            elif opcion == "6":
                self.escuela.listar_estudiantes()
            elif opcion == "7":
                self.escuela.listar_maestros()
            elif opcion == "8":
                self.escuela.listar_materias()
            elif opcion == "9":
                self.escuela.listar_grupos()

            elif opcion == "10":
                print("\nSeleccionaste la opcion para eliminar un estudiante")

                numero_control = input("Ingresa el numero de control del estudiante: ")
                
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "11":
                print("\nSeleccionaste la opcion para eliminar un maestro")

                numero_control = input("Ingresa el numero de control del maestro: ")
                
                self.escuela.eliminar_maestro(numero_control=numero_control)

            elif opcion == "12":
                print("\nSeleccionaste la opcion para eliminar un materia")

                id_materia = input("Ingresa el ID de la materia: ")
                
                self.escuela.eliminar_materia(id_materia=id_materia)
            
            elif opcion == "13":
                print("\nSeleccionaste la opcion para registrar una carrera")

                nombre = input("Ingresa el nombre de la carrera: ")

                carrera = Carrera(nombre=nombre)

                self.escuela.registrar_carrera(carrera=carrera)

            elif opcion == "14":
                print("\nSeleccionaste la opcion registrar semestre")

                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")

                semestre = Semestre(numero=numero, id_carrera=id_carrera)

                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion == "15":
                self.escuela.listar_carrera()
        
            elif opcion == "16":
                self.escuela.listar_semestre()

            elif opcion == "17":
                self.coordinador.mostrar_info_coordinador(numero_control)

            elif opcion =="20":
                print("\nHasta luego")
                break