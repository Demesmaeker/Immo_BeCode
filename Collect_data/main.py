from Function import *

base_url = "https://www.immoweb.be/"
search_url = "https://www.immoweb.be/fr/recherche/appartement/a-vendre?countries=BE&isALifeAnnuitySale=false&page=1&orderBy=relevance "
is_firefox = False

driver = init_webdriver()

init_connection(driver, search_url, title="Immoweb", check_button=True)
time.sleep(2)

print(driver)

number_of_pages = driver.find_elements_by_css_selector('div.search-results__header a.pagination__link span.button__label')

print(number_of_pages)

number_of_pages = number_of_pages[2]
number_of_pages = number_of_pages.get_attribute('innerHTML')

print(number_of_pages)

driver.close()
