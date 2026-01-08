import json
import os
from xifrat_hibrid import carregar_clau, xifrar_text, desxifrar_text
from hmac_integritat import generar_hmac, verificar_hmac

# Archivos del usuario actual 
PASSWORDS_DB = None
HMAC_DB = None
CLAU_FERNET = carregar_clau() # Clave utilizada para el cifrado 



def configurar_usuario(user_id): #Define los archivos segun el usuario
    global PASSWORDS_DB, HMAC_DB
    PASSWORDS_DB = f"passwords_{user_id}.bin"
    HMAC_DB = f"passwords_{user_id}.hmac"



def carregar_contrasenya(): # Esta parte se encarga de leer y descifrar las contraseñas de los usuarios
    if not PASSWORDS_DB or not os.path.exists(PASSWORDS_DB):
        return []

    try:
        # Lee el archivo cifrado
        with open(PASSWORDS_DB, "rb") as f:
            dades_cifrades = f.read()

        # Comprobar integridad con HMAC
        if os.path.exists(HMAC_DB):
            with open(HMAC_DB, "r") as f:
                hmac_guardat = f.read().strip()

            if not verificar_hmac(dades_cifrades, hmac_guardat):
                print("Archivo modificado o corrupto")
                return []

        # Descifrar y convertir a JSON
        dades_json = desxifrar_text(dades_cifrades, CLAU_FERNET)
        return json.loads(dades_json)

    except Exception as e:
        print("Error cargando contraseñas:", e)
        return []


def guardar_contrasenya(servei, usuari, contrasenya):
    # Añade una nueva contraseña
    if not PASSWORDS_DB:
        print("Usuario no configurado")
        return

    try:
        dades = carregar_contrasenya()

        # Guardamos todo en una lista de diccionarios
        dades.append({
            "servei": servei,
            "usuari": usuari,
            "contrasenya": contrasenya
        })

        # Cifrar datos
        dades_json = json.dumps(dades, ensure_ascii=False)
        dades_cifrades = xifrar_text(dades_json, CLAU_FERNET)

        with open(PASSWORDS_DB, "wb") as f:
            f.write(dades_cifrades)

        # Generar HMAC para detectar cambios
        with open(HMAC_DB, "w") as f:
            f.write(generar_hmac(dades_cifrades))

        print(f"Contraseña guardada: {servei}")

    except Exception as e:
        print("Error guardando contraseña:", e)


def llistar_contrasenya():
    dades = carregar_contrasenya()

    if not dades:
        print("No hay contraseñas")
        return

    print("\n--- Servicios guardados ---")
    for i, d in enumerate(dades, 1):
        print(f"{i}. {d['servei']} ({d['usuari']})")


def veure_contrasenya(servei):
    dades = carregar_contrasenya() # Muestra los servicios de uno en concreto

    for d in dades:
        if d["servei"].lower() == servei.lower():
            print(f"\nServicio: {d['servei']}")
            print(f"Usuario: {d['usuari']}")
            print(f"Contraseña: {d['contrasenya']}")
            return

    print("Servicio no encontrado")
