
def Crear_menu():
    ancho = 31

    menu = [
        ""
        "ENTI-KEYPASS:",
        "-------------------------------",
        "1. Crear nueva contrasena\n",
        "2. Buscar contrasenas\n",
        "3. Editar contrasenas\n",
        "4. Salir\n"
]

    for linea in menu:
        if linea[0] == "-":
            print(linea)
        else:
            print("        " + linea)
            
Crear_menu()
