import re
import csv

from zajem_podatkov import *
from prevajanje_ikon import  prevedi_ikono


def html_v_csv_gorovje(html_tabela):
    """HTML tabelo pretvori v zapis, primeren za pisanje v CSV."""

    csv_vrstice = []

    # Ime gorovja dobimo iz thead
    thead = html_tabela.find("thead")
    ime_gorovja = thead.get_text(" ", strip=True)

    # Vse vrstice so v tbody
    tbody = html_tabela.find("tbody")
    vrstice = tbody.find_all("tr")

    # PRVA vrstica tbody je glava s časovnimi podatki
    prva_vrstica = vrstice[0]

    glava = [celica.get_text(" ", strip=True) for celica in prva_vrstica.find_all("td")]
    if glava[0].startswith("Izračun:"): 
        glava[0] = glava[0].replace(",", "", 1)

    # Na začetek dodamo ime gorovja
    glava = [ime_gorovja] + glava

    # Ostale vrstice pretvorimo v podatke
    for vrsta in vrstice[1:]:
        celice = []
        for celica in vrsta.find_all("td"):
            if celica.img:
                pot = celica.img["src"]
                zadetek = re.search(r"/(\w+)\.png", pot)
                if zadetek:
                    vrednost = prevedi_ikono(zadetek.group(1))
                else:
                    vrednost = ""
            else:
                vrednost = celica.get_text(" ", strip=True).replace(",", "")
            celice.append(vrednost)

        # Na začetek vsake podatkovne vrstice dodamo ime gorovja
        celice = [ime_gorovja] + celice
        csv_vrstice.append(celice)

    return glava, csv_vrstice


def zapis_v_csv(ime_datoteke, celice, glava):

    with open (ime_datoteke,"w", encoding="utf-8", newline="") as datoteka:
        pisec = csv.writer(datoteka) 
        pisec.writerow(glava) 

        for vrstica in celice: 
            pisec.writerow(vrstica)



# GENERIRANJE-CSV-DATOTEKE
# ta del programa je namenjen temu, da se sprehodi skozi
# vsa mozna gorovja za katera arso napoveduje vreme
# in izlušči podatke ter jih shrani v csv

def ustvari_csv_je():

    seznam_gorovij = [
        "JULIAN-ALPS",
        "JULIAN-ALPS_SOUTH-WEST",
        "KAMNIK-SAVINJA-ALPS",
        "KARAVANKE-ALPS",
        "POHORJE",
        "SNEZNIK",
        "SKOFJELOSKO-HRIBOVJE",
        "EAST-MOUNTAINS"
    ]

    vsi_podatki = []
    glava = None

    for gorovje in seznam_gorovij:
        tabela = zajemi_tabelo(prenos_html_strani(povezava_gorovje(gorovje)))
        trenutna_glava, besedilo = html_v_csv_gorovje(tabela)

        if glava is None: 
            glava = trenutna_glava

        vsi_podatki.extend(besedilo)
        
    # Razdelimo podatke na podatke o vremenu, podatke o temperaturi, podatke o vetru in podatke o vlagi
    temperatura = []
    vlaga = []
    veter = []
    vreme = []

    # DOLOČIMO, V KATEREM ODSEKU SMO
    odsek = None 
    for vrstica in vsi_podatki: 
        # Vrstica je prazna, ko ima poleg imena gorovja samo prazne celice. 
        prazna_vrstica = all( celica == "" for celica in vrstica[1:] ) 

        if prazna_vrstica: 
            odsek = None 
            continue 

        # ZAČETEK POSAMEZNEGA ODSEKA
        if len(vrstica) > 1:
            if vrstica[1] == "Temperatura":
                odsek = "temperatura"
                continue
            elif vrstica[1] == "Vlažnost":
                odsek = "vlaga"
                continue
            elif vrstica[1] == "Veter":
                odsek = "veter"
                continue
            elif vrstica[1].startswith("Vreme"):
                odsek = "vreme"

            # SHRANJEVANJE PODATKOV V PRAVILEN SEZNAM
            if odsek == "temperatura":
                temperatura.append(vrstica)
            elif odsek == "vlaga":
                vlaga.append(vrstica)
            elif odsek == "veter":
                veter.append(vrstica)
            elif odsek == "vreme":
                vreme.append(vrstica)

    
    # ZAPIS V ŠTIRI CSV DATOTEKE
    # imena stolpcev
    glava_temperatura = (["Gorovje"] + glava[1:])
    glava_veter = (["Gorovje"] + glava[1:])
    glava_vlaga = (["Gorovje"] + glava[1:])
    glava_vreme = (["Gorovje"] + glava[1:])

    zapis_v_csv( "temperatura.csv", temperatura, glava_temperatura )
    zapis_v_csv( "vlaga.csv", vlaga, glava_vlaga )
    zapis_v_csv( "veter.csv", veter, glava_veter )
    zapis_v_csv( "vremenska_napoved.csv", vreme, glava_vreme )
