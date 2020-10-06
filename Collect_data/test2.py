import re
import requests
import lxml.html as lh
import Data
import Functions
import pprint
from bs4 import BeautifulSoup
import csv
import json
import numpy as np
import pickle
import time
#from Data import pickle_data

#house_data = pickle.load(open('immoweb_1', 'rb'))

house = Data.estate()

print(vars(house))
print(type(vars(house)))

pprint.pprint(vars(house))

"""with open("mypicklefile", "rb") as h:
    house_data = pickle.load(h)

house_data = PickleData.get_data()

    print(house_data)"""
"""
print("****************************")

seconds = time.time()

print(len(house_data))


for i in house_data:
    test = Functions.collect_data_3_immoweb_id(i)
    print("------------------------")
    print(vars(house_data[i]))
    print(seconds - time.time())

    for x in vars(house_data[i]):
        for y in vars(test):
            if x == y and vars(test)[y] != Functions.default:
                if vars(house_data[i])[x] == Functions.default or vars(house_data[i])[x] is None:
                    vars(house_data[i])[x] = vars(test)[y]
                    pickle.dump(house_data, open('immoweb_1', 'wb'))

    print(vars(house_data[i]))
    print("------------------------")
"""

"""for i in house_data:
    print(vars(house_data[i]))"""

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

"""bien = Data.estate()

pprint.pprint(vars(bien))

print(len(vars(bien)))

collone = ""
count = 0

for i in vars(bien):
    if count == 0:
        collone += i

    else :
        collone += "," + i

    count += 1

with open('house_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([collone])

with open('house_detail.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["locality", "type_of_property", "subtype_of_property", "price", "type_of_sale",
                     "number_of_rooms", "house_area", "fully_equipped_kitchen", "furnished", "open_fire",
                     "terrace", "terrace_area", "garden", "garden_area", "surface_of_the_land",
                     "surface_of_the_plot_of_land", "number_of_facades", "swimming_pool",
                     "state_of_the_building", "construction_year"])

print(collone)

print(Functions.house_data)"""
Functions.colect_data_research_page(min=1, max=50000, type_de_bien="house")
Functions.colect_data_research_page(min=1, max=50000, type_de_bien="apartment")


#Functions.collect_data_3_immoweb_id(8826466)


"""

permet de parcourir toutes les pages de recherche imoweb

"""

# Functions.colect_data_research_page()



"""


A ressoudre :

comment faire pour gérer l'actualisation des données sur immoweb.
    - date de modification sur immoweb ??

"""
# Functions.collect_data_1_tr_collect(8899851, bien) ==> extraction des données d'un tableau
"""
min = 50001
max = 100000
sequences = 1
page = 1
type_de_bien = "appartement"

print(str(sequences) + ' : ' + str(page))

url = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
      + str(min) + '&maxPrice=' + str(max) + '&page=' + str(page) + '&orderBy=relevance'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

data = json.loads(soup.find('iw-search')[':results'])

for d in data:
    url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])"""

    # vérifier que la donnée n'a pas déjà été enregistrée















# print(getattr(maison, detail))
