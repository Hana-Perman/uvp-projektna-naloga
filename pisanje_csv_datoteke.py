from zajem_podatkov import *
from prevajanje_ikon import *

from bs4 import BeautifulSoup
import re
from pathlib import Path


def html_v_csv_gorovje(html_tabela):

    """funkcija vzame html-tabelo dobljeno z beautiful soup in je 
    pretvori v zapis primeren za pisanje v csv-datoteko"""

    csv_vrstice = []

    thead = html_tabela.find("thead") #tabela ima samo en t-head zato ne potrebujem find_all
    ime_gorovja = thead.get_text(" ", strip = True) #head vsebuje samo ime gorovja

    tbody = html_tabela.find("tbody")
    vrstice = tbody.find_all("tr")

    #Spodnji del funckije iz celic izlušli tekst. Previdni moramo biti pri link-ih do ikon, saj tam sicer
    #ni besedila vendar se ključni podatki skrivajo v povezavi, do spletne strani z ikono. Vsi linki so enaki, 
    #razlikujejo se samo v imenu slike. S regexom zato izluščimo ime slike.

    for vrsta in vrstice:
        celice = [
            celica.get_text(" ", strip=True).replace(",", "") 
            if not celica.img 
            else prevedi_ikono(re.search(r"\/(\w+)\.png", celica.img["src"]).group(1)) #z regexom izluščimo ime ikone za vreme
            for celica in vrsta.find_all("td")
            ]
        csv_vrstice.append(",".join([ime_gorovja] + celice))

    return "\n".join(csv_vrstice)



def zapis_v_csv(celice):
   
    #pot = Path(__file__).parent / "datotetka.csv" 
    with open ("datoteka.csv","w", encoding="utf-8") as datoteka:
        datoteka.write(celice)

    return


#----------------------GENERIRANJE-CSV-DATOTEKE---------------------------------------------------------------------------------------------------------------
"""ta del programa je namenjen temu, da se sprehodi skozi vsa mozna gorovja za katera arso napoveduje vreme 
in izlušči podatke ter jih shrani v csv"""

def ustvari_csv():

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

    
    csv = ""
    for gorovje in seznam_gorovij:
       
        tabela = zajemi_tabelo(prenos_html_strani(povezava_gorovje(gorovje)))
        csv += html_v_csv_gorovje(tabela)
        csv += "\n"
        #komentar 
        #print(csv)
    zapis_v_csv(csv)

