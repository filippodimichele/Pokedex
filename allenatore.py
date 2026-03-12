class Allenatore:
    """rappresenta un allenatore Pokemon."""

    MAX_POKEMON = 6

    def __init__(self, nome, medaglie=0):
        self.nome = nome
        self.medaglie = medaglie
        self.squadra = []  # lista di Pokemon (max 6)

    def aggiungi_pokemon(self, pokemon):
        if len(self.squadra) >= self.MAX_POKEMON:
            return f" {self.nome} ha già {self.MAX_POKEMON} Pokemon! Non può aggiungerne altri."
        self.squadra.append(pokemon)
        return f" {pokemon.nome} aggiunto alla squadra di {self.nome}!"

    def rimuovi_pokemon(self, identificatore):
        """rimuove un Pokemon per nome o soprannome."""
        for p in self.squadra:
            if p.nome.lower() == identificatore.lower() or \
               (p.soprannome and p.soprannome.lower() == identificatore.lower()):
                self.squadra.remove(p)
                return f" {p.nome} rimosso dalla squadra di {self.nome}."
        return f" Nessun Pokemon chiamato '{identificatore}' nella squadra di {self.nome}."

    def ps_totali(self):
        return sum(p.ps for p in self.squadra)

    def visualizza_squadra(self):
        if not self.squadra:
            return f"La squadra di {self.nome} è vuota."
        output = f"\n{'='*40}\n"
        output += f"  Squadra di {self.nome} (Medaglie: {self.medaglie})\n"
        output += f"{'='*40}\n"
        for p in self.squadra:
            output += p.scheda() + "\n"
        output += f"PS Totali squadra: {self.ps_totali()}\n"
        return output

    def __str__(self):
        return f"Allenatore {self.nome} | Medaglie: {self.medaglie} | Pokemon: {len(self.squadra)}/{self.MAX_POKEMON}"