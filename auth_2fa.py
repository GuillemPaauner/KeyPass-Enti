import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from gestio_usuaris import verificar_login, get_user_id

def generar_codi_otp():
    return str(random.randint(100000, 999999))

def enviar_codi_email(destinatari, codi_otp, remitent_email, remitent_password):
    # crear missatge otp
    missatge = MIMEMultipart()
    missatge["From"] = remitent_email
    missatge["To"] = destinatari
    missatge["Subject"] = "KEYPASS-ENTI - Codi de Verificació"

    body = f"""
Hola,

El teu codi de verificació per a KeyPass-ENTI és: {codi_otp}

Aquest codi expirarà en 5 minuts.

Salutacions,
Equip KeyPass-ENTI
"""
    missatge.attach(MIMEText(body, "plain"))

    # enviar email amb gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remitent_email, remitent_password)
        servidor.sendmail(remitent_email, destinatari, missatge.as_string())

    return True
    

def autenticacio_2fa():
    print("\n ---- Autenticació de Doble Factor ---- \n")

    # login (email + contrasenya)
    print("\n--- 1.CREDENCIALS ---\n")

    email = None
    while True:
        email = input("Email: ").strip().lower()
        contrasenya = input("Contrasenya: ").strip()

        if verificar_login(email, contrasenya):
            print(f"\n Credencials vàlides.\n")
            break
        else:
            print("Credencials incorrectes. Torna-ho a intentar.\n")

    # enviar codi OTP al correu
    print("--- 2.VERIFICACIÓ 2FA ---\n")
    print(f"Enviant codi de verificació a {email}...")

    codi_otp = generar_codi_otp()

    remitent_email = "keypassenti@gmail.com"  
    remitent_password = "ywcydopsydlnbspq"  

    # enviar codi
    if not enviar_codi_email(email, codi_otp, remitent_email, remitent_password):
        print("\nError enviant el codi de verificació. Intenta-ho més tard.")
        return None, None

    print("\n Codi enviat! \n")

    # verificar codi OTP
    while True:
        codi_introduit = input("Introdueix el codi de 6 dígits: ").strip()

        if codi_introduit == codi_otp:
            print("Autenticació amb éxit! Accés concedit.")

            # Carregar user_id
            from gestio_usuaris import get_user_id
            return email, get_user_id(email)
        else:
            print("Codi incorrecte. Torna-ho a intentar.\n")

    


