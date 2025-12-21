
import json
from pathlib import Path

PASSWORDS_DB = "PasswordsBBDD.txt"


def carregar_contrasenya() -> list:
    "Carrega les contrasenyes del arxiu"
    if Path(PASSWORDS_DB).exists():
        with open (PASSWORDS_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    return[]



def guardar_contrasenya(servei:str, usuari:str, contrasenya:str) -> None:
    "Guardar una contrasenya en l'arxiu"
    dades = carregar_contrasenya()
    
    dades.append({"servei": servei,
                  "usuari": usuari,
                  "contrasenya": contrasenya
                  })
    
    with open(PASSWORDS_DB, "w", encoding="utf-8") as f:
        json.dump(dades, f, indent=2, ensure_ascii=False)
    
    print(f"Contrasenya guardada para servei {servei}")
    
    
def llistar_contrasenya() ->None:
    "Mostra les contrasenyes guardades"
    dades=carregar_contrasenya()
    
    if not dades:
        print("No hi han contrasenyes guardades")
        return
    
    
    print("---- Contrasenya guardades ----")
    for index, dada in enumerate(dades, 1):
        print(f"{index}. Servei: {dada['servei']}, Usuari: {dada['usuari']}")
    print()


def veure_contrasenya(servei: str) -> None:
    "Mostra contrasenya de servei especific"
    dades = carregar_contrasenya()

    for dada in dades:
        if dada["servei"].lower() == servei.lower():
            print(f"Servei: {dada['servei']}")
            print(f"Usuari: {dada['usuari']}")
            print(f"Contrasenya: {dada['contrasenya']}\n")
            return
    
    print(f"No s'ha trobat cap contrasenya per al servei '{servei}'.")