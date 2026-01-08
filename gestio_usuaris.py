import json
import hashlib
import os

USERS_DB = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def cargar_usuarios():
    if not os.path.exists(USERS_DB):
        return {}
    try:
        with open(USERS_DB, "r") as f:
            return json.load(f)
    except:
        return {}

def guardar_usuarios(usuarios):
    with open(USERS_DB, "w") as f:
        json.dump(usuarios, f, indent=2)

def registrar_usuario(email, password):
    usuarios = cargar_usuarios()

    if email in usuarios:
        print("Error: El usuario ya existe")
        return False

    # Crear hash único para el nombre del archivo del usuario
    user_hash = hashlib.md5(email.encode()).hexdigest()[:12]

    usuarios[email] = {
        "password_hash": hash_password(password),
        "email": email,
        "user_id": user_hash  
    }

    guardar_usuarios(usuarios)
    print(f"Usuari {email} registrado correctamente")
    return True

def verificar_login(email, password):
    usuarios = cargar_usuarios()

    if email not in usuarios:
        return False

    password_hash = hash_password(password)
    return usuarios[email]["password_hash"] == password_hash

def get_user_id(email):
    usuarios = cargar_usuarios()
    if email in usuarios:
        return usuarios[email].get("user_id")
    return None
