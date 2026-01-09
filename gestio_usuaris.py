import json
import hashlib
import os

# Nom del fitxer on es guarden els usuaris
USERS_DB = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funció per carregar els usuaris des del fitxer JSON
def cargar_usuarios():
    if not os.path.exists(USERS_DB):
        return {}
        # Si el fitxer no existeix, es retorna un diccionari buit

    try:
        # S'obre el fitxer i es carrega el contingut JSON
        with open(USERS_DB, "r") as f:
            return json.load(f)
    except:
        return {} # Si hi ha algun error de lectura o format, es retorna un diccionari buit

# Funció per guardar els usuaris actualitzats al fitxer JSON
def guardar_usuarios(usuarios):
    with open(USERS_DB, "w") as f:
        json.dump(usuarios, f, indent=2)

#Registre d'usuaris nous
def registrar_usuario(email, password):
    usuarios = cargar_usuarios()

    if email in usuarios:
        print("Error: El usuario ya existe")
        return False

    # Crear hash únic per al nom de l'arxiu de l'usuari
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
        return False     # Es comprova si l'email existeix a la base de dades


    password_hash = hash_password(password)
    return usuarios[email]["password_hash"] == password_hash
    # Es compara amb el hash guardat


def get_user_id(email):
    usuarios = cargar_usuarios()
    if email in usuarios:
        return usuarios[email].get("user_id")
    return None
