from bs4 import BeautifulSoup
import requests
import json
import Functions
import Data
import pprint
import shadow_useragent





url = "https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&maxPrice=350000&minPrice=250000&orderBy=relevance"

"""data = Functions.recuperer_data_research_page(url)

print(data)

Functions.collect_data_research_page(data)"""





ua = shadow_useragent.ShadowUserAgent()

# on sélectionne un user-agent assez commun, avec au moins 5% d'utilisateurs
my_user_agent = ua.percent(0.05)

headers = {
    'User-Agent': '{}'.format(my_user_agent),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'fr_FR,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

reponse = requests.get(url, headers=headers)
print(reponse.status_code)
if reponse is not None:
    soup = BeautifulSoup(reponse.text, 'lxml')
    print("***********************************")
    print("+++++++++++++++++++++++++++++++++++++")
    print(reponse.content)

print("ola33")

test = soup.select("div")

print(test)

for i in soup.select("div.search-results__header"):
    print("ola32")
    print(i)


