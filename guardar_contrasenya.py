
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
    