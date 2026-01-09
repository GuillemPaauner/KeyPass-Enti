import hmac        # Llibrería per crear firmes segures
import hashlib     # Llibrería per usar algoritmes hash

# Clau secreta que només coneix el programa, la qual s'utiliztzar per firmar les dades
CLAU_SECRETA = b"Clau_Secreta_Keypass"   


def generar_hmac(dades):
    #Creem la frma utilitzant la clau secreta, les dades i l'algoritme SHA-256
    firma = hmac.new(CLAU_SECRETA, dades, hashlib.sha256)

    # Convertim la firma a text hexadecimal per a poder guardarla
    return firma.hexdigest()


def verificar_hmac(dades, hmac_guardat):

    # Tornem a crear la firma amb les dades actuals
    hmac_actual = generar_hmac(dades)

    # Comparem la firma nova amb la firma guardada, i si son iguals retorna true sino es que ha estat canviada i retorna false
    if hmac_actual == hmac_guardat:
        return True
    else:
        return False
