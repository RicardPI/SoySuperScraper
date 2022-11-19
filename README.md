
# Pràctica 1 - Tipologia i cicle de Vida de les Dades   --  SoySuperScraper --

Assignatura: M2.851 / Semestre: 2022-1 / Data: 18-11-2022

URL de la web escollida : https://www.soysuper.com

## Autors
  * Ricard Piqué Inglada - [rpiquei@uoc.edu](email@uoc.edu)
  * Adrià Jaraba Corrius - [ajarabac@uoc.edu](email@uoc.edu)

## Descripció del repositori

Aquest Scrapper entra a la web soysuper.com i extreu els preus d'uns productes prèviament seleccionats de diferents supermercats.
Els supermercats que s'analitzen son:
*  Condis
*  Hipercor
*  El corte Inglés
*  Mercadona
*  Capravo
*  Alcampo
*  Dia

Els productes que s'han seleccionat son productes que els 7 supermercats els tinguin en els seus linials.

Per tal de poder executar l'script, es necesessàri tindre un chromdriver.exe a la carpeta on estigui logalitzat Extraccio_Soy_Super.py
chromedriver -> https://chromedriver.chromium.org/downloads

També, s'han dinstal·lar les llibreries (consultar requirements.txt):

```
pip3 install pandas
pip3 install selenium
pip3 install beautifulsoup4
pip3 install fsspec
pip3 install requests
```
Després per Executar el codi, caldrà el següent codi:

```
python Extraccio_Soy_Super.py
```

  * `memoria.pdf`: Document de respostes.
  * `/src/Extraccio_Soy_Super.py`: Arxiu principal.
  * `/src/requirements.txt`: Llista de paquetes utilitzats (Python 3.7.5).
  * `/dataset/collected_data_1.csv`: Descripción archivo.
  
## Publicació a Zenodo
El dataset s'ha publicat a Zenodo amb DOI [10.5281/zenodo.7337202](https://doi.org/10.5281/zenodo.7337202).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7337202.svg)](https://doi.org/10.5281/zenodo.7337202)

## Vídeo de la presentació

Enllaç del vídeo a la presentació de la pràctica: [https://drive.google.com/...](https://drive.google.com/...)


# Recursos

1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
