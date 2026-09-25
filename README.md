<p align="center">
<img width="1280" height="1238" alt="image" src="https://github.com/user-attachments/assets/fdd319c9-985b-4e7a-b44f-883c20e79885" />
</p>


# PokeManager - Gestionale Pokemon

Un centro di ricerca Pokemon ti ha commissionato lo sviluppo di un gestionale per catalogare, organizzare e analizzare i Pokemon catturati dai vari allenatori.

Di seguito trovi i requisiti funzionali del sistema.

---

## Contesto

Il Professor Oak ha bisogno di un sistema per il suo laboratorio.  
Ogni giorno riceve Pokemon da decine di allenatori e ha bisogno di:

- Registrare i Pokemon con tutte le loro informazioni
- Consultare rapidamente le schede dei Pokemon
- Gestire gli allenatori e i loro Pokemon
- Generare report e statistiche

Il sistema funziona interamente da terminale con un **menu testuale**.

---

## Requisiti Funzionali

### RF01 - Registrazione Pokemon

Il sistema deve permettere di registrare un Pokemon specificando:

- **Nome** (es. "Charizard")
- **Tipo** tra: Fuoco, Acqua, Erba
- **Livello** (da 1 a 100)
- **Soprannome** (opzionale, dato dall'allenatore)

Ogni tipo di Pokemon ha caratteristiche specifiche:

| Tipo  | PS Base | Attributo Speciale |
|------|--------|--------------------|
| Fuoco | 80 | Potenza Fiamma (inizia a 10) |
| Acqua | 90 | Resistenza Marea (inizia a 8) |
| Erba | 85 | Rigenerazione (inizia a 5) |

I **PS (Punti Salute)** effettivi di un Pokemon si calcolano in modo diverso a seconda del tipo:

- **Fuoco:** `PS Base + (Livello x 2) + Potenza Fiamma`
- **Acqua:** `PS Base + (Livello x 3)`
- **Erba:** `PS Base + (Livello x 2) + (Rigenerazione x 3)`

---

### RF02 - Scheda Pokemon

Ogni Pokemon deve poter generare la propria **scheda descrittiva testuale**.

La scheda deve contenere:

- Nome
- Tipo
- Livello
- PS

e un dettaglio specifico per tipo:

- **Fuoco:** mostra la *Potenza Fiamma* e un indicatore visivo  
  `"🔥" x potenza_fiamma / 2`

- **Acqua:** mostra la *Resistenza Marea* e la percentuale di riduzione danni  
  `(resistenza x 3%)`

- **Erba:** mostra la *Rigenerazione* e i PS recuperati per turno  
  `(rigenerazione x 2)`

Esempio di scheda per un Pokemon di tipo Fuoco:


╔══════════════════════════════╗
║ CHARIZARD (Fuoco) Lv.36 ║
║ Soprannome: Fiammetta ║
║ PS: 162 ║
║ Potenza Fiamma: 10 ║
║ 🔥🔥🔥🔥🔥 ║
╚══════════════════════════════╝


---

### RF03 - Allenamento

Ogni Pokemon può essere **allenato**.

L'allenamento:

- aumenta il **livello di 1**
- migliora l'attributo speciale

Il miglioramento funziona diversamente per ogni tipo:

- **Fuoco:** la Potenza Fiamma aumenta di **1 ogni 3 livelli**
- **Acqua:** la Resistenza Marea aumenta di **1 ogni 4 livelli**
- **Erba:** la Rigenerazione aumenta di **1 ogni 2 livelli**

Dopo l'allenamento i **PS vengono ricalcolati automaticamente**.

---

### RF04 - Gestione Allenatori

Il sistema deve gestire gli **Allenatori**.

Ogni allenatore ha:

- **Nome**
- **Numero medaglie** (da 0 a 8)
- **Lista di Pokemon** (massimo 6)

Un allenatore deve poter:

- Aggiungere un Pokemon alla propria squadra (se ha meno di 6 Pokemon)
- Rimuovere un Pokemon dalla squadra (per nome o soprannome)
- Visualizzare il riepilogo della propria squadra con le schede di tutti i Pokemon

---

### RF05 - Pokedex Centrale

Il **Pokedex Centrale** è il cuore del gestionale.

Deve permettere di:

- Registrare un nuovo Pokemon e assegnarlo a un allenatore
- Cercare Pokemon per **nome**, **tipo** o **intervallo di livello**
- Elencare tutti i Pokemon registrati, **ordinati per livello (dal più alto)**
- Filtrare per tipo
- Mostrare la scheda di un Pokemon specifico

---

### RF06 - Report e Statistiche

Il sistema deve generare un report con:

- **Totale Pokemon registrati**
- **Conteggio per tipo**: quanti Fuoco, quanti Acqua, quanti Erba
- **Pokemon più forte per tipo** (quello con i PS più alti)
- **Livello medio** di tutti i Pokemon
- **Allenatore con la squadra più forte** (somma dei PS di tutti i suoi Pokemon)

---

### RF07 - Creature Esterne

Alcuni allenatori viaggiano in regioni lontane e catturano creature che non sono dei Pokemon classici (ad esempio i Digimon).

Queste creature hanno:

- Nome
- Livello
- PS
- Scheda descrittiva

Non appartengono alla classificazione ufficiale dei tipi Pokemon.

Il sistema deve poterle registrare nel Pokedex come **"Creature Non Classificate"** e devono poter essere:

- Aggiunte alla squadra di un allenatore (contano nel limite di 6)
- Visualizzate con la propria scheda nel Pokedex
- Escluse dai report ufficiali per tipo (RF06)
- Incluse nel conteggio totale dei Pokemon registrati

In pratica una creatura esterna funziona come un Pokemon ai fini della gestione quotidiana, ma viene distinta quando servono statistiche ufficiali.

---

### RF08 - Menu Principale

All'avvio il sistema mostra:

========================================
POKEMANAGER - Centro Ricerche

Registra nuovo Pokemon

Registra nuovo Allenatore

Assegna Pokemon a un Allenatore

Cerca Pokemon

Visualizza scheda Pokemon

Allena un Pokemon

Visualizza squadra Allenatore

Registra Creatura Esterna

Report e Statistiche

Esci

Scelta:


---

## Dati di Esempio per il Test

Per facilitare i test, all'avvio il sistema può **pre-caricare i seguenti dati**.

### Allenatori

| Nome | Medaglie |
|-----|---------|
| Ash | 4 |
| Misty | 3 |

### Pokemon di Ash

| Nome | Tipo | Livello | Soprannome |
|-----|------|--------|------------|
| Charizard | Fuoco | 36 | Fiammetta |
| Bulbasaur | Erba | 15 | - |
| Squirtle | Acqua | 20 | Splash |

### Pokemon di Misty

| Nome | Tipo | Livello | Soprannome |
|-----|------|--------|------------|
| Gyarados | Acqua | 40 | - |
| Starmie | Acqua | 30 | Stella |

### Creatura Esterna di Ash

| Nome | Livello | PS |
|-----|--------|----|
| Agumon | 25 | 110 |

---

## Esempio di Interazione

========================================
POKEMANAGER - Centro Ricerche

Scelta: 1

--- REGISTRA NUOVO POKEMON ---
Nome: Pikachu
Tipo (1=Fuoco, 2=Acqua, 3=Erba): 1
Livello: 25
Soprannome (invio per saltare): Sparky

Pokemon registrato! PS calcolati: 140

Scelta: 5

--- SCHEDA POKEMON ---
Nome del Pokemon: Charizard

╔══════════════════════════════╗
║ CHARIZARD (Fuoco) Lv.36 ║
║ Soprannome: Fiammetta ║
║ PS: 162 ║
║ Potenza Fiamma: 10 ║
║ 🔥🔥🔥🔥🔥 ║
╚══════════════════════════════╝

Scelta: 6

--- ALLENAMENTO ---
Nome del Pokemon: Bulbasaur
Bulbasaur si e allenato! Livello: 15 → 16
Rigenerazione aumentata! 5 → 6
PS aggiornati: 132

Scelta: 9

--- REPORT ---
Totale Pokemon registrati: 7 (di cui 1 creatura esterna)

Per tipo:
Fuoco: 2
Acqua: 3
Erba: 1

Pokemon piu forte per tipo:
Fuoco: Charizard (PS: 162)
Acqua: Gyarados (PS: 210)
Erba: Bulbasaur (PS: 135)

Livello medio: 27.3

Allenatore piu forte: Ash (PS totali: 539)

Scelta: 0
Arrivederci dal Centro Ricerche!
