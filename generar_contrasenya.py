import string
import random

def generar_contrasenya(longitud):  
    if longitud < 8:             # Si la contrasenya té menys de 8 caracters, dona error
        raise ValueError("La longitud minima es 8 carcters.")

    lletres_majus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"        # Caracters possibles per a la contrasenya
    lletres_minus = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    simbols = "!@#$%^&*()-_=+[]{};:,.?/"
    
    # S'escolleixen primer 1 de cada una de las 4 llistes per a que hi hagi almenys 1 caracter diferent
    contrasenya = [random.choice(lletres_majus),random.choice(lletres_minus),random.choice(nums),random.choice(simbols)]
    
    # Se sumen tots els caràcters quedant ABCD....abc....012....
    total = lletres_majus + lletres_minus + nums + simbols
    
    # Es van escollint valors aleatoris de la llista total fins a arribar a la longitud desitjada
    while len(contrasenya) < longitud:
        contrasenya.append(random.choice(total))
    
    # Es barregen els caràcters per a que no segueixin un patró concret
    random.shuffle(contrasenya)
    return "".join(contrasenya)
    print(contrasenya)


