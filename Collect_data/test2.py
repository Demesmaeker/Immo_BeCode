import re
import requests
import lxml.html as lh
import Data
import Functions
import pprint
from bs4 import BeautifulSoup
import csv
import json



bien = Data.estate()




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
