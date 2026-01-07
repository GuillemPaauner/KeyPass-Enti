# Importacio de funcions
from generar_contrasenya import generar_contrasenya
from guardar_contrasenya import guardar_contrasenya, llistar_contrasenya, veure_contrasenya, carregar_contrasenya
from detectar_contrasenya import es_contrasenya_feble

# Funcion principal del programa
def main():
    print("\n ---- GESTOR DE CONTRASENYES (KEYPASS) ----\n")

    while True:  # Bucle que se repite hasta que el usuario salga
        print("¿Qué vols fer?")
        print("1. Generar nova contrasenya")
        print("2. Veure totes les contrasenyes")
        print("3. Buscar contrasenya d'un servei")
        print("4. Sortir")

        # Leemos opción del usuario
        opcio = input("Tria una opció (1-4): ")


        if opcio == "1":
            try:
                # Pedimos la longitud de la contrasenya, la cual si no pone nada sera 12 por defecto
                longitud = int(input("Longitud de la contrasenya (mín 8): ") or "12")

                # Cargamos todas las contraseñas que se han usado
                contrasenyes_existents = []
                for item in carregar_contrasenya():
                    contrasenyes_existents.append(item['contrasenya'])
                
                # Generamos una contraseña aleatoria
                contrasenya_aleatoria = generar_contrasenya(longitud)

                # Comprobamos si es débil o repetida
                if es_contrasenya_feble(contrasenya_aleatoria, contrasenyes_existents):
                    print("Contrasenya feble o repetida, regenerant...")
                    contrasenya_aleatoria = generar_contrasenya(longitud)  # Regeneramos si es débil

                print(f"Contrasenya generada: {contrasenya_aleatoria}")

                # Pedimos el servicio y el usuario
                servei = input("Per quin servei es la contrasenya? (EX: Gmail): ")
                usuari = input("Quin es el nom d'usuari? (correu electronic): ")

                # Guardamos la contraseña en el archivo
                guardar_contrasenya(servei, usuari, contrasenya_aleatoria)
            except ValueError:
                 # Control de errores por si el ususario pone otra cosa que no sea un número
                print("Longitud ha de ser un número")  


        elif opcio == "2":
            llistar_contrasenya()  # Muestra todos los servicios y los diferentes usuarios


        elif opcio == "3":
            servei = input("\nQuin servei vols cercar?: ")
            veure_contrasenya(servei)  # Muestra servicio, usuario y contraseña


        elif opcio == "4":
            print("Adeu!")
            break  # Sale del bucle y termina el programa


        else:
            print("Opció no vàlida.")

main()
