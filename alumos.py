from Personas import Persona

class Alumno (Persona):

    def __init__(self):
        super().__init__()

        self.__semestre=0
        self.__materias=[]
        self.__calificacion1=0
        self.__calificacion2=0
        self.__calificacion3=0
        self.__calificacionlobal=0

    def calcular_calificaciones(self):
        return self.__calificacion1 + self.__calificacion2 + self.__calificacion3

    def set__semestre(self,sem):
        self.__semestre=sem

    def set__materias(self,lima):
        self.__materias=lima
    
    def set__calificacion1(self,cal1):
        self.__calificacion1=cal1

    def set__calificacion2(self,cal2):
        self.__calificacion2=cal2

    def set__calificacion3(self,cal3):
        self.__calificacion3=cal3            

    def set__calificacion_global(self,cagl):
        self.__calificacionlobal=cagl
    
    def get__semestre(self):
        return self.__semestre
    
    def get__materias(self):
        return self.__materias
    
    def get__calificacion1(self):
        return self.__calificacion1
    
    def get__calificacion2(self):
        return self.__calificacion2
    
    def get__calificacion3(self):
        return self.__calificacion3

    def get__calificacionglobal(self):
        return self.__calificacionlobal
    
