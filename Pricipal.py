from CLase_Email import email
import re
import csv

if __name__ == "__main__":
    nombre = input("Ingresar Nombre ")
    correo = input("Ingrese correo ")
    contr = input("Igrese contraseña ")
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        print("Estimado",nombre,"te emviaremos tus mensajes a la direccion ",correo)
        separador = correo.split('@')
        idcuenta = separador[0]
        separador2 = separador[1].split('.')
        dom = separador2[0]
        tipo = separador2[1]
        Mail = email(idcuenta,dom,contr,tipo)
    else:
	    print ("Correo incorrecto")
        
    
    actual = input("Ingrese contraseña actual")
    if actual == Mail.getPwd():
        nueva = input("Ingrese nueva contraseña ")
        Mail.setpass(nueva)
    else:
        print("Contraseña mal ingresada ")

    Mail = email(idcuenta,dom,None,tipo)  
    correo = input("Ingrese correo ")
    while (correo != "fin"):
        m1 = Mail.CrearCuenta(correo)
        correo = input("Ingrese correo ")

    archivo = open('correos.csv')
    reader = csv.reader(archivo, delimiter = ';')
    BuscDOm = input("Ingrese dominio a buscar ")
    cont = 0
    for i in reader:
        if i[1] == BuscDOm:
            cont += 1

    print("La cantidad de correos para el dominio ",BuscDOm,"es de ",cont)     
