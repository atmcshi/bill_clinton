# -*- coding: utf-8 -*-

from BC_Class_Waehrungv3 import Waehrung, AktuelleKurse
from BC_Class_Handelseinheit import Handelseinheit

class Einzelpreis(object):
    def __init__ ( self, m, w, h ):
        self.menge = m
        self.waehrung = w
        self.handelseinheit = h

    def __str__ ( self ):
        strAusgabe = "| "
        strAusgabe += "%6.2f" % self.menge   #### %06.2f, %05d, %-20s
        strAusgabe += " "
        strAusgabe += "%3s" % self.waehrung
        strAusgabe += "/"
        strAusgabe += "%3s" % self.handelseinheit
        strAusgabe += " |"
        return strAusgabe
