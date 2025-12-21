from generar_contrasenya import generar_contrasenya
from guardar_contrasenya import guardar_contrasenya, llistar_contrasenya, veure_contrasenya


def main():
    print()
    print("---- GESTOR DE CONTRASENYES (KEYPASS) ----")
    print()
    
    while True:
        print("¿Qué vols fer?")
        print("1. Generar nova contrasenya")
        print("2. Veure totes les contrasenyes")
        print("3. Buscar contrasenya d'un servei")
        print("4. Sortir")
        
        opcio = input("Tria una opció (1-4): ").strip()
        
        if opcio == "1":
            longitud = 12
            pwd = generar_contrasenya(longitud)
            print(f"Contrasenya generada: {pwd}")
            
            servei = input("Per quin servei es la contrasenya? EX: Gmail ").strip()
            usuari = input("Quin es el nom d'usuari? (correu electronic)").strip()
            
            guardar_contrasenya(servei, usuari, pwd)
        
        elif opcio == "2":
            llistar_contrasenya()
        
        elif opcio == "3":
            servei = input("\nQuin servei vols cercar?: ").strip()
            veure_contrasenya(servei)
        
        elif opcio == "4":
            print("adeu tontito")
            break
        
        else:
            print("Opció no vàlida.")


if __name__ == "__main__":
    main()
