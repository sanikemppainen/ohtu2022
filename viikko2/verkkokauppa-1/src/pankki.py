from kirjanpito import Kirjanpito

from kirjanpito import kirjanpito as kirjanpito_1

class Pankki:
    def __init__(self,kirjanpito: Kirjanpito=kirjanpito_1):
        self._kirjanpito=kirjanpito

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True
pankki=Pankki()