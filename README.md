
# KEYPASS-ENTI

Gestor de Contrasenyes – Alpha Release

KEYPASS-ENTI és un gestor de contrasenyes desenvolupat en Python amb finalitats educatives. Permet generar, emmagatzemar i consultar credencials de manera centralitzada mitjançant una interfície de línia de comandes.  
El projecte es troba actualment en fase Alpha, amb funcionalitats bàsiques implementades i una base preparada per a futures millores de seguretat.

---

## Estat del projecte

Versió Alpha.  
Aquesta versió inclou funcionalitats mínimes operatives. No es recomana el seu ús en entorns reals ni amb credencials sensibles.

---

## Funcionalitats implementades

- Generació de contrasenyes segures
- Emmagatzematge local de contrasenyes
- Llistat de serveis guardats
- Cerca de contrasenyes per servei
- Interfície per consola (CLI)

### Generador de contrasenyes
- Longitud configurable (mínim 8 caràcters)
- Inclou:
  - Lletres majúscules
  - Lletres minúscules
  - Dígits
  - Símbols especials
- Compleix requisits bàsics de seguretat

### Gestió de contrasenyes
- Emmagatzema credencials associades a:
  - Servei
  - Usuari
  - Contrasenya
- Persistència local mitjançant fitxer
- Consulta individual de contrasenyes per servei

---

## Funcionalitats previstes (no implementades en aquesta versió)

Les funcionalitats següents formen part del disseny del projecte, però no estan desenvolupades en la versió Alpha:

- Xifratge de les contrasenyes
- Autenticació mitjançant contrasenya mestra
- Autenticació de doble factor (2FA)
- Detecció de contrasenyes febles o repetides
- Verificació d’integritat amb HMAC
- Esquema de xifratge híbrid

Les llibreries necessàries per a aquestes funcionalitats ja estan definides al fitxer `requirements.txt`.

---

## Requisits

- Python 3.10 o superior
- Sistema operatiu compatible amb Python
- Els fitxers main.py, generar_contrasenya.py i guardar_contrasenya.py han d’estar a la mateixa carpeta.

### Dependències

En la versió ALPHA només fem servir llibreria estàndard de Python, o sigui, res d’instal·lar amb pip:
​
    - string: per obtenir lletres majúscules i minúscules.

    - random: per triar caràcters aleatoris de la contrasenya.
​

    - json: per guardar les contrasenyes en format JSON al fitxer.
​

    - pathlib.Path: per comprovar si el fitxer de base de dades existeix.
​

No hi ha cap requirements.txt perquè no hi ha paquets externs.

Instal·lació de dependències (preparades per a futures versions):

bash
pip install -r requirements.txt
