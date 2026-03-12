
from pokemon import Pokemon  # importiamo la classe base


class PokemonFuoco(Pokemon):
    """Pokemon di tipo Fuoco."""

    def __init__(self, nome, livello, soprannome=None):
        self.potenza_fiamma = 10  # inizializzato PRIMA di super()
        super().__init__(nome, livello, soprannome)

    def tipo(self):
        return "Fuoco"

    def calcola_ps(self):
        return 80 + (self.livello * 2) + self.potenza_fiamma

    def allena(self):
        messaggio = super().allena()
        if self.livello % 3 == 0:
            self.potenza_fiamma += 1
            self.ps = self.calcola_ps()
            messaggio += f"\nPotenza Fiamma aumentata! → {self.potenza_fiamma}"
        messaggio += f"\nPS aggiornati: {self.ps}"
        return messaggio

    def scheda(self):
        fiamme = "" * (self.potenza_fiamma // 2)
        soprannome_str = f"\n║  Soprannome: {self.soprannome}" if self.soprannome else ""
        return (
            f"╔══════════════════════════════╗\n"
            f"║  {self.nome.upper()} (Fuoco) Lv.{self.livello}{soprannome_str}\n"
            f"║  PS: {self.ps}\n"
            f"║  Potenza Fiamma: {self.potenza_fiamma}\n"
            f"║  {fiamme}\n"
            f"╚══════════════════════════════╝"
        )


class PokemonAcqua(Pokemon):
    """Pokemon di tipo Acqua."""

    def __init__(self, nome, livello, soprannome=None):
        self.resistenza_marea = 8  # inizializzato prima di super()
        super().__init__(nome, livello, soprannome)

    def tipo(self):
        return "Acqua"

    def calcola_ps(self):
        return 90 + (self.livello * 3)

    def allena(self):
        messaggio = super().allena()
        if self.livello % 4 == 0:
            self.resistenza_marea += 1
            messaggio += f"\nResistenza Marea aumentata! → {self.resistenza_marea}"
        messaggio += f"\nPS aggiornati: {self.ps}"
        return messaggio

    def scheda(self):
        riduzione = self.resistenza_marea * 3
        soprannome_str = f"\n║  Soprannome: {self.soprannome}" if self.soprannome else ""
        return (
            f"╔══════════════════════════════╗\n"
            f"║  {self.nome.upper()} (Acqua) Lv.{self.livello}{soprannome_str}\n"
            f"║  PS: {self.ps}\n"
            f"║  Resistenza Marea: {self.resistenza_marea}\n"
            f"║  Riduzione danni: {riduzione}%\n"
            f"╚══════════════════════════════╝"
        )


class PokemonErba(Pokemon):
    """Pokemon di tipo Erba."""

    def __init__(self, nome, livello, soprannome=None):
        self.rigenerazione = 5  # inizializzato prima di super()
        super().__init__(nome, livello, soprannome)

    def tipo(self):
        return "Erba"

    def calcola_ps(self):
        return 85 + (self.livello * 2) + (self.rigenerazione * 3)

    def allena(self):
        messaggio = super().allena()
        if self.livello % 2 == 0:
            self.rigenerazione += 1
            self.ps = self.calcola_ps()
            messaggio += f"\nRigenerazione aumentata! → {self.rigenerazione}"
        messaggio += f"\nPS aggiornati: {self.ps}"
        return messaggio

    def scheda(self):
        ps_per_turno = self.rigenerazione * 2
        soprannome_str = f"\n║  Soprannome: {self.soprannome}" if self.soprannome else ""
        return (
            f"╔══════════════════════════════╗\n"
            f"║  {self.nome.upper()} (Erba) Lv.{self.livello}{soprannome_str}\n"
            f"║  PS: {self.ps}\n"
            f"║  Rigenerazione: {self.rigenerazione}\n"
            f"║  PS recuperati/turno: {ps_per_turno}\n"
            f"╚══════════════════════════════╝"
        )