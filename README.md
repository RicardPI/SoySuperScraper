
# SoySuperScraper

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
pip3 isntall selenium
pip3 install beautifulsoup4
pip3 install fsspec
pip3 install requests
```
Després per Executar el codi, caldrà el següent codi:

```
python Extraccio_Soy_Super.py
```
# Recursos

1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.


