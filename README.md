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

## Cilj projektne naloge
V projetkni nalogi si poskušamo z analizo podatkov o vremenu ustvariti predstavo o tem, kakšne vremenske razmere lahko pričakujemo in kako se le-te spreminjajo časovno in z nadmorsko višino ali še kako drugače. 

## Struktura projektne naloge

```
projektna-naloga/
├── analiza.ipynb
├── README.md
├── prevajanje_ikon.py
├── pisanje_csv_datoteke.py
├── zajem_podatkov.py
├── vremenska_napoved.csv
├── temperatura.csv
├── vlaga.csv
├── veter.csv
└── urejanji_zapiski_iz_pogovora.pdf
```

## Kako smo pridobili podatke

Pridobivanje poddatkov je bilo postopno. Najprej smo s funkcijami v datoteki `zajem_podatkov` zajeli podatke iz spletnih strani in zajeli tabelo iz teh podatkov s pomočjo `BeautifulSoup`. Nato smo s funkcijo `pisanje_csv_datoteke` podatke zapisali v csv datoteko. Tukaj smo potrebovali pomožno datoteko `prevajanje_ikon`, ki je informacije o vremenu iz standardnega arso formata prevedla v nam berljiv format (podatki o tem kako se ikone sestavljene so dostopni na spletnih straneh navedenih v datotekah). Funkcija `pisanje_csv_datoteke` ustvari csv-datoteko iz zbranih podatkov.

## Kako smo analizirali podatke

Podatki v `vremenska_napoved.csv` so strukturirani tako:

| Gorovje                 | Izračun: Nedelja 06.09.2026 02 CEST | Ne 08 CEST     | Ne 11 CEST     | Ne 14 CEST     | Ne 17 CEST     | Ne 20 CEST | Ne 23 CEST       | Po 02 CEST | Po 05 CEST     | To 11 CEST     |
|-------------------------|-------------------------------------|----------------|----------------|----------------|----------------|------------|------------------|------------|----------------|----------------|
| JULIJSKE ALPE           | Vreme na 2500 m                     | oblačno        | pretežno jasno | pretežno jasno | jasno          | jasno      | jasno            | jasno      | pretežno jasno | pretežno jasno |
| JULIJSKE ALPE           | Vreme na 1500 m                     | oblačno        | pretežno jasno | pretežno jasno | jasno          | jasno      | jasno            | jasno      | pretežno jasno | pretežno jasno |
| KAMNIŠKO-SAVINJSKE ALPE | Vreme na 2500 m                     | pretežno jasno | delno oblačno  | delno oblačno  | pretežno jasno | jasno      | jasno            | jasno      | pretežno jasno | pretežno jasno |
| KAMNIŠKO-SAVINJSKE ALPE | Vreme na 1500 m                     | pretežno jasno | delno oblačno  | delno oblačno  | pretežno jasno | jasno      | jasno            | jasno      | pretežno jasno | pretežno jasno |
| POHORJE                 | Vreme na 1500 m                     | pretežno jasno | pretežno jasno | pretežno jasno | jasno          | jasno      | pretežno oblačno | jasno      | jasno          | jasno          |
| SNEŽNIK                 | Vreme na 1500 m                     | jasno          | jasno          | jasno          | jasno          | jasno      | jasno            | jasno      | jasno          | jasno          |


Podatki v `temperatura.csv`,`vlaga.csv` in `veter.csv` so strukturirani podobno. Za primer vzemimo `temperatura.csv` :

| Gorovje                 | Izračun: Nedelja 06.09.2026 02 CEST | Ne 08 CEST | Ne 11 CEST | Ne 14 CEST | Ne 17 CEST | Ne 20 CEST | Ne 23 CEST | Po 02 CEST | Po 05 CEST | Po 08 CEST |
|-------------------------|-------------------------------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| JULIJSKE ALPE           | na 5500 m                           | -5 °C      | -5 °C      | -4 °C      | -5 °C      | -5 °C      | -5 °C      | -6 °C      | -7 °C      | -7 °C      |
| JULIJSKE ALPE           | na 3000 m                           | 5 °C       | 6 °C       | 6 °C       | 7 °C       | 8 °C       | 8 °C       | 9 °C       | 10 °C      | 10 °C      |
| JULIJSKE ALPE           | na 2500 m                           | 8 °C       | 8 °C       | 8 °C       | 9 °C       | 10 °C      | 10 °C      | 10 °C      | 12 °C      | 12 °C      |
| JULIJSKE ALPE           | na 2000 m                           | 10 °C      | 9 °C       | 12 °C      | 13 °C      | 13 °C      | 13 °C      | 13 °C      | 13 °C      | 13 °C      |
| JULIJSKE ALPE           | na 1500 m                           | 12 °C      | 13 °C      | 17 °C      | 18 °C      | 17 °C      | 16 °C      | 15 °C      | 14 °C      | 14 °C      |
| JULIJSKE ALPE           | na 1000 m                           | 15 °C      | 17 °C      | 20 °C      | 22 °C      | 20 °C      | 19 °C      | 18 °C      | 17 °C      | 17 °C      |
| JULIJSKE ALPE           | na 500 m                            | 19 °C      | 20 °C      | 24 °C      | 25 °C      | 23 °C      | 22 °C      | 21 °C      | 20 °C      | 20 °C      |
| KAMNIŠKO-SAVINJSKE ALPE | na 5500 m                           | -5 °C      | -5 °C      | -5 °C      | -4 °C      | -5 °C      | -5 °C      | -6 °C      | -7 °C      | -7 °C      |
...
| KARAVANKE               | na 5500 m                           | -5 °C      | -5 °C      | -5 °C      | -5 °C      | -5 °C      | -5 °C      | -6 °C      | -7 °C      | -7 °C      |
 ...


in tako dalje za vsa gorovja iz zgoraj navedenega seznama.
V datoteki `analiza.ipynb` smo podatke analizirali, s funkcijami navedenimi na začetku datoteke.

## Navodila za uporabo
V kolikor so vse datoteke v isti mapi, uporabnik odpre `analiza.ipynb` in požene run all. V datoteki je klicana funkcija `ustvari_cvs` zato se csv automatično ustvari, v nadaljevanju pa iz narejenega csv-ja beremo podatke in delamo analizo. (`ustvari_csv` je funkcija v `pisanje-csv_datoteke`)


## Viri podatkov
https://meteo.arso.gov.si/met/sl/weather/bulletin/mountain/
