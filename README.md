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

| JULIJSKE ALPE | Izračun: Sreda 26.08.2026 02 CEST | Sr 08 CEST          | Sr 11 CEST       | Sr 14 CEST                      | Sr 17 CEST                         | Sr 20 CEST       | Sr 23 CEST        | Če 02 CEST        |
|---------------|-----------------------------------|---------------------|------------------|---------------------------------|------------------------------------|------------------|-------------------|-------------------|
| JULIJSKE ALPE | Vreme na 2500 m                   | jasno               | jasno            | delno oblačno rahel/-lo/-la dež | pretežno oblačno rahel/-lo/-la dež | delno oblačno    | oblačno           | jasno             |
| JULIJSKE ALPE | Vreme na 1500 m                   | jasno               | jasno            | delno oblačno rahel/-lo/-la dež | pretežno oblačno rahel/-lo/-la dež | delno oblačno    | oblačno           | jasno             |
| JULIJSKE ALPE | Temperatura                       |                     |                  |                                 |                                    |                  |                   |                   |
| JULIJSKE ALPE | na 5500 m                         | -8 °C               | -8 °C            | -8 °C                           | -8 °C                              | -8 °C            | -8 °C             | -8 °C             |
| JULIJSKE ALPE | na 3000 m                         | 5 °C                | 6 °C             | 7 °C                            | 7 °C                               | 9 °C             | 8 °C              | 8 °C              |
| JULIJSKE ALPE | na 2500 m                         | 9 °C                | 10 °C            | 9 °C                            | 10 °C                              | 11 °C            | 10 °C             | 11 °C             |
|...|
| JULIJSKE ALPE | Višina ničte izoterme             | 3832 m              | 3883 m           | 4086 m                          | 4204 m                             | 4389 m           | 4274 m            | 4244 m            |
| JULIJSKE ALPE | Meja sneženja                     | 3525 m              | 3579 m           | 3750 m                          | 3852 m                             | 4109 m           | 4000 m            | 3984 m            |
| JULIJSKE ALPE | Veter                             |                     |                  |                                 |                                    |                  |                   |                   |
| JULIJSKE ALPE | na 5500 m                         | močan zahod         | zmeren zahod     | močan zahod                     | močan zahod                        | močan zahod      | zmeren zahod      | zmeren zahod      |
| JULIJSKE ALPE | hitrost                           | 55 km/h             | 51 km/h          | 62 km/h                         | 64 km/h                            | 64 km/h          | 42 km/h           | 46 km/h           |
| JULIJSKE ALPE | na 3000 m                         | zmeren severo-zahod | zmeren zahod     | zmeren zahod                    | zmeren zahod                       | zmeren zahod     | rahel zahod       | zmeren jugo-zahod |
| JULIJSKE ALPE | hitrost                           | 18 km/h             | 19 km/h          | 21 km/h                         | 22 km/h                            | 23 km/h          | 17 km/h           | 27 km/h           |
| JULIJSKE ALPE | Vlažnost                          |                     |                  |                                 |                                    |                  |                   |                   |
|...|
| JULIJSKE ALPE | na 5500 m                         | 42 %                | 65 %             | 51 %                            | 49 %                               | 63 %             | 49 %              | 81 %              |
| JULIJSKE ALPE | na 3000 m                         | 64 %                | 60 %             | 79 %                            | 80 %                               | 60 %             | 75 %              | 68 %              |
| JULIJSKE ALPE | na 2500 m                         | 57 %                | 54 %             | 90 %                            | 83 %                               | 67 %             | 74 %              | 77 %              |
|...|
| JULIJSKE ALPE | Stabilnost                        | rahlo labilno       | labilno          | labilno                         | labilno                            | labilno          | labilno           | rahlo labilno     |
|...|


in tako dalje za vsa gorovja iz zgoraj navedenega seznama.
V datoteki `analiza.ipynb` smo podatke analizirali, s funkcijami navedenimi na začetku datoteke.

## Navodila za uporabo
V kolikor so vse datoteke v isti mapi, uporabnik odpre `analiza.ipynb` in požene run all. V datoteki je klicana funkcija `ustvari_cvs` zato se csv automatično ustvari, v nadaljevanju pa iz narejenega csv-ja beremo podatke in delamo analizo. (`ustvari_csv` je funkcija v `pisanje-csv_datoteke`)


## Viri podatkov
https://meteo.arso.gov.si/met/sl/weather/bulletin/mountain/
