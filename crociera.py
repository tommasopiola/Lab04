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
        self.passeggeri= []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        if not isinstance(nuovo_nome, str) or nuovo_nome.strip() == "":
            raise ValueError("Nuovo nome non valido: Il nome della crociera deve essere una stringa non vuota.")
        self._nome = nuovo_nome.strip()


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for riga in reader:
                    if not riga:
                        continue
                    codice_cabina = riga[0].strip()

                    #leggo cabine da file

                    if codice_cabina.startswith("CAB"):
                        if len(riga) == 4:
                            codice_cabina, nposti, ponte, prezzo = riga
                            cabina = Cabina(codice_cabina, nposti, ponte, prezzo)
                        elif len(riga) == 5:
                            try:
                                # verifico CabinaAnimale
                                int(riga[4])
                                codice_cabina, nposti, ponte, prezzo, max_animali = riga
                                cabina = CabinaAnimale(codice_cabina, nposti, ponte, prezzo, max_animali)
                            except ValueError:
                                # altrimenti CabinaDeluxe
                                codice_cabina, nposti, ponte, prezzo, stile = riga
                                cabina = CabinaStilosa(codice_cabina, nposti, ponte, prezzo, stile)
                        else:
                            continue
                        self.cabine.append(cabina)
                        print(f" {len(self.cabine)} cabine caricate dal file.")


                    elif codice_cabina.startswith("PAS"):
                        codice_passeggero, nome, cognome = riga
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.passeggeri.append(passeggero)
                        print(f" {len(self.passeggeri)} passeggeri caricati dal file.")

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

