# PokeManager - Gestionale Pokemon

Un centro di ricerca Pokemon ti ha commissionato lo sviluppo di un gestionale per catalogare, organizzare e analizzare i Pokemon catturati dai vari allenatori.

Di seguito trovi i requisiti funzionali del sistema.

---

# Contesto

Il Professor Oak ha bisogno di un sistema per il suo laboratorio.  
Ogni giorno riceve Pokemon da decine di allenatori e ha bisogno di:

- Registrare i Pokemon con tutte le loro informazioni
- Consultare rapidamente le schede dei Pokemon
- Gestire gli allenatori e i loro Pokemon
- Generare report e statistiche

Il sistema funziona interamente da terminale con un **menu testuale**.

---

# Requisiti Funzionali

## RF01 - Registrazione Pokemon

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

## RF02 - Scheda Pokemon

Ogni Pokemon deve poter generare la propria **scheda descrittiva testuale**.

La scheda deve contenere:

- nome
- tipo
- livello
- PS

e un dettaglio specifico per tipo:

- **Fuoco:** mostra la *Potenza Fiamma* e un indicatore visivo  
  `"🔥" x potenza_fiamma / 2`
- **Acqua:** mostra la *Resistenza Marea* e la percentuale di riduzione danni  
  `(resistenza x 3%)`
- **Erba:** mostra la *Rigenerazione* e i PS recuperati per turno  
  `(rigenerazione x 2)`

### Esempio scheda (tipo Fuoco)

Arrivederci dal Centro Ricerche!

