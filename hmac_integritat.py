import hmac        # Librería para crear firmas seguras
import hashlib     # Librería para usar algoritmos hash

# Clave secreta que SOLO conoce el programa
# Se usa para firmar los datos
CLAU_SECRETA = b"clau-super-secreta-keypass-2024"   


def generar_hmac(dades):

    # Creamos la firma usando:
    # - la clave secreta
    # - los datos
    # - el algoritmo SHA-256
    firma = hmac.new(CLAU_SECRETA, dades, hashlib.sha256)

    # Convertimos la firma a texto para poder guardarla
    return firma.hexdigest()


def verificar_hmac(dades, hmac_guardat):
    # Volvemos a crear la firma con los datos actuales
    hmac_actual = generar_hmac(dades)

    # Comparamos la firma nueva con la firma guardada
    # Si son iguales ? los datos NO han cambiado
    if hmac_actual == hmac_guardat:
        return True
    else:
        return False
