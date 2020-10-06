from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os




chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&isALifeAnnuitySale=false&page=1&orderBy=relevance")

number_of_pages = driver.find_elements_by_css_selector('div.search-results__header a.pagination__link span.button__label')

print(number_of_pages)

number_of_pages = number_of_pages[2]
number_of_pages = number_of_pages.get_attribute('innerHTML')

print(number_of_pages)

driver.close()


