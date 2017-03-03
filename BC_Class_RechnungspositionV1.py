# -*- coding: utf-8 -*-

from BC_Class_Artikel_v2 import Artikel
from BC_Class_Einzelpreis import Einzelpreis
from BC_Class_Waehrungv3 import Waehrung, AktuelleKurse
from BC_Class_Handelseinheit import Handelseinheit
from BC_Class_Artikelgruppev2 import Artikelgruppe

class Rechnungsposition ( object ):

    def __init__ ( self, PosNr, gesamtmenge, einheit, bezeichnung, einzelpreis, waehrung, steuer, artikelgruppe ):
        self.PosNr = PosNr
        self.Gesamtmenge = gesamtmenge
        self.MeinArtikel = Artikel ( bezeichnung, einzelpreis, waehrung, einheit, steuer, artikelgruppe )

    def __str__ ( self ):
        strAusgabe = "| "
        strAusgabe += "%3d" % self.PosNr
        strAusgabe += " |"
        strAusgabe += "%4.1f" % self.gesamtmenge
        strAusgabe += "/ "
        strAusgabe += "%3s" % self.einheit
        strAusgabe += "| "
        strAusgabe += "%-15s" % self.bezeichnung
        strAusgabe += " |"
        strAusgabe += "%6.2f" % self.einzelpreis
        strAusgabe += "/ "
        strAusgabe += "%3s" % self.waehrung
        strAusgabe += " | "
        strAusgabe += "%4.1f%%" % self.steuer
        strAusgabe += "| "
        strAusgabe += "%2s" % self.artikelgruppe
        strAusgabe += " |"

        return strAusgabe
