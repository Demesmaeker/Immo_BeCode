
import json
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

import Data

maison = Data.estate()

type_de_bien = "appartement"


def url_scrapper(type_de_bien):
    """
    A faire : avec selenium, rechercher le nombre de page maximum pour éviter d'interroger le site innutilement


    """
    min = 50001
    max = 100000
    sequences = 1
    pages = np.arange(1, 333) # comment faire pour retrouver les span ? ce qui permet de récupérer le nbr de page

    while max < 600000:

        for page in pages:

            print(str(sequences) + ' : ' + str(page))

            url = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
                  + str(min) + '&maxPrice=' + str(max) + '&page=' + str(page) + '&orderBy=relevance'

            soup = BeautifulSoup(requests.get(url).content, 'html.parser')

            data = json.loads(soup.find('iw-search')[':results'])

            for d in data:
                url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

                # vérifier que la donnée n'a pas déjà été enregistrée ?

                with open('scrap_immoweb_1.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([url])

        min += 50000
        max += 50000
        sequences += 1

    min = 600000
    max = 100000000

    for page in pages:

        print(str(sequences) + ' : ' + str(page))

        url = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
              + str(min) + '&maxPrice=' + str(max) + '&page=' + str(page) + '&orderBy=relevance'

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        data = json.loads(soup.find('iw-search')[':results'])

        for d in data:
            url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

            # vérifier que la donnée n'a pas déjà été enregistrée

            with open('scrap_immoweb_1.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url])