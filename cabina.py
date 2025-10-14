class Cabina:
    def __init__(self, codice_cabina, nposti, prezzo_a_notte, affittata=False):
        self.codice = codice_cabina
        self.nposti = nposti
        self.prezzo_a_notte = prezzo_a_notte

        self.affittata = bool(affittata)

class CabinaStilosa(Cabina):
    def __init__(self, codice_cabina, nposti, prezzo_a_notte, affittata, stile):
        self.stile = stile

class CabinaAnimale(Cabina):
    def __init__(self, codice_cabina, nposti, prezzo_a_notte, affittata, nanimali):
        self.nanimali = nanimali

#modifico classi figlie
