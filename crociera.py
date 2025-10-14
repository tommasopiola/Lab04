import csv
from cabina import Cabina
from cabina import CabinaStilosa
from cabina import CabinaAnimale
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabine = []
        self.cabineanimali = []
        self.cabinestilose = []
        self.passeggeri= []

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for riga in reader:
                    #leggo cabine speciali
                    if len(riga) == 5:
                        #leggo cabine animali
                        if isinstance(riga[4], int):
                            codice_cabina, nposti, nponte, prezzo_a_notte, nanimali = riga
                            cabina = CabinaAnimale(codice_cabina.strip(), nposti.strip(),nponte.strip(), prezzo_a_notte.strip(), nanimali.strip())
                            self.cabineanimali.append(cabina)
                        #leggo cabine lusso
                        else:
                            codice_cabina, nposti, nponte, prezzo_a_notte, stile = riga
                            cabina = CabinaStilosa(codice_cabina.strip(), nposti.strip(),nponte.strip(), prezzo_a_notte.strip(), stile.strip())
                            self.cabinestilose.append(cabina)
                            pass    # == int allora cabina animali
                    #leggo cabine normali
                    elif len(riga) == 4:
                        codice_cabina, nposti, nponte, prezzo_a_notte = riga
                        cabina = Cabina(codice_cabina.strip(), nposti.strip(), nponte.strip(), prezzo_a_notte.strip())
                        self.cabine.append(cabina)
                    #leggo passeggeri
                    else:
                        codice_passeggero, nome, cognome = riga
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.passeggeri.append(passeggero)

            print(f"{len(self.cabine)} cabine caricate correttamente dal file '{file_path}'.")
            print(f"{len(self.passeggeri)} passeggeri caricati correttamente dal file '{file_path}'.")


        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: il file '{file_path}' non esiste.")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

