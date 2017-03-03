# -*- coding: utf-8 -*-

from BC_Class_Einzelpreis import Einzelpreis
from BC_Class_Artikelgruppev2 import Artikelgruppe


class Artikel ( object ):

    def __init__ ( self, bez, menge, waeh, hand, Artikelgruppe, Mwstsatz=0 ):
        Mwstsatz = {"NF" : 7.0, "FD" : 19.0, "AE" : 0.0}
        self.Bezeichnung = bez
        self.MwSt = Mwstsatz(Artikelgruppe)       # rückgabe der werte der artikelgruppe via mwst
        self.Einzelpreis = Einzelpreis ( menge, waeh, hand )

    def __str__ ( self ):
        strAusgabe = "| "
        strAusgabe += self.Bezeichnung
        strAusgabe += " "
        strAusgabe += "%20s" % self.Einzelpreis
        strAusgabe += " "
        strAusgabe += "%4.1f%%" % self.MwSt
        strAusgabe += " |"

        return strAusgabe
