import string
import random

def generar_contrasenya(longitud):  
    if longitud < 8:             # Si la contrasenya tiene menos de 8 caracteres entonces da error
        raise ValueError("La longitud minima es 8 carcters.")

    lletres_majus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"        # Caracteres possibles para la contrasenya
    lletres_minus = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    simbols = "!@#$%^&*()-_=+[]{};:,.?/"
    
    # Se elijen primero 1 de cada una de las 4 listas para que haya almenos 1 caracter diferente
    contrasenya = [random.choice(lletres_majus),random.choice(lletres_minus),random.choice(nums),random.choice(simbols)]
    
    # Se suman todas los caracterses quedando ABCD....abc....012....
    total = lletres_majus + lletres_minus + nums + simbols
    
    # Se van eligiendo randoms de la lista total hasta ser igual a la longitud elegida
    while len(contrasenya) < longitud:
        contrasenya.append(random.choice(total))
    
    # Se mezcla todo para evitar que haya possibles patrones
    random.shuffle(contrasenya)
    return "".join(contrasenya)
    print(contrasenya)


