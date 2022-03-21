from ostoskori import Ostoskori
from varasto import Varasto
from pankki import Pankki
from viitegeneraattori import Viitegeneraattori

#poistetaan riippuvuuksia, korvataan niitä
from varasto import Varasto as varasto_1
from pankki import Pankki as pankki_1
from viitegeneraattori import Viitegeneraattori as viitegeneraattori_1

class Kauppa:
#väh riippuvaisuuksia määrittelemällä parametrissa)
    def __init__(self, 
        varasto: Varasto=varasto_1,
        pankki:Pankki= pankki_1, 
        viitegeneraattori: Viitegeneraattori=viitegeneraattori_1):

        self._varasto = varasto
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self._varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self._varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        if self._varasto.saldo(id) > 0:
            tuote = self._varasto.hae_tuote(id)
            self._ostoskori.lisaa(tuote)
            self._varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self._viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)
