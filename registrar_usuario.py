from gestio_usuaris import registrar_usuario

email = input("Email del nuevo usuario: ").strip().lower()
password = input("Contrasenya: ").strip()
registrar_usuario(email, password)  
