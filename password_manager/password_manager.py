#pip install cryptography
from cryptography.fernet import Fernet

##FUNCION QUE SOLO SE UTILIZARA UNA SOLA VEZ PARA CREAR LA KEY DE LA PASSWORD
'''
def write_key():
    #GENERA UNA LLAVE CON LA LIBRERIA EXTERNA
    key = Fernet.generate_key()
    #CREA UN ARCHIVO PARA GUARDAR LA LLAVE SI NO LO HAY Y SE REALIZA LA RESPECTIVA ESCRITURA
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

#LUEGO QUE SE CARGA LA KEY ENTONCES SE PUEDE UTILIZAR ESTA FUNCION
def load_key():
    #ABRE EL ARCHIVO EN LECTURA DE BYTES 
    file = open("key.key", "rb")
    #GUARDA LA LLAVE
    key = file.read()
    #CIERRA EL ARCHIVO
    file.close()
    #DEVUELVE LA LLAVE
    return key

#SE LE PIDE AL USUARIO LA CONTRASEÑA
master_pwd = input("¿Cual es tu contraseña maestra? -->" ).lower()
#SE CREA UNA LLAVE CON LA CONTRASEÑA DEL USUARIO MASTER CODIFICADA EN BYTES
key = load_key() + master_pwd.encode()
#SE CODIFICA LA LLAVE ANTERIOR
fer = Fernet(key)

#MUESTRA LAS CONTRASEÑAS
def view():
    #ABRE EL ARCHIVO EN SOLO LECTURA
    with open("password-list.txt", "r") as f:
        #LEE LINEA POR LINEA LOS DATOS
        for line in f.readlines():
            #GUARDA LA LINEA ACTUAL Y HACE UN RETORNO DE CARRO
            data = line.rstrip()
            #DIVIDE LOS DATOS CONVIRTIENDO EN UN ARRAY DEPENDIENDO DEL SEPARADOR
            user, passw = data.split("|")
            #SE IMPRIMEN LOS RESPECTIVOS DATOS UTILIZANDO EL ARRAY ANTERIOR
            #LA CONSTRASEÑA SE DESENCRITA CON LA INSTANCIA DE FER
            print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())

#AGREGA UNA CONTRASELA A LA LISTA DEL ARCHIVO
def add():
    #SE PIDE EL NOMBRE
    name = input("Account name: ")
    #SE PIDE LA CONTRASEÑA
    pwd = input("Password: ")
    
    #ENCRYPTADO DE CONTRASEÑA
    #SE ENCRIPTA EN BYTES
    #SE ABRE EL ARCHIVO EN MODO ESCRITURA EN BYTES
    with open("password-list.txt", "a") as f:
        #SE ESCRIBEN LOS RESPECTIVOS DATOS LA CONTRASEÑA SE ENCRYPTA CON LA INSTANCIA DE FER O LA LLAVE MAESTRA
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Te gustaria agregar una password o ver las existentes, (view, add), presiona \"q\" para salir -->").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Modo invalido.")
        continue