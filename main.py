from tipi import PokemonFuoco, PokemonAcqua, PokemonErba
from creatura_esterna import CreaturaEsterna
from allenatore import Allenatore
from pokedex import Pokedex


def carica_dati_esempio(pokedex):
    """pre-carica i dati di esempio descritti nella consegna."""

    # allenatori
    ash   = Allenatore("Ash", medaglie=4)
    misty = Allenatore("Misty", medaglie=3)
    pokedex.registra_allenatore(ash)
    pokedex.registra_allenatore(misty)

    # pokemon di Ash
    charizard = PokemonFuoco("Charizard", 36, "Fiammetta")
    bulbasaur = PokemonErba("Bulbasaur", 15)
    squirtle  = PokemonAcqua("Squirtle", 20, "Splash")
    ash.aggiungi_pokemon(charizard)
    ash.aggiungi_pokemon(bulbasaur)
    ash.aggiungi_pokemon(squirtle)
    pokedex.pokemon_registrati.extend([charizard, bulbasaur, squirtle])

    # pokemon di Misty
    gyarados = PokemonAcqua("Gyarados", 40)
    starmie  = PokemonAcqua("Starmie", 30, "Stella")
    misty.aggiungi_pokemon(gyarados)
    misty.aggiungi_pokemon(starmie)
    pokedex.pokemon_registrati.extend([gyarados, starmie])

    # creatura esterna di Ash
    agumon = CreaturaEsterna("Agumon", 25, 110)
    ash.aggiungi_pokemon(agumon)
    pokedex.pokemon_registrati.append(agumon)


def menu_principale():
    pokedex = Pokedex()
    carica_dati_esempio(pokedex)

    while True:
        print("\n" + "=" * 40)
        print("    POKEMANAGER - Centro Ricerche")
        print("=" * 40)
        print("1. Registra nuovo Pokemon")
        print("2. Registra nuovo Allenatore")
        print("3. Assegna Pokemon a un Allenatore")
        print("4. Cerca Pokemon")
        print("5. Visualizza scheda Pokemon")
        print("6. Allena un Pokemon")
        print("7. Visualizza squadra Allenatore")
        print("8. Registra Creatura Esterna")
        print("9. Report e Statistiche")
        print("0. Esci")
        print()

        scelta = input("Scelta: ").strip()

        # ---- 1 Registra nuovo Pokemon ----
        if scelta == "1":
            print("\n--- REGISTRA NUOVO POKEMON ---")
            nome = input("Nome: ").strip()
            print("Tipo (1=Fuoco, 2=Acqua, 3=Erba): ", end="")
            tipo = input().strip()
            livello = int(input("Livello (1-100): ").strip())
            soprannome = input("Soprannome (invio per saltare): ").strip() or None

            if tipo == "1":
                p = PokemonFuoco(nome, livello, soprannome)
            elif tipo == "2":
                p = PokemonAcqua(nome, livello, soprannome)
            elif tipo == "3":
                p = PokemonErba(nome, livello, soprannome)
            else:
                print("Tipo non valido!")
                continue

            pokedex.pokemon_registrati.append(p)
            print(f"Pokemon registrato! PS calcolati: {p.ps}")

        # ---- 2 Registra nuovo Allenatore ----
        elif scelta == "2":
            print("\n--- REGISTRA NUOVO ALLENATORE ---")
            nome = input("Nome: ").strip()
            medaglie = int(input("Numero medaglie (0-8): ").strip())
            a = Allenatore(nome, medaglie)
            print(pokedex.registra_allenatore(a))

        # ---- 3 Assegna Pokemon a un Allenatore ----
        elif scelta == "3":
            print("\n--- ASSEGNA POKEMON ---")
            nome_pokemon = input("Nome del Pokemon: ").strip()
            nome_allenatore = input("Nome dell'Allenatore: ").strip()
            p = pokedex.trova_pokemon(nome_pokemon)
            a = pokedex.trova_allenatore(nome_allenatore)
            if not p:
                print(f" Pokemon '{nome_pokemon}' non trovato.")
            elif not a:
                print(f" Allenatore '{nome_allenatore}' non trovato.")
            else:
                print(a.aggiungi_pokemon(p))

        # ---- 4 Cerca Pokemon ----
        elif scelta == "4":
            print("\n--- CERCA POKEMON ---")
            print("1. Per nome  2. Per tipo  3. Per intervallo livello  4. Elenca tutti")
            sotto = input("Scelta: ").strip()

            if sotto == "1":
                nome = input("Nome (anche parziale): ").strip()
                risultati = pokedex.cerca_per_nome(nome)
            elif sotto == "2":
                tipo = input("Tipo (Fuoco/Acqua/Erba): ").strip()
                risultati = pokedex.cerca_per_tipo(tipo)
            elif sotto == "3":
                lmin = int(input("Livello minimo: "))
                lmax = int(input("Livello massimo: "))
                risultati = pokedex.cerca_per_livello(lmin, lmax)
            elif sotto == "4":
                risultati = pokedex.elenca_tutti()
            else:
                print("Scelta non valida.")
                continue

            if risultati:
                for p in risultati:
                    print(f"  - {p.nome} ({p.tipo()}) Lv.{p.livello} | PS: {p.ps}")
            else:
                print("Nessun Pokemon trovato.")

        # ---- 5 Visualizza scheda Pokemon ----
        elif scelta == "5":
            print("\n--- SCHEDA POKEMON ---")
            nome = input("Nome del Pokemon: ").strip()
            p = pokedex.trova_pokemon(nome)
            if p:
                print(p.scheda())
            else:
                print(f" Pokemon '{nome}' non trovato.")

        # ---- 6 Allena un Pokemon ----
        elif scelta == "6":
            print("\n--- ALLENAMENTO ---")
            nome = input("Nome del Pokemon: ").strip()
            p = pokedex.trova_pokemon(nome)
            if p:
                print(p.allena())
            else:
                print(f" Pokemon '{nome}' non trovato.")

        # ---- 7 Visualizza squadra Allenatore ----
        elif scelta == "7":
            print("\n--- SQUADRA ALLENATORE ---")
            nome = input("Nome dell'Allenatore: ").strip()
            a = pokedex.trova_allenatore(nome)
            if a:
                print(a.visualizza_squadra())
            else:
                print(f" Allenatore '{nome}' non trovato.")

        # ---- 8 Registra Creatura Esterna ----
        elif scelta == "8":
            print("\n--- REGISTRA CREATURA ESTERNA ---")
            nome = input("Nome: ").strip()
            livello = int(input("Livello: ").strip())
            ps = int(input("PS: ").strip())
            c = CreaturaEsterna(nome, livello, ps)
            pokedex.pokemon_registrati.append(c)
            print(f" Creatura esterna '{nome}' registrata.")

        # ---- 9 Report e Statistiche ----
        elif scelta == "9":
            print(pokedex.genera_report())

        # ---- 0 Esci ----
        elif scelta == "0":
            print("Arrivederci dal Centro Ricerche!")
            break

        else:
            print("Scelta non valida, riprova.")


#AVVIO PROGRAMMA
if __name__ == "__main__":
    menu_principale()