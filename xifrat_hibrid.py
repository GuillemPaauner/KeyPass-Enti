from cryptography.fernet import Fernet
import os


# Nombre del archivo donde se guarda la clave
CLAU_FILE = "clau_fernet.key"


def guardar_clau(clau):
    # Abrimos el archivo en modo escritura binaria (se utiliza para guaradar claves)
    with open(CLAU_FILE, "wb") as f:
        # Escribimos la clave en el archivo
        f.write(clau)


def carregar_clau():
    # Comprobamos si el archivo de la clave existe
    if os.path.exists(CLAU_FILE):
        # Si existe, abrimos el archivo y leemos la clave binaria
        with open(CLAU_FILE, "rb") as f:
            return f.read()

    # Si no existe, generamos una clave nueva
    clau = Fernet.generate_key()

    # Guardamos la nueva clave
    guardar_clau(clau)
    
    return clau


def xifrar_text(text, clau):  
    f = Fernet(clau) # Creamos el objeto Fernet con la clave

    # Convertimos el texto a bytes y lo ciframos
    return f.encrypt(text.encode())


def desxifrar_text(token, clau):
    # Creamos el objeto Fernet con la clave
    f = Fernet(clau)

    # Desciframos el texto y lo devolvemos como string
    return f.decrypt(token).decode()
