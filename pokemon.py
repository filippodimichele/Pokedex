class Pokemon:
    """classe base per tutti i Pokemon."""

    def __init__(self, nome, livello, soprannome=None):
        self.nome = nome
        self.livello = livello
        self.soprannome = soprannome
        self.ps = self.calcola_ps()

    def calcola_ps(self):
        # verrà sovrascritto dalle classi figlie
        return 0

    def tipo(self):
        # verrà sovrascritto dalle classi figlie
        return "Sconosciuto"

    def allena(self):
        self.livello += 1
        self.ps = self.calcola_ps()
        return f"{self.nome} si è allenato! Livello: {self.livello - 1} → {self.livello}"

    def scheda(self):
        # verrà sovrascritto dalle classi figlie
        return f"{self.nome} - Lv.{self.livello} - PS: {self.ps}"

    def __str__(self):
        return self.scheda()