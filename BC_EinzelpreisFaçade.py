# -*- coding: utf-8 -*-

#### Einzelpreis Façade ####
# import sys


from BC_Class_Waehrungv3 import Waehrung, AktuelleKurse
from BC_Class_Handelseinheit import Handelseinheit
from BC_Class_Einzelpreis import Einzelpreis
from BC_Class_Artikel_v2 import Artikel

print ("Hauptprogramm")
e1 = Einzelpreis ( 13.6, Waehrung.EUR, Handelseinheit.KILOGRAMM )
e2 = Einzelpreis ( 24.0, Waehrung.NOK, Handelseinheit.LITER )
print ( e1 )
print ( e2 )

a1 = Artikel ( "Bioschnaps", 1.89, Waehrung.EUR, Handelseinheit.LITER, 19.0 )
a2 = Artikel ( "Biobananen", 3.59, Waehrung.TRY, Handelseinheit.STUECK, 7.0 )
print ( a1 )
print ( a2 )
