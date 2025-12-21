
import string
import random
import json
from pathlib import Path

def generar_contrasenya(longitud: int = 12) -> str:
    """
    Genera una contrasenya random que compleix:
    - Minim 8 caracters
    - Minim 1 lletra majuscula
    - Minim 1 lletra minuscula
    - Minim 1 digit
    - Minim 1 simbol especial
    """
    if longitud < 8:
        raise ValueError("La longitud minima es 8 carcters.")

    lletres_majus = string.ascii_uppercase
    lletres_minus = string.ascii_lowercase
    digits = string.digits
    simbols = "!@#$%^&*()-_=+[]{};:,.?/"
    
    
    # Assegurem els requisits minims
    contrasenya = [
        random.choice(lletres_majus),
        random.choice(lletres_minus),
        random.choice(digits),
        random.choice(simbols),
    ]
    
    # Llista de tots els caracters per omplir la resta
    tots_caracters = lletres_majus + lletres_minus + digits + simbols
    
    while len(contrasenya) < longitud:
        contrasenya.append(random.choice(tots_caracters))
        
  
    contrasenya_final = "".join(contrasenya)
    return print(contrasenya_final)
        
    

generar_contrasenya()