class Cabina:
    def __init__(self, codice_cabina, nposti, ponte, prezzo_base, affittata = False):
        self.codice = codice_cabina
        self.nposti = int(nposti)
        self.ponte = int(ponte)
        self.prezzo_base = float(prezzo_base)
        self.affittata = affittata

    def prezzo_finale(self):
        """Cabina standard: prezzo = prezzo base"""
        return self.prezzo_base

    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self.codice == other.codice
        return False

    def __lt__(self, other):
        return self.prezzo_finale() < other.prezzo_finale()

    def __str__(self):
        stato = "Occupata" if self.affittata else "Disponibile"
        return f"{self.codice}: Standard | {self.nposti} letti - Ponte {self.ponte} - Prezzo {self.prezzo_finale():.2f}€ - {stato}"

class CabinaDeluxe(Cabina):
    def __init__(self, codice_cabina, nposti, ponte, prezzo_base, stile):
        super().__init__(codice_cabina, nposti, ponte, prezzo_base)
        self.stile = stile

    def prezzo_finale(self):
        return self.prezzo_base * 1.20

    def __str__(self):
        stato = "Occupata" if self.affittata else "Disponibile"
        return f"{self.codice}: Deluxe ({self.stile}) | {self.nposti} letti - Ponte {self.ponte} - Prezzo {self.prezzo_finale():.2f}€ - {stato}"

class CabinaAnimale(Cabina):
    def __init__(self, codice_cabina, nposti, ponte, prezzo_base, max_animali):
        super().__init__(codice_cabina, nposti, ponte, prezzo_base)
        self.max_animali = int(max_animali)

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.10 * self.max_animali)

    def __str__(self):
        stato = "Occupata" if self.affittata else "Disponibile"
        return f"{self.codice}: Animali | {self.nposti} letti - Ponte {self.ponte} - Prezzo {self.prezzo_finale():.2f}€ - Max animali: {self.max_animali} - {stato}"