from pokemon import Pokemon  # importiamo la classe base


class CreaturaEsterna(Pokemon):
    
    #creatura non classificata (es. Digimon).
    #funziona come un Pokemon per la gestione quotidiana,ma viene esclusa dai report ufficiali per tipo
    

    def __init__(self, nome, livello, ps):
        self._ps_fissi = ps  # PS forniti manualmente
        super().__init__(nome, livello, soprannome=None)

    def tipo(self):
        return "Non Classificata"

    def calcola_ps(self):
        return self._ps_fissi

    def allena(self):
        messaggio = super().allena()
        messaggio += f"\nPS: {self.ps}"
        return messaggio

    def scheda(self):
        return (
            f"╔══════════════════════════════╗\n"
            f"║  {self.nome.upper()} (Creatura Esterna)\n"
            f"║  Lv.{self.livello}\n"
            f"║  PS: {self.ps}\n"
            f"╚══════════════════════════════╝"
        )