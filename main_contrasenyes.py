from generar_contrasenya import generar_contrasenya
from guardar_contrasenya import guardar_contrasenya, llistar_contrasenya, veure_contrasenya, carregar_contrasenya
from detectar_contrasenya import es_contrasenya_feble

# Función principal del programa
def main():
    print("\n🔐 ---- GESTOR DE CONTRASENYES (KEYPASS) ----\n")  # Título

    while True:  # Bucle principal, se repite hasta que el usuario salga
        print("¿Qué vols fer?")
        print("1. Generar nova contrasenya")
        print("2. Veure totes les contrasenyes")
        print("3. Buscar contrasenya d'un servei")
        print("4. Sortir")

        # Leemos opción del usuario
        opcio = input("Tria una opció (1-4): ").strip()


        if opcio == "1":
            try:
                # Pedimos longitud, si no pone nada usamos 12 por defecto
                longitud = int(input("Longitud de la contrasenya (mín 8): ") or "12")

                # Cargamos todas las contraseñas existentes
                contrasenyes_existents = [item['contrasenya'] for item in carregar_contrasenya()]
                
                # Generamos una contraseña aleatoria
                pwd = generar_contrasenya(longitud)

                # Comprobamos si es débil o repetida
                if es_contrasenya_feble(pwd, contrasenyes_existents):
                    print("⚠️ Contrasenya feble o repetida, regenerant...")
                    pwd = generar_contrasenya(longitud)  # regeneramos si es débil

                print(f"✅ Contrasenya generada: {pwd}")

                # Pedimos el servicio y el usuario
                servei = input("Per quin servei es la contrasenya? (EX: Gmail): ").strip()
                usuari = input("Quin es el nom d'usuari? (correu electronic): ").strip()

                # Guardamos la contraseña en el archivo
                guardar_contrasenya(servei, usuari, pwd)
            except ValueError:
                print("❌ Longitud ha de ser un número")  # Control de errores si no pone número


        elif opcio == "2":
            llistar_contrasenya()  # Muestra servicio y usuario


        elif opcio == "3":
            servei = input("\nQuin servei vols cercar?: ").strip()
            veure_contrasenya(servei)  # Muestra servicio, usuario y contraseña


        elif opcio == "4":
            print("👋 Adeu!")
            break  # Sale del bucle y termina el programa


        else:
            print("❌ Opció no vàlida.")

# Solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    main()
