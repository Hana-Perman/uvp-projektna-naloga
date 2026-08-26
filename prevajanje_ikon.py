"""obstajata dve spletni strani, kjer arso opiše kako so sestavljene njihove ikone:
    https://meteo.arso.gov.si/uploads/meteo/help/sl/xml_service.html
    https://meteo.arso.gov.si/uploads/meteo/style/img/weather/meteoSI/ikone.html
Ikone bomo pospravili v slovarje in napisali funkcijo, ki prebere poljubno ikono 
in pove kakšno vreme je napovedano, tako, da so podatki primerni za nadaljno analizo"""

"""opomba: imena ikon so oblike:
    overcast_lightRA """

import re


def prevedi_ikono(ime_ikone):

    oblacnost = {
        "clear": "jasno",
        "mostClear": "pretežno jasno",
        "slightCloudy": "rahlo oblačno",
        "partCloudy": "delno oblačno",
        "modCloudy": "zmerno oblačno",
        "prevCloudy": "pretežno oblačno",
        "overcast": "oblačno",
        "FG": "megla"
    }

    pojavi = {
        "FG": "megla",
        "DZ": "rosenje",
        "FZDZ": "zmrzujoče rosenje",
        "RA": "dež",
        "FZRA": "zmrzujoči dež",
        "RASN": "dež s snegom",
        "SN": "sneg",
        "SHRA": "ploha dežja",
        "SHRASN": "ploha dežja s snegom",
        "SHSN": "snežna ploha",
        "SHGR": "ploha sodre",
        "TS": "nevihta",
        "TSRA": "nevihta z dežjem",
        "TSRASN": "nevihta z dežjem in snegom",
        "TSSN": "nevihta s sneženjem",
        "TSGR": "nevihta s točo"
    }

    jakost = {
        "light": "rahel/-lo/-la",
        "mod": "zmeren/-no/-na",
        "heavy": "močen/-no/-na"
    }

    jakost_vetra = {
        "light": "rahel",
        "mod": "zmeren",
        "heavy": "močan"

    }

    smeri = {
        "N": "sever",
        "W": "zahod",
        "E": "vzhod",
        "S": "jug",
        "NE": "severo-vzhod",
        "NW": "severo-zahod",
        "SE": "jugo-vzhod",
        "SW": "jugo-zahod"
    }

    vreme = re.search(r"([A-Za-z]+)(_([a-z]+)([A-Z]+))?", ime_ikone)

    #prvi primer: ikona je ikona za veter, torej je oblike modN ipd
    #drugi primer: ikona je ikona za vreme je oblike  overcast_lightRA
    

    if "light" in vreme.group(1) or "mod" in vreme.group(1) or "heavy" in vreme.group(1):
       

        ja = re.search(r"([a-z]+)([A-Z]+)",vreme.group(1)).group(1)
        sm = re.search(r"([a-z]+)([A-Z]+)",vreme.group(1)).group(2)
        return f"{jakost_vetra[ja]} {smeri[sm]}"

    else:
        ob = vreme.group(1)
        ja = vreme.group(3)
        po = vreme.group(4)
    
        return f"{oblacnost[ob]} {jakost[ja]} {pojavi[po]}" if ja and po else f"{oblacnost[ob]}"

