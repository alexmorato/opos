# 🧩 Taula comparativa ampliada: NIS2 · ENS · RGPD

## 1. Taula detallada de notificacions

| **Aspecte** | **NIS2** | **ENS (Espanya)** | **RGPD** |
|-------------|----------|-------------------|----------|
| **Tipus d’incident que activa la notificació** | Incident significatiu que afecti la disponibilitat, integritat, autenticitat o confidencialitat dels serveis essencials o importants. [es.isms.online] | Qualsevol incident de seguretat que afecti sistemes d’informació del sector públic o proveïdors. En molts casos segueix els criteris i llindars de NIS2. [easytelecomlaw.com], [es.scassi.com] | Violació de dades personals, accidental o il·lícita, que afecti la confidencialitat, integritat o disponibilitat de dades personals. [eiposgrados.com] |
| **Cal que hi hagi dades personals?** | ❌ No. L’objectiu és la continuïtat del servei i la ciberresiliència. | ❌ No. L’objectiu és la seguretat del sistema públic. | ✔️ Sí. Només aplica si hi ha dades personals. |
| **Qui ha d’avisar?** | Entitats essencials i importants segons la directiva (energia, salut, transport, serveis digitals, administració pública, etc.). [es.isms.online] | Administracions públiques i proveïdors que gestionen informació pública. [easytelecomlaw.com] | El responsable del tractament (o l’encarregat informa al responsable). |
| **A qui s’ha d’avisar?** | A l’autoritat competent NIS o CSIRT/Cert Nacional (a Espanya: INCIBE-CERT + autoritats sectorials). | Principalment al CCN‑CERT, que és l’autoritat ENS. [es.scassi.com] | A l’autoritat de protecció de dades (AEPD a Espanya). |
| **Temps de notificació (primer avís)** | 24 hores des que es detecta un incident significatiu. [es.isms.online] | S’alinea amb NIS2 per a entitats obligades. Normalment notificació immediata/prime 24 h segons gravetat. | 72 hores des que es té constància de la violació de dades personals. [eiposgrados.com] |
| **Tipus de notificacions (fases)** | 1) Early warning (24 h). 2) Informe complet inicial (48–72 h). 3) Informe final amb causes i mesures. | Similar a NIS2: notificació inicial + informes de seguiment per al CCN-CERT. | 1) Notificació a AEPD. 2) Si hi ha alt risc → comunicació als afectats sense dilació indeguda. |
| **Contingut mínim de l’avís** | Naturalesa de l’incident, impacte, sistemes afectats, mesures aplicades, evidències i estimació de risc. | Idèntic enfocament: sistemes afectats, impacte, mesures i traçabilitat ENS. | Tipus de dades afectades, nombre d’afectats, conseqüències, mesures aplicades i previstes. |
| **Cal avisar els afectats?** | ❌ No habitualment, excepte si per efectes indirectes hi ha risc per persones físiques. | ❌ No (el focus és institucional). | ✔️ Sí, si hi ha alt risc per drets i llibertats. |
| **Exemples d’incidents que obliguen a notificar** | Ciberatac que atura serveis essencials, ransomware en hospital, caiguda massiva de telecomunicacions. | Caiguda d’una plataforma pública, intrusió en sistemes municipals, corrupció de dades en serveis públics. | Filtració de dades de ciutadans, accés indegut a dades, pèrdua de dispositius amb dades personals. |

## 2. Taula de llindars i condicions de notificació

| **Marc** | **Quan s’activa l’obligació exactament?** | **Llindars d’incidència** |
|----------|------------------------------------------|---------------------------|
| **NIS2** | Quan l’incident té impacte significatiu, és a dir, afecta la capacitat de l’organització de prestar un servei essencial o important. [es.isms.online] | Impacte en: servei essencial, nombre d’usuaris afectats, durada, efecte sobre l’economia o seguretat pública. |
| **ENS** | Quan l’incident comprometi la seguretat dels sistemes d’informació públics o la informació que gestionen. | Basat en: severitat, afectació a serveis públics, disponibilitat i integritat del sistema. |
| **RGPD** | Quan es produeix una violació de dades personals i aquesta pot comprometre drets o llibertats. [eiposgrados.com] | Si no hi ha risc → no cal avisar als afectats (només AEPD). Si hi ha alt risc → s’avisa també als afectats. |

## 3. Taula: temps i responsabilitats segons el tipus d’incident

| **Tipus d’incident** | **NIS2** | **ENS** | **RGPD** |
|----------------------|----------|---------|----------|
| **Ransomware que atura serveis** | Notificar en 24 h | Notificar al CCN‑CERT | Només si afecta dades personals |
| **Caiguda de servei essencial** | Notificar en 24 h | Notificar | ❌ No aplicable |
| **Filtració de dades personals** | Notificar si afecta continuïtat | Notificar si afecta SE públic | ✔️ Notificar AEPD (<72 h) i afectats si alt risc |
| **Bretxa interna sense afectació greu** | Si és significatiu → sí | Segons gravetat ENS | Sí, si afecta dades personals |
| **Compromís de credencials** | Si afecta operativitat → sí | Sí | Sí, si contenen dades personals |