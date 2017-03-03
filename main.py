# -*- coding: utf-8 -*-


from BC_Class_Waehrungv3 import Waehrung, AktuelleKurse
from BC_Class_Handelseinheit import Handelseinheit
from BC_Class_Einzelpreis import Einzelpreis
from BC_Class_Artikel_v2 import Artikel


SUPPORTED_CURRENCIES = {
    "EUR": "European euro",
    "USD": "US dollar",
    "GBP": "Pound sterling",
    "BRL": "Brazilian real"
}



print(Waehrung)
# currency code .. ist eine nummer --> String .. kein int
curr_code = int(input("choose preferred currency-code:"))

#curr_code = 2
# suche Waerungsbezeichnung ueber den code  : 1 --> USD
curr = Waehrung[curr_code]
#curr = Waehrung[2]

# Nimm EUR und schaue in dictionary rein ... USD --> Kurs von USD(Key) in EUR
instanz_von_AktuelleKurse = AktuelleKurse()
#print(AktuelleKurse.l[curr])
print(instanz_von_AktuelleKurse.l[curr])

# If KEY ==BaseCurrency -> Calc newcurr -> print new curr