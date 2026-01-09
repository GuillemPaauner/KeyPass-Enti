from generar_contrasenya import generar_contrasenya
from guardar_contrasenya import configurar_usuario, guardar_contrasenya, llistar_contrasenya, veure_contrasenya, carregar_contrasenya
from detectar_contrasenya import es_contrasenya_feble
from auth_2fa import autenticacio_2fa

def main():
    # Inicia el sistema de login amb 2FA i retorna l'usuari actual i el seu user_id
    usuario_actual, user_id = autenticacio_2fa()

    # Si el login o el 2FA fallen, es tanca el programa
    if not usuario_actual or not user_id:
        print("\nAccés denegat. Adeu...")
        return

    # Configura els arxius específics associats a aquest usuari (segons el seu user_id)
    configurar_usuario(user_id)

    print("\n ---- GESTOR DE CONTRASENYES (KEYPASS) ----\n")
    
    
    # Bucle principal del menú
    while True:
        print("¿Qué vols fer?")
        print("1. Generar nova contrasenya")
        print("2. Veure totes les contrasenyes")
        print("3. Buscar contrasenya d'un servei")
        print("4. Sortir")

        # Llegeix l'opció del menú triada per l'usuari
        opcio = input("Tria una opció (1-4): ")

        if opcio == "1":
            try:
                longitud = int(input("Longitud de la contrasenya (mín 8): ") or "12")
                # Demana la longitud de la contrasenya (per defecte 12 si l'usuari prem Enter)

                contrasenyes_existents = []
                for item in carregar_contrasenya():
                    contrasenyes_existents.append(item['contrasenya'])

                contrasenya_aleatoria = generar_contrasenya(longitud)  # Genera una contrasenya aleatòria amb la longitud indicada

                # Comprova si la contrasenya és feble o repetida i, si cal, la regenera
                if es_contrasenya_feble(contrasenya_aleatoria, contrasenyes_existents):
                    print("Contrasenya feble o repetida, regenerant...")
                    contrasenya_aleatoria = generar_contrasenya(longitud)

                print(f"Contrasenya generada: {contrasenya_aleatoria}") # Mostra la contrasenya generada a l'usuari
                
                # Demana informació del servei i usuari associats a la contrasenya
                servei = input("Per quin servei es la contrasenya? (EX: Gmail): ")
                usuari = input("Quin es el nom d'usuari? (correu electronic): ")

                guardar_contrasenya(servei, usuari, contrasenya_aleatoria)

            except ValueError:
                print("Longitud ha de ser un número") # Controla que la longitud sigui un número vàlid

        elif opcio == "2":
            llistar_contrasenya()

        elif opcio == "3":
            servei = input("\nQuin servei vols cercar?: ")
            veure_contrasenya(servei)

        elif opcio == "4":
            print("Adeu!")
            break

        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    main()
