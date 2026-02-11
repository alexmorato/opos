### 🚀 MPLS (Multiprotocol Label Switching)

**Tecnologia de xarxa de nivell 2.5** que utilitza **etiquetes (labels)** per encaminar paquets, en lloc d'adreces IP llargues, creant **camins virtuals predeterminats** (LSP - Label Switched Paths).

> 📝 **Frase clau:** És una tecnologia de **commutació per etiquetes** que permet un encaminament més **ràpid, eficient i amb qualitat de servei (QoS)** que l'encaminament IP tradicional, especialment en **xarxes troncals de gran volum (backbones)**.

---

### 🚦 Conceptes clau de MPLS per a examen

| Concepte | Explicació | Frase Clau |
|----------|------------|------------|
| **LSP (Label Switched Path)** | Camí unidireccional predeterminat que segueixen els paquets dins la xarxa MPLS. | És el **túnel virtual** que creua la xarxa MPLS, definit per una seqüència d'etiquetes. |
| **LER (Label Edge Router)** | Router d'entrada/sortida de la xarxa MPLS; **afegir** (push) o **treure** (pop) l'etiqueta. | Actua com a **porta d'enllaç** entre la xarxa IP tradicional i el domini MPLS. |
| **LSR (Label Switch Router)** | Router intermedi que **commuta paquets** basant-se només en l'etiqueta, sense obrir l'encapçalament IP. | Realitza **commutació ràpida** mitjançant taules d'etiquetes (LIB - Label Information Base). |
| **FEC (Forwarding Equivalence Class)** | Conjunt de paquets que reben el **mateix tractament** i segueixen el mateix LSP. | Agrupa trànsit amb **destí o QoS similar** per assignar-li una etiqueta comuna. |
| **Push / Swap / Pop** | Operacions bàsiques sobre etiquetes: **afegir**, **intercanviar** o **eliminar**. | L'**etiqueta es manipula** a cada salt: Push a l'entrada, Swap als intermedis, Pop a la sortida. |
| **MPLS VPN** | Ús de MPLS per crear **xarxes privades virtuales** escalables sobre infraestructura compartida. | Permet **separar trànsit de diferents clients** amb etiquetes, garantint aïllament i seguretat. |
| **TE (Traffic Engineering)** | Capacitat de **controlar explícitament** el camí del trànsit per evitar congestió. | Optimitza l'ús dels enllaços **desviant trànsit de rutes curtes però congestionades** a rutes llargues però lliures. |
| **MPLS-TP** | Perfil de MPLS per a **xarxes de transport** (operadores), sense necessitat de protocols de ruteig IP. | Versió **simplificada i orientada a la gestió** per a xarxes de telecomunicacions. |

---

> 📝 **Frase clau global:** MPLS **no encamina per adreça IP**, sinó que **commuta per etiquetes**, oferint **velocitat, QoS i capacitat per crear túnels VPN** de forma eficient.

---

![Esquema conceptual de MPLS: CE, PE, P, LER, LSR, LSP](https://www.acuative.com/sites/default/files/styles/wide/public/assets/resources/MPLS%20POST.png)

Aquesta imatge il·lustra gràficament els conceptes clau de MPLS que hem estudiat: **CE (Customer Edge)**, **PE (Provider Edge)**, **P (Provider router)**, **LER (Label Edge Router)**, **LSR (Label Switching Router)** i **LSP (Label Switched Path)**. És molt útil per visualitzar la relació entre els diferents components d'una xarxa MPLS.

### 📋 Taula de conceptes MPLS (basada en la imatge)

| Concepte | Acrònim | Funció a la xarxa MPLS | Ubicació |
|----------|---------|------------------------|----------|
| **Customer Edge** | CE | Router de **client** que connecta amb el proveïdor; **desconeix MPLS**, només parla IP. | Xarxa del client |
| **Provider Edge** | PE | Router de **frontera del proveïdor**; connecta amb els CE i **etiqueta/desetiqueta** els paquets (LER). | Perifèria del núvol MPLS |
| **Provider Router** | P | Router **intern del proveïdor**; només commuta per etiquetes (LSR), **no gestiona IP** dels clients. | Nucli del núvol MPLS |
| **Label Edge Router** | LER | Sinònim de **PE**; realitza **push/pop** d'etiquetes a l'entrada/sortida. | Entrada/sortida del domini MPLS |
| **Label Switching Router** | LSR | Sinònim de **P**; realitza **swap** (intercanvi) d'etiquetes al nucli. | Nucli del domini MPLS |
| **Label Switched Path** | LSP | **Camí virtual unidireccional** que segueix un paquet etiquetat dins la xarxa MPLS. | A través dels LSR i LER |

---

> 📝 **Frase clau:** La imatge mostra clarament la **jerarquia MPLS**: els **CE** parlen IP amb els **PE/LER**, aquests encapsulen amb etiquetes, els **P/LSR** commuten ràpidament per etiquetes, i tot segueix un **LSP** predefinit.