from cryptography.fernet import Fernet
import os


# Nom de l'arxiu on es guarda la clau
CLAU_FILE = "clau_fernet.key"


def guardar_clau(clau):
    # Obrim el arxiu en mode escriptura binaria (s'utilitza per a guaradar claus)
    with open(CLAU_FILE, "wb") as f:
        # Escribim la clau a l'arxiu
        f.write(clau)


def carregar_clau():
    #Comprovem si l'arxiu de la clau existeix
    if os.path.exists(CLAU_FILE):
        # Si existeis, obrim l'arxiu i llegim la clau binària
        with open(CLAU_FILE, "rb") as f:
            return f.read()

    # Si no existeix, generem una clau nova
    clau = Fernet.generate_key()

    # Guardem la clau nova
    guardar_clau(clau)
    
    return clau


def xifrar_text(text, clau):  
    f = Fernet(clau) # Creem el objecto Fernet amb la clau

    # Convertim el text a bytes y el xifrem
    return f.encrypt(text.encode())


def desxifrar_text(token, clau):
    # Creem el objecte Fernet amb la clau
    f = Fernet(clau)

    # Desxifrem el text y el retornem com a string
    return f.decrypt(token).decode()
