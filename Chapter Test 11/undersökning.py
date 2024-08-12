class AnonymUndersökning:

    def __init__(self, fråga):

        self.fråga = fråga
        self.svaren = []

    def visa_fråga(self):

        print(self.fråga)

    def samla_svaren(self, nya_svar):
        self.svaren.append(nya_svar)

    def visa_resultat(self):

        print("Undersökning resultat:")
        for svar in self.svaren:
            print(f"-{svar}")

    