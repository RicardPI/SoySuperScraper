
#Importació de llibreries necessàries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import requests
import csv
from datetime import datetime
from datetime import timedelta
import bs4
from bs4 import BeautifulSoup
import json
import time
import os

#Creació de funcions necessàries

# Creació de funció que ens dona la posició real a la barra lateral dreta dels supers que hi han
def getRealPositions(cartVersions,PosicionsWeb):
    """ Crea diccionari amb les posicions de cada super actuals"""
    
    tagsTr = cartVersions.find("tbody").find_all("tr")
    posicioSupers=[]
    for i in tagsTr:
        posicioSupers.append(i["data-version"])
    return dict(zip(posicioSupers,PosicionsWeb))

# es crea la funció que extreu tots els preus per a cada super
def extreuPreus(data,supermercat):
    """ Donada data, que es la transformació de l'arxiu json de la web, extreu el nom dels productes 
    a una llista anomenada lnom i extreu els preus unitaris a una llista anomenada lpreu"""
    lnom = []
    lpreu=[]
    for diccionari in data['cart']["items"]:
        if list(diccionari.keys())[0] == 'brand':
            lnom.append(diccionari["name"])
            lpreu.append(diccionari["price"])
    return {supermercat:(lnom,lpreu)}

def CreacioDataFrame(llista_tots_diccionaris):
    """ Donada la llista extreta de tots els diccionaris retorna un dataframe amb tots els 
    preus extrets"""
    columnes=[]
    index = list(llista_tots_diccionaris[0].values())[0][0]
    dates = [datetime.today().strftime("%Y-%m-%d")]*len(index)
    d={"Productes":index,"Data":dates}
    for supers in llista_tots_diccionaris:
        for nom,valors in supers.items():
            columnes.append(nom)
            preus = valors[1]
            d[nom]=preus
    
    df=pd.DataFrame(d)
    
    return df

def getcsv(path,df):
    """ donat df i path crea un csv en aquell directori"""
    df.to_csv(path)


# Obertura de la paàgina soysuper.com
PATH_Casa = os.getcwd()
PATH_Casa = os.path.join(PATH_Casa,"chromedriver.exe")
driver = webdriver.Chrome(executable_path=PATH_Casa)
driver.get("https://soysuper.com/signin")
driver.implicitly_wait(3)
driver.maximize_window()

# ### 1.1 Introducció de l'usuari i contrassenya
time.sleep(2)
username = "adriaricarduoc@gmail.com"
password = "Practica1"
driver.find_element("name","email").send_keys(username)
driver.find_element("name","password").send_keys(password)
driver.find_element("xpath","/html/body/section[1]/section[2]/div[1]/section/section/section/section/section[1]/section/section[2]/form/p[2]/button").click()

# Dades Inicialització

# Path de les posicions de la barra lateral de la web on hi han els supers
PosicionsWeb=["/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[1]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[2]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[3]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[4]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[5]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[6]",
              "/html/body/section/section[2]/div/section/aside[1]/div/div[1]/section/table/tbody/tr[7]"
             ]

# Llista de supers dels quals s'ha de descarregar dades
totsSupers = ["dia","caprabo","alcampo","hipercor","corteingles","mercadona","condis"]
llista_per_fer = totsSupers.copy()

time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
data = json.loads(soup.find('script',{"type": "application/json","id":"app-data"}).text)
supermercat = data["user"]['supermarket']
cartVersions = soup.find("div",{"id":"cartversions"})

#s'extreu un diccionari amb les poscions exactes de la barra lateral dreta
posicions_reals = getRealPositions(cartVersions,PosicionsWeb)

#Path del botó on donem ok a canviar
boto_ok = "/html/body/section/section[2]/div/section/section/section/div/section[1]/p/a"

#inicialització de la llista de diccionaris que conte tots els articles i preus de tots els supers
llista_tots_diccionaris = []

#Comença l'extracció de dades
while len(llista_per_fer)>0:
    driver.refresh()
    time.sleep(10)
    #s'extreu tot el contingut html que hi ha a la web
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    # agafem la part de l'esquerra de la web on sabrem visualment on està cada super
    cartVersions = soup.find("div",{"id":"cartversions"})
    data = json.loads(soup.find('script',{"type": "application/json","id":"app-data"}).text)
    #treiem totes les dades actuals
    llista_tots_diccionaris.append(extreuPreus(data,supermercat))
    #eliminem de la llista per fer el supermercat actual
    llista_per_fer.remove(supermercat)
    if len(llista_per_fer) == 0:
        driver.close()
    else:
        supermercat =llista_per_fer[0]
        #path que s'ha de clicar per anar al següent super
        new_path = getRealPositions(cartVersions,PosicionsWeb)[supermercat]
        #seqüència de botons per anar al següent super
        driver.find_element("xpath",new_path).click()   
        time.sleep(8)
        #scroll up fins a dalt de tot i veure el boto_ok
        driver.find_element("xpath",boto_ok).send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(8)
        driver.find_element("xpath",boto_ok).click()   
        time.sleep(5)


#Creació del Dataset amb data actual
df=CreacioDataFrame(llista_tots_diccionaris)

#Extracció a un arxiu csv al current directory on estiguem treballant
path_actual = os.getcwd()
csvPath = os.path.join(path_actual,"resultats.csv")
df.to_csv(csvPath)