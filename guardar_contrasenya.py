import json
import os
from xifrat_hibrid import carregar_clau, xifrar_text, desxifrar_text
from hmac_integritat import generar_hmac, verificar_hmac

# Creamos los archivos donde se guardan las contrasenyas y la firma 
PASSWORDS_DB = "PasswordsBBDD.bin"
HMAC_DB = "PasswordsBBDD.hmac"

# Cargamos la clave de Fernet
CLAU_FERNET = carregar_clau()

# Función para cargar contraseñas
def carregar_contrasenya():
    if not os.path.exists(PASSWORDS_DB):
        return []

    try:
        with open(PASSWORDS_DB, "rb") as f:
            dades_cifrades = f.read()

        if os.path.exists(HMAC_DB):
            with open(HMAC_DB, "r") as f:
                hmac_guardat = f.read().strip()
            if not verificar_hmac(dades_cifrades, hmac_guardat):
                print("Archivo corrupto o modificado")
                return []

        dades_json = desxifrar_text(dades_cifrades, CLAU_FERNET)
        return json.loads(dades_json)

    except:
        print("Error cargando contraseñas")
        return []

# Función para guardar una nueva contraseña
def guardar_contrasenya(servei, usuari, contrasenya):
    try:
        dades = carregar_contrasenya()
        dades.append({"servei": servei, "usuari": usuari, "contrasenya": contrasenya})

        dades_json = json.dumps(dades, indent=2, ensure_ascii=False)
        dades_cifrades = xifrar_text(dades_json, CLAU_FERNET)

        with open(PASSWORDS_DB, "wb") as f:
            f.write(dades_cifrades)

        hmac_text = generar_hmac(dades_cifrades)
        with open(HMAC_DB, "w") as f:
            f.write(hmac_text)

        print(f"Guardado: {servei}")

    except Exception as e:
        print(f"Error: {e}")

# Función para listar todas las contraseñas
def llistar_contrasenya():
    dades = carregar_contrasenya()
    if not dades:
        print("No hay contraseñas")
        return

    print("---- Contraseñas ----")
    for i, d in enumerate(dades, 1):
        print(f"{i}. {d['servei']} - {d['usuari']}")


# Función para ver la contraseña de un servicio
def veure_contrasenya(servei):
    dades = carregar_contrasenya()
    for d in dades:
        if d["servei"].lower() == servei.lower():
            print(f"Servei: {d['servei']}")
            print(f"Usuari: {d['usuari']}")
            print(f"Password: {d['contrasenya']}")
            return
    print(f"No encontrado: {servei}")
