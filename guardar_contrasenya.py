import json
import os  # Usamos os en lugar de Path
from xifrat_hibrid import carregar_clau, xifrar_text, desxifrar_text
from hmac_integritat import generar_hmac, verificar_hmac

# Nombre del archivo donde guardamos las contraseñas cifradas
PASSWORDS_DB = "PasswordsBBDD.bin"  

# Nombre del archivo donde guardamos el HMAC
HMAC_DB = "PasswordsBBDD.hmac"

# Cargamos la clave Fernet (la crea si no existe)
CLAU_FERNET = carregar_clau()


def carregar_contrasenya() -> list:
    # Si el archivo no existe, devolvemos lista vacía
    if not os.path.exists(PASSWORDS_DB):
        return []

    try:
        # Leemos el archivo cifrado en modo binario
        with open(PASSWORDS_DB, "rb") as f:
            dades_cifrades = f.read()

        # Si existe HMAC, lo comprobamos
        if os.path.exists(HMAC_DB):
            with open(HMAC_DB, "r") as f:
                hmac_guardat = f.read().strip()
            if not verificar_hmac(dades_cifrades, hmac_guardat):
                print("⚠️ Archivo corrupto o modificado")
                return []

        # Desciframos las contraseñas con Fernet
        dades_json = desxifrar_text(dades_cifrades, CLAU_FERNET)
        # Convertimos de JSON a lista de diccionarios
        return json.loads(dades_json)

    except:
        print("❌ Error carregant")
        return []


def guardar_contrasenya(servei: str, usuari: str, contrasenya: str) -> None:
    try:
        # Cargamos las contraseñas existentes
        dades = carregar_contrasenya()
        # Añadimos la nueva
        dades.append({"servei": servei, "usuari": usuari, "contrasenya": contrasenya})

        # Convertimos a JSON
        dades_json = json.dumps(dades, indent=2, ensure_ascii=False)
        # Ciframos con Fernet
        dades_cifrades = xifrar_text(dades_json, CLAU_FERNET)

        # Guardamos el archivo cifrado
        with open(PASSWORDS_DB, "wb") as f:
            f.write(dades_cifrades)

        # Generamos HMAC para verificar integridad
        hmac_text = generar_hmac(dades_cifrades)
        with open(HMAC_DB, "w") as f:
            f.write(hmac_text)

        print(f"✅ Guardat: {servei}")

    except Exception as e:
        print(f"❌ Error: {e}")

def llistar_contrasenya() -> None:
    dades = carregar_contrasenya()
    if not dades:
        print("No hi han contrasenyes")
        return

    print("---- Contrasenyes ----")
    for i, d in enumerate(dades, 1):
        print(f"{i}. {d['servei']} - {d['usuari']}")


def veure_contrasenya(servei: str) -> None:
    dades = carregar_contrasenya()
    for d in dades:
        if d["servei"].lower() == servei.lower():
            print(f"Servei: {d['servei']}")
            print(f"Usuari: {d['usuari']}")
            print(f"Password: {d['contrasenya']}")
            return
    print(f"No trobat: {servei}")
