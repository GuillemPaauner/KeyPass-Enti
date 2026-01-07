import hmac        # Librería para crear firmas seguras
import hashlib     # Librería para usar algoritmos hash

# Clave secreta que solo conoce el programa, la cual se usa para firmar los datos
CLAU_SECRETA = b"Clau_Secreta_Keypass"   


def generar_hmac(dades):

    # Creamos la firma usando la clave secreta, los datos y el algoritmo SHA-256
    firma = hmac.new(CLAU_SECRETA, dades, hashlib.sha256)

    # Convertimos la firma a texto hexadecimal para poder guardarla
    return firma.hexdigest()


def verificar_hmac(dades, hmac_guardat):

    # Volvemos a crear la firma con los datos actuales
    hmac_actual = generar_hmac(dades)

    # Comparamos la firma nueva con la firma guardada, y si son iguales devuleve true sino es que ha sido cambiada y devuelve false
    if hmac_actual == hmac_guardat:
        return True
    else:
        return False
