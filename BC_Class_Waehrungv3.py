# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from urllib.request import urlopen


Waehrung = { 1 : "EUR",
            2: "USD",
            3: "NOK",
            4: "HUF",
            5: "TRY",
            }

# get + parse währung + move into dict l

class AktuelleKurse(object):

 #   l = {}                              # new dict for currencies

    def __init__ (self, waehrung = Waehrung):

        self.l = {}

        root = ET.parse(urlopen('http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')).getroot()   # open url and parse xml

        #w = Waehrung()

        for child in root[2][0]:
            #print child.tag
            #print child.attrib
            curr = child.get('currency')
            rate = child.get('rate')

            # if curr == w.USD or curr == w.NOK or curr == w.TRY  or curr == w.HUF :  #  grab relevant currencies
            if curr in waehrung.values(): #  grab relevant currencies
               self.l.update({curr : rate})

    def __str__( self ):
        strOutput = ""
        lvalues = self.l.values()
        for element in lvalues:
            strOutput += element+", "
        return strOutput

#print(l["USD"])
#print(l["NOK"])
#print(l["TRY"])
#print(l["HUF"])

#ak = AktuelleKurse()
#print (ak)


# dieAndereWaehrung

        def umrechnen ( self, basiswaehrung, newcurr ):

            self.newcurr = float()
            self.basiswaehrung = ["EUR"]
            newcurr = basiswaehrung * ["USD"]
            print(newcurr)
