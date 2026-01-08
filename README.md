# KeyPass‑ENTI

## Català

### Descripció del projecte

**KeyPass‑ENTI** és un gestor de contrasenyes desenvolupat en **Python** com a projecte acadèmic, amb l’objectiu d’aplicar conceptes reals de **ciberseguretat**, **xifratge** i **gestió segura de credencials**. El projecte combina bones pràctiques professionals amb un enfocament didàctic propi d’un entorn d’estudiant.

L’aplicació permet registrar usuaris, generar contrasenyes segures, emmagatzemar-les de forma xifrada, verificar-ne la integritat i reforçar l’accés mitjançant **autenticació de doble factor (2FA)**.

### Objectius

* Aplicar xifratge híbrid per a la protecció de dades sensibles
* Garantir la integritat de les contrasenyes mitjançant HMAC
* Implementar autenticació amb 2FA
* Desenvolupar un gestor funcional amb estructura modular
* Simular el funcionament d’un producte real orientat a seguretat

### Funcionalitats principals

* Gestió d’usuaris (registre i autenticació)
* Generador de contrasenyes segures personalitzables
* Detecció de fortalesa de contrasenyes
* Emmagatzematge xifrat de credencials
* Xifratge híbrid (simètric + asimètric)
* Verificació d’integritat amb HMAC
* Autenticació de doble factor (2FA)

### Estructura del projecte

```
KeyPass-ENTI/
├── main_contrasenyes.py
├── registrar_usuario.py
├── gestio_usuaris.py
├── guardar_contrasenya.py
├── generar_contrasenya.py
├── detectar_contrasenya.py
├── auth_2fa.py
├── xifrat_hibrid.py
├── hmac_integritat.py
├── users.json
├── requirements.txt
└── README.md
```

### Tecnologies utilitzades

* Python 3
* Criptografia (xifratge híbrid)
* HMAC per a integritat
* Arxius JSON per a persistència de dades

### Execució del projecte

1. Instal·lar dependències:

```
pip install -r requirements.txt
```

2. Executar l’aplicació:

```
python main_contrasenyes.py
```

### Limitacions

* Projecte educatiu (no apte per a ús productiu)
* Gestió local de dades
* Interfície per consola

### Aprenentatges clau

Aquest projecte ha permès entendre de forma pràctica com es protegeixen credencials, com s’estructura una aplicació de seguretat i quins són els reptes reals en el desenvolupament de software segur.

---

## English

### Project Description

**KeyPass‑ENTI** is a password manager developed in **Python** as an academic project, designed to apply real‑world concepts of **cybersecurity**, **encryption**, and **secure credential management**. The project blends professional practices with a student‑level educational approach.

The application allows user registration, secure password generation, encrypted storage of credentials, integrity verification, and access protection through **two‑factor authentication (2FA)**.

### Objectives

* Apply hybrid encryption for sensitive data protection
* Ensure password integrity using HMAC
* Implement two‑factor authentication (2FA)
* Develop a modular and functional password manager
* Simulate a real‑world security‑oriented product

### Main Features

* User management (registration and authentication)
* Secure and customizable password generator
* Password strength detection
* Encrypted credential storage
* Hybrid encryption (symmetric + asymmetric)
* Integrity verification using HMAC
* Two‑factor authentication (2FA)

### Project Structure

```
KeyPass-ENTI/
├── main_contrasenyes.py
├── registrar_usuario.py
├── gestio_usuaris.py
├── guardar_contrasenya.py
├── generar_contrasenya.py
├── detectar_contrasenya.py
├── auth_2fa.py
├── xifrat_hibrid.py
├── hmac_integritat.py
├── users.json
├── requirements.txt
└── README.md
```

### Technologies Used

* Python 3
* Cryptography (hybrid encryption)
* HMAC for integrity verification
* JSON files for data persistence

### How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python main_contrasenyes.py
```

### Limitations

* Educational project (not production‑ready)
* Local data storage
* Console‑based interface

### Key Learnings

This project provides hands‑on experience with credential protection, secure software architecture, and the real challenges involved in building cybersecurity‑focused applications.

---

**Project developed as part of a cybersecurity academic course at ENTI‑UB.**
