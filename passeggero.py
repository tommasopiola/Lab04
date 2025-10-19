class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.cabina_assegnata = None

    def assegna_cabina(self, cabina):
        """Assegna una cabina al passeggero"""
        self.cabina_assegnata = cabina

    def __str__(self):
        if self.cabina_assegnata is not None:
            return f"{self.codice_passeggero} - {self.nome} {self.cognome} → Cabina {self.cabina_assegnata}"
        else:
            return f"{self.codice_passeggero} - {self.nome} {self.cognome} → Nessuna cabina"
