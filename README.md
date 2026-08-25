# Vreme v slovenskih gorovjih
V projektni nalogi bomo analizirali vreme v slovenskih gorovij. 
Gorovja, ki pridejo v poštev so:

- `"JULIJSKE ALPE"`,
- `"JULIJSKE ALPE / JUGOZAHOD"`,
- `"KAMNIŠKO-SAVINJSKE ALPE"`,
- `"KARAVANKE"`,
- `"POHORJE"`,
- `"SNEŽNIK"`,
- `"ŠKOFJELOŠKO HRIBOVJE"`,
- `"VZHODNOSLOVENSKO HRIBOVJE"`.

## Struktura projektne naloge

```
projektna-naloga/
├── analiza.ipynb
├── README.md
├── datoteka.csv
├── prevajanje_ikon.py
├── pisanje_csv_datoteke.py
├── zajem_podatkov.py
└── urejanji_zapiski_iz_pogovora.pdf
```

## Kako smo pridobili podatke

Pridobivanje poddatkov je bilo postopno. Najprej smo s funkcijami v datoteki `zajem_podatkov` zajeli podatke iz spletnih strani in zajeli tabelo iz teh podatkov s pomočjo `BeautifulSoup`. Nato smo s funkcijo `pisanje_csv_datoteke` podatke zapisali v csv datoteko. Tukaj smo potrebovali pomožno datoteko `prevajanje_ikon`, ki je informacije o vremenu iz standardnega arso formata prevedla v nam berljiv format (podatki o tem kako se ikone sestavljene so dostopni na spletnih straneh navedenih v datotekah). Funkcija `pisanje_csv_datoteke` ustvari csv-datoteko iz zbranih podatkov.

## Kako smo analizirali podatke

Podatki v `datoteka.csv` so strukturirani tako:

```
| ime gorovja | dan meritve      | To 08 CEST      | To 11 CEST      | To 14 CEST    | To 17 CEST      | ...
JULIJSKE ALPE |                  |                 |                 |               |                 | ...
JULIJSKE ALPE |Vreme na 2500 m   |oblačno          |oblačno          | oblačno       | pretežno oblačno| ... 
JULIJSKE ALPE |Vreme na 1500 m   |oblačno          |oblačno          |oblačno        |pretežno oblačno |....
JULIJSKE ALPE |                  |                 |                 |               |                 | ...
JULIJSKE ALPE |Temperatura       |                 |                 |               |                 | ...
JULIJSKE ALPE |na 5500 m         |-9 °C            |-9 °C            |-10 °C         |-9 °C            | ...
...      
JULIJSKE ALPE |na 500 m          |...    
JULIJSKE ALPE |                  |                 |                 |               |                 | ...
JULIJSKE ALPE |Višina ničte izoterme ....    
JULIJSKE ALPE |Meja sneženja...      
JULIJSKE ALPE |                  |                 |                 |               |                 | ...
JULIJSKE ALPE |Veter             |                 |                 |               |                 | ...
JULIJSKE ALPE |na 5500 m         |zmeren jugo-zahod|močan jugo-zahod |zmeren zahod   |zmeren zahod     | ...
JULIJSKE ALPE |hitrost           |49 km/h          |62 km/h          |54 km/         |45 km/h          | ...
...
JULIJSKE ALPE |                  |                 |                 |               | 
JULIJSKE ALPE |Vlažnost          |                 |                 |               | 
JULIJSKE ALPE |na 5500 m         |99 %             |21%              |57%            |78 %             | ...
...      
JULIJSKE ALPE |na 500 m          |...    
JULIJSKE ALPE |                  |                 |                 |               | 
JULIJSKE ALPE |Stabilnost        |stabilno         |rahlo labilno    |labilno        |labilno


```

in tako dalje za vsa gorovja iz zgoraj navedenega seznama.
V datoteki `analiza.ipynb` smo podatke analizirali, s funkcijami navedenimi na začetku datoteke.

## Navodila za uporabo
V kolikor so vse datoteke v isti mapi, uporabnik odpre `analiza.ipynb` in požene run all. V datoteki je klicana funkcija `ustvari_cvs` zato se csv automatično ustvari, v nadaljevanju pa iz narejenega csv-ja beremo podatke in delamo analizo. (`ustvari_csv` je funkcija v `pisanje-csv_datoteke`)


## Viri podatkov
https://meteo.arso.gov.si/met/sl/weather/bulletin/mountain/
