#link do spletne strani https://meteo.arso.gov.si/met/sl/weather/bulletin/mountain/


import time
from  urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup





def povezava_gorovje(gorovje):
    """Funkcija vrne URL do spletne strani, ki kaže vreme za izbrano gorovje. Url-ji so pospravljeni
    v indeksni tabeli na spletni strani"""
    
    url_indeks = "https://meteo.arso.gov.si/uploads/probase/www/fproduct/text/sl/forecast_si-mountain/upperAir-long-index.html"
    vsebina = requests.get(url_indeks, timeout=10) #funkcija pridobi html iz url-ja
    vsebina.raise_for_status() #preverjamo ali nam bo strežnik vrnil napako

    soup = BeautifulSoup(vsebina.text, "html.parser") #string razčleni v html, to mu povemo s "html.parser"

    for a in soup.find_all("a", href=True): #najde vse linke na spletni strani (ki so v indeksni tabeli)
        href = a["href"]

        if gorovje.lower() in href.lower(): #če povezava, do izbranega gorovja obstaja nam jo funkcija vrne
            return urljoin(url_indeks, a["href"])

    return f"za gorovje {gorovje} ni povezave"
   

def prenos_html_strani(url):
    """Funkcija prenese spletno stran vremena za posamično gorovje. 
    To poskusi trikrat, med poskusi počaka 3s."""

    for i in range (3): #funkcija 3 poskuša pridobiti podatke
        try:

            r = requests.get(url, timeout=10)
            r.encoding = r.apparent_encoding 
            #to je treba dodati, saj se če ne čšž-ji narobe prenesejo


            if r.status_code == 200:    #če je bilo pridobivanje podatkov uspešno
                
                soup = BeautifulSoup(r.text, "html.parser")
                return soup
            else:
                print(f'Strežnik javi napako {r.status_code}')

        except requests.RequestException as e:
            print(f'napaka pri povezavi {e}')

        time.sleep(3)

    return f"prenos neuspešen"

#-----------------------------------ISKANJE TABELE NA SPLETNI STRANI--------------------------------------------

def zajemi_tabelo(soup):
    """posamezna tabela vsebuje le eno tabelo. Funkcija poišče to tabelo."""
    if soup != None:
        tabela = soup.find("table")
        if not tabela:
            return None
        return tabela
    else:
        return f"Soup ni veljaven"


