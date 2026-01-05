from cryptography.fernet import Fernet
import os   # Usamos os en lugar de Path


# Nombre del archivo donde se guarda la clave
CLAU_FILE = "clau_fernet.key"


def guardar_clau(clau: bytes):
    # Abrimos el archivo en modo escritura binaria
    with open(CLAU_FILE, "wb") as f:
        # Escribimos la clave en el archivo
        f.write(clau)


def carregar_clau() -> bytes:
    # Comprobamos si el archivo de la clave existe
    if os.path.exists(CLAU_FILE):
        # Si existe, abrimos el archivo y leemos la clave
        with open(CLAU_FILE, "rb") as f:
            return f.read()

    # Si no existe, generamos una clave nueva
    clau = Fernet.generate_key()

    # Guardamos la nueva clave
    guardar_clau(clau)

    # Devolvemos la clave
    return clau


def xifrar_text(text: str, clau: bytes) -> bytes:
    # Creamos el objeto Fernet con la clave
    f = Fernet(clau)

    # Convertimos el texto a bytes y lo ciframos
    return f.encrypt(text.encode())


def desxifrar_text(token: bytes, clau: bytes) -> str:
    # Creamos el objeto Fernet con la clave
    f = Fernet(clau)

    # Desciframos el texto y lo devolvemos como string
    return f.decrypt(token).decode()
