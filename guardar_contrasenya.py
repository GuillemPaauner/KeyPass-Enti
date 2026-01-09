import json
import os
from xifrat_hibrid import carregar_clau, xifrar_text, desxifrar_text
from hmac_integritat import generar_hmac, verificar_hmac

# Arxius de dades per a cada usuari
PASSWORDS_DB = None
HMAC_DB = None
CLAU_FERNET = carregar_clau() # Clau utilitzada per xifrar i desxifrar les contrasenyes



def configurar_usuario(user_id): #Defineix els noms dels arxius segons l'usuari
    global PASSWORDS_DB, HMAC_DB
    PASSWORDS_DB = f"passwords_{user_id}.bin"
    HMAC_DB = f"passwords_{user_id}.hmac"



def carregar_contrasenya(): # Aquesta part s'encarrega de llegir i desxifrar les contrasenyes dels usuaris
    if not PASSWORDS_DB or not os.path.exists(PASSWORDS_DB):
        return []

    try:
        # Llegeix l'arxiu xifrat
        with open(PASSWORDS_DB, "rb") as f:
            dades_cifrades = f.read()

        # Comprovar integritat con HMAC
        if os.path.exists(HMAC_DB):
            with open(HMAC_DB, "r") as f:
                hmac_guardat = f.read().strip()

            if not verificar_hmac(dades_cifrades, hmac_guardat):
                print("Archiu modificat o corrupte")
                return []

        # Desxifrar y convertir a JSON
        dades_json = desxifrar_text(dades_cifrades, CLAU_FERNET)
        return json.loads(dades_json)

    except Exception as e:
        print("Error carregant contrasenyes:", e)
        return []


def guardar_contrasenya(servei, usuari, contrasenya):
    # Afegir una nova contrasenya
    if not PASSWORDS_DB:
        print("Usuario no configurat")
        return

    try:
        dades = carregar_contrasenya()

        # Es guarda tot en un diccionari
        dades.append({
            "servei": servei,
            "usuari": usuari,
            "contrasenya": contrasenya
        })

        # Xifrar diccionari i guardar-lo
        dades_json = json.dumps(dades, ensure_ascii=False)
        dades_cifrades = xifrar_text(dades_json, CLAU_FERNET)

        with open(PASSWORDS_DB, "wb") as f:
            f.write(dades_cifrades)

        # Generar HMAC par a detectar canvis
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
    dades = carregar_contrasenya() # Mostra els serveis de un en concret

    for d in dades:
        if d["servei"].lower() == servei.lower():
            print(f"\nServicio: {d['servei']}")
            print(f"Usuario: {d['usuari']}")
            print(f"Contraseña: {d['contrasenya']}")
            return

    print("Servei no trobat")
