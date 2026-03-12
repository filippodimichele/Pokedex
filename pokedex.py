from creatura_esterna import CreaturaEsterna  # serve per distinguerle nei report


class Pokedex:
    """gestisce tutti i Pokemon e gli allenatori registrati."""

    def __init__(self):
        self.pokemon_registrati = []  # tutti i Pokemon (incluse creature esterne)
        self.allenatori = []

    # --- registrazione ---

    def registra_pokemon(self, pokemon, allenatore=None):
        self.pokemon_registrati.append(pokemon)
        if allenatore:
            return allenatore.aggiungi_pokemon(pokemon)
        return f" {pokemon.nome} registrato nel Pokedex."

    def registra_allenatore(self, allenatore):
        self.allenatori.append(allenatore)
        return f" Allenatore {allenatore.nome} registrato."

    # --- Ricerca ---

    def cerca_per_nome(self, nome):
        return [p for p in self.pokemon_registrati if nome.lower() in p.nome.lower()]

    def cerca_per_tipo(self, tipo):
        return [p for p in self.pokemon_registrati if p.tipo().lower() == tipo.lower()]

    def cerca_per_livello(self, livello_min, livello_max):
        return [p for p in self.pokemon_registrati
                if livello_min <= p.livello <= livello_max]

    def elenca_tutti(self):
        """restituisce tutti i Pokemon ordinati per livello (dal più alto)."""
        return sorted(self.pokemon_registrati, key=lambda p: p.livello, reverse=True)

    def trova_pokemon(self, nome):
        """trova un Pokemon per nome esatto (case-insensitive)."""
        for p in self.pokemon_registrati:
            if p.nome.lower() == nome.lower():
                return p
        return None

    def trova_allenatore(self, nome):
        """trova un allenatore per nome esatto (case-insensitive)."""
        for a in self.allenatori:
            if a.nome.lower() == nome.lower():
                return a
        return None

    # --- Report ---

    def genera_report(self):
        totale = len(self.pokemon_registrati)
        creature_esterne = [p for p in self.pokemon_registrati if isinstance(p, CreaturaEsterna)]
        pokemon_ufficiali = [p for p in self.pokemon_registrati if not isinstance(p, CreaturaEsterna)]

        fuoco = [p for p in pokemon_ufficiali if p.tipo() == "Fuoco"]
        acqua = [p for p in pokemon_ufficiali if p.tipo() == "Acqua"]
        erba  = [p for p in pokemon_ufficiali if p.tipo() == "Erba"]

        def piu_forte(lista):
            return max(lista, key=lambda p: p.ps) if lista else None

        livello_medio = (sum(p.livello for p in pokemon_ufficiali) / len(pokemon_ufficiali)
                         if pokemon_ufficiali else 0)

        allenatore_forte = (max(self.allenatori, key=lambda a: a.ps_totali())
                            if self.allenatori else None)

        report = f"\n{'='*40}\n"
        report += f"  REPORT E STATISTICHE\n"
        report += f"{'='*40}\n"
        report += f"Totale Pokemon registrati: {totale}"
        if creature_esterne:
            report += f" (di cui {len(creature_esterne)} creature esterne)"
        report += f"\n\nPer tipo:\n"
        report += f"  Fuoco: {len(fuoco)}\n"
        report += f"  Acqua: {len(acqua)}\n"
        report += f"  Erba:  {len(erba)}\n"

        report += f"\nPokemon più forte per tipo:\n"
        for tipo, lista in [("Fuoco", fuoco), ("Acqua", acqua), ("Erba", erba)]:
            p = piu_forte(lista)
            if p:
                report += f"  {tipo}: {p.nome} (PS: {p.ps})\n"
            else:
                report += f"  {tipo}: nessuno\n"

        report += f"\nLivello medio: {livello_medio:.1f}\n"

        if allenatore_forte:
            report += f"Allenatore più forte: {allenatore_forte.nome} (PS totali: {allenatore_forte.ps_totali()})\n"

        return report