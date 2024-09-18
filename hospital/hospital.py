from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes: List[Paciente]=[]
    medicos: List[Medico]=[]
    consultas: List[Consulta]=[]

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def eliminar_paciente(self, paciente_a_eliminar):
        for paciente in self.pacientes:
            if paciente.id == paciente_a_eliminar:
                self.pacientes.remove(paciente)
                print("Se eliminó el paciente con el ID: ", paciente_a_eliminar)
                break

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def eliminar_medico(self, medico_a_eliminar):
        for medico in self.medicos:
            if medico.id == medico_a_eliminar:
                self.medicos.remove(medico)
                print("Se eliminó el medico con el ID: ", medico_a_eliminar)
                break
    
    def mostrar_pacientes(self):
        print("\n----- Pacientes en el Sistema -----")
        if len(self.pacientes) == 0:
            print("\nNo existen pacientes en el sistema\n")
            return
        for paciente in self.pacientes:
            if paciente.ano_nacimiento > 2006:
                print("\nMenor de edad")
                paciente.mostrar_informacion_paciente()
            else:
                print("\nMayor de edad")
                paciente.mostrar_informacion_paciente()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def mostrar_medicos(self):
        print("\n----- Medicos en el Sistema -----")
        if len(self.medicos) == 0:
            print("\nNo existen medicos en el sistema\n")
            return
        for medico in self.medicos:
            medico.mostrar_informacion_medico()
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True