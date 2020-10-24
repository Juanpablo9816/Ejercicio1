import re
class email():
    __idcuenta = ""
    __dominio = ""
    __contraseña = ""
    __tipoDom = ""

    def __init__(self,idc,dom,con,tipo):
        self.__idcuenta = idc
        self.__dominio = dom
        self.__contraseña = con
        self.__tipoDom = tipo
    
    def RetornaEmail(self):
        s = str(self.__idcuenta)
        s += "@"+str(self.__dominio)
        s += "."+str(self.__tipoDom)
      
        return s
    def GetDom(self):
        return self.__dominio
      
    def CrearCuenta(self,correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            separador = correo.split('@')
            idcuenta = separador[0]
            separador2 = separador[1].split('.')
            dom = separador2[0]
            tipo = separador2[1]
            return email(idcuenta,dom,None,tipo)
    def getPwd(self):
        return self.__contraseña
    def setpass(self,new):
        self.__contraseña = new
