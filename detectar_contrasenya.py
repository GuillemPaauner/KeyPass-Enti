import re

def es_contrasenya_feble(contrasenya, llista_existents):

    if len(contrasenya) < 8:       # Mira la longitud de la contrasenya
        return True
    
    if contrasenya in llista_existents:    #Si existeix retorna, true
        return True

    patrones = [r"[A-Z]",r"[a-z]",r"[0-9]",r"[!@#$%^&*()\-_=+\[\]{};:,.?/]"]  # S'utiliza rejex per veure patrons com abc, lletres o caracters, i la r" per a que reconegui /n
    
    # Mira els patrons que ha que seguir per veure si es una contrasena forta, comprarant el patró amb la contrasenya, en el cas que no ho sigui retorna True, que la contrasenya es debil.
    for patro in patrones:
        if not re.search(patro, contrasenya):
            return True

    return False

