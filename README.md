# KeyPass-Enti
Gestor de Contrasenyes: 

Resum: El nostre treball consisteix en un gestor de contrasenyes desenvolupat íntegrament en Python que permet emmagatzemar, gestionar i protegir credencials mitjançant xifratge robust i mecanismes d'autenticació reforçada. 
 
Descripcio detallada:

 El programa serà un gestor de contrasenyes que permetrà crear, guardar, editar i eliminar contrasenyes associades a diferents serveis (correu, xarxes socials, plataformes, etc.) de forma centralitzada i segura. 

La principal i més important funció serà la de emmagatzemar de manera encriptada totes les contrasenyes per mantenir-les de manera més segura. 


Les funcionalitats principals són:  

•	Generador de contrasenyes segures: Personalitzable per longitud, tipus de caràcters i nivell de complexitat. 

•	Autenticació de doble factor (2FA): Via correu electrònic o aplicació tipus authenticator per accedir al gestor. 

•	Validació de contrasenyes febles: Avís automàtic si una contrasenya és feble o es repeteix en diversos serveis. 

•	Comprovació d’integritat amb HMAC: El gestor calcularà un codi d’autenticació (HMAC) sobre les dades xifrades per detectar qualsevol manipulació o corrupció abans de desxifrar la informació, garantint la integritat de les credencials emmagatzemades.

•	Esquema de xifratge híbrid Simple: Les contrasenyes es protegiran amb un esquema híbrid que combina un algoritme simètric per xifrar les dades i un mecanisme derivat de la contrasenya mestra per protegir i gestionar les claus, millorant la confidencialitat i la gestió segura de claus al gestor.


Motivació: La motivació principal és el fet de millorar la seguretat de les credencials dels usuaris, evitant pràctiques insegures com reutilitzar contrasenyes o guardar-les en text pla. Aquest projecte permet aplicar coneixements de programació en Python i conceptes de ciberseguretat apresos durant el curs.

Usuari final: L'eina està pensada per a:
-	Usuaris que vulguin gestionar de forma segura les seves contrasenyes
-	Estudiants i treballadors que necessiten controlar múltiples credencials
-	Petits administradors de sistemes
-	Persones que vulguin entendre millor com funcionen els gestors de contrasenyes i les tècniques de protecció de dades

Limitacions: Algunes funcionalitats previstes, com la implementació correcta de 2FA o l'ús d'algorismes criptogràfics avançats, poden requerir l'estudi de llibreries i conceptes que el grup encara no ha treballat en profunditat.

prueva de cambio

esto es para ver si se hace update el jira
