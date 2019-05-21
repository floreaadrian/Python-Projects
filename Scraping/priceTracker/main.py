# import what we needs
import requests
import bs4
import os
import errno
import csv
from domain import Product, writeToFile, createSites
from datetime import date

#sites = ["https://altex.ro/gaming-jocuri-jucarii/xbox-one/console/", "https://altex.ro/gaming-jocuri-jucarii/playstation-4/console",
      #   "https://www.emag.ro/console-hardware/filter/platforma-f7609,xbox-one-v-4421000/c",
       #  "https://www.emag.ro/console-hardware/filter/platforma-f7609,playstation-4-v-4421003/c"]


xbox = []
ps4 = []

def runPrice():
    produse = []
    f = open("sites.txt","r")
    line = f.readline().strip()
    while line != "":
        produse.append(line)
        line = f.readline().strip()
    f.close()
    sites = createSites(produse)
    sites.append("https://altex.ro/gaming-jocuri-jucarii/xbox-one/console/")
    sites.append("https://altex.ro/gaming-jocuri-jucarii/playstation-4/console")
    sites.append("https://www.emag.ro/console-hardware/filter/platforma-f7609,xbox-one-v-4421000/c")
    sites.append("https://www.emag.ro/console-hardware/filter/platforma-f7609,playstation-4-v-4421003/c")
    for i in sites:
        print(i)
        res = requests.get(i)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        # produsele de pe altex
        if 'altex' in i:
            product = soup.findAll('div', class_='Product')
            for k in product:
                title = k.findAll('div', class_='Product-photoWrapper')
                nume = ""
                link = ""
                price = k.findAll('div', class_='Product-list-right')
                pret = 0
                # daca are produsul reducere o sa aiba o alta clasa asa ca cautam aici
                for k1 in price:
                    price2 = k1.findAll('div', class_='Price Price--discount')
                    for k2 in price2:
                        price3 = k2.findAll('meta')
                        for k3 in price3:
                            if(k3['content'] != "RON"):
                                pret = float(k3['content'])
                for k1 in price:
                    price2 = k1.findAll('div', class_='Price')
                    for k2 in price2:
                        price3 = k2.findAll('meta')
                        for k3 in price3:
                            if(k3['content'] != "RON"):
                                pret = float(k3['content'])
                for j in title:
                    nume = j.a['title']
                    link = j.a['href']
                pret = int(pret)
                if "consola" in nume or "Consola" in nume:
                    if "Xbox" in nume or "XBOX" in nume:
                        xbox.append(Product("Altex", nume, link, pret))
                    else:
                        ps4.append(Product("Altex", nume, link, pret))
        else:
            product = soup.findAll('div', class_='card-item js-product-data')
            for k in product:
                nume = k['data-name']
                pret = 0
                first = k.find('div', class_='card')
                second = first.find(
                    'div', class_='card-section-wrapper js-section-wrapper')
                third = second.find('div', class_='card-section-top')
                first = third.find('div', class_='card-heading')
                link = first.a['href']
                first = second.find('div', class_='card-section-btm')
                second = first.findAll('div', class_='card-body')
                newP = second[1].find('p', class_='product-new-price')
                pret = newP.text.split()[0]
                if pret == "de":
                    pret = newP.text.split()[2]
                pret = float(pret)*1000
                pret = int(pret)
                if "consola" in nume or "Consola" in nume:
                    if "Xbox" in nume or "XBOX" in nume:
                        xbox.append(Product("Emag", nume, link, pret))
                    else:
                        ps4.append(Product("Emag", nume, link, pret))
def mainD():
    print(len(xbox), len(ps4))
    st = ""
    for i in ps4:
        k = '|||'.join(i.toList())
        k += '\n'
        st += k
    ps4File = "all/ps4/"+str(date.today())+".csv"
    xboxFile = "all/xbox/"+str(date.today())+".csv"
    writeToFile(ps4File, st)
    st = ""
    for i in xbox:
        k = '|||'.join(i.toList())
        k += '\n'
        st += k
    writeToFile(xboxFile, st)

mainD()
