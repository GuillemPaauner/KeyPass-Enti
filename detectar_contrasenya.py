import re

def es_contrasenya_feble(contrasenya, llista_existents):

    if len(contrasenya) < 8:       #Mira la longitud de la contrasenya
        return True
    
    if contrasenya in llista_existents:    #Si existe devuelve true
        return True

    patrones = [r"[A-Z]",r"[a-z]",r"[0-9]",r"[!@#$%^&*()\-_=+\[\]{};:,.?/]"]  #Se utiliza rejex para ver patrones como abc, letras o caracteres, i la r" para que reconozca /n
    
    # Mira los patrones que tiene que seguir para ver si es una contrasena fuerta, comprarando el aptron con la contra, en el caso que no sea devulve True, que la contrasena es debil
    for patro in patrones:
        if not re.search(patro, contrasenya):
            return True

    return False
