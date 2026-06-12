class Persona:

    def __init__(self):
        self.__nombre=""
        self.__usuario=""
        self.__correo=""
        self.__id=0
        self.__numerotelefono=""

    def set__nombre(self,no):
        self.__nombre=no
 
    def set__usuario(self,u):
        self.__usuario=u

    def set__correo(self,co):
        self.__correo=co

    def set__id(self,i):
        self.__id=i

    def set__numerotelefono(self,note):
        self.__numerotelefono=note

    def get__nombre(self):
        return self.__nombre

    def get__usuario(self):
        return self.__usuario
    
    def get__correo(self):
        return self.__correo
    
    def get__id(self):
        return self.__id
    
    def get__numero_telefono(self):
        return self.__numerotelefono

