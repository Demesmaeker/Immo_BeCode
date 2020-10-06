import re
import requests
import lxml.html as lh
import pprint
from bs4 import BeautifulSoup
import json
import Data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
from datetime import date
import pickle


"""valeur par defaut = la valeur n'a pas été trouvée"""

default = "Not found"


# pour afficher ce qui se passe lors du dev


debug = False

# première fois :
#house_data = {}
# ensuite

#house_data = pickle.load(open('immoweb_1', 'rb'))

def get_str_from_req_content(pattern, fct_content):
    """
    permet d'utiliser les regex pour sortir des données
    """
    if not pattern:
        return None

    print(str(pattern))

    prog = re.compile(pattern)
    fstr = prog.search(str(fct_content))

    return fstr

def recuperer_tr_tag(immmoweb_id):
    """
    permet de récupérer les informations contenue dans le tableau d'une page immoweb à partir de l'id du bien
    """

    url = "https://www.immoweb.be/en/classified/" + str(immmoweb_id)

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url)

    if page.status_code == 200:

        # Store the contents of the website under doc
        doc = lh.fromstring(page.content)

        # Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')

        el = []

        for tr in tr_elements:
            name = tr.text_content()
            el.append(name)

        dico = {}

        for item in el:

            items = list(filter(None, map(str.strip, item.split("\n"))))

            try:
                dico[items[0]] = items[1]

            except IndexError:

                continue

        return dico

    else:
        return "url not reachable"


def collect_data_1_tr_collect(immmoweb_id, maison):
    """
    Récupère les données sur immoweb à partir des tableaux de la page
    """
    dico = recuperer_tr_tag(immmoweb_id)

    if dico == "url not reachable":
        maison.removed_from_immoweb = True
        maison.update_date = date.today()
        if debug:
            print("la page n'est pas accessible")
            print(dico)

    else:
        maison.available_date = dico.get("Available date", default)
        maison.property_name = dico.get("Property name", default)
        maison.neighbourhood = dico.get("Neighbourhood or locality", default)
        maison.construction_year = dico.get("Construction year", default)
        maison.floor = dico.get("Floor", default)
        maison.nbr_floor = dico.get("Number of floors", default)
        maison.state_of_the_building = dico.get("Building condition", default)
        maison.street_facade_width = dico.get("Street facade width", default)
        maison.nbr_facades = dico.get("Facades", default)
        maison.covered_parking_spaces = dico.get("Covered parking spaces", default)
        maison.outdoor_parking_spaces = dico.get("Outdoor parking spaces", default)
        maison.house_area = dico.get("Living area", default)
        maison.living_room_surface = dico.get("Living room surface", default)
        maison.kitchen_type = dico.get("Kitchen type", default)
        maison.nbr_bedrooms = dico.get("Bedrooms", default)
        maison.bedroom_1_surface = dico.get("Bedroom 1 surface", default)
        maison.bedroom_2_surface = dico.get("Bedroom 2 surface", default)
        maison.bedroom_3_surface = dico.get("Bedroom 3 surface", default)
        maison.bedroom_4_surface = dico.get("Bedroom 4 surface", default)
        maison.bedroom_5_surface = dico.get("Bedroom 5 surface", default)
        maison.nbr_bathrooms = dico.get("Bathrooms", default)
        maison.nbr_shower = dico.get("Shower rooms", default)
        maison.nbr_toilet = dico.get("Toilets", default)
        maison.office_surface = dico.get("Office surface", default)
        maison.office = dico.get("Office", default)
        maison.work_space_surface = dico.get("Work space surface", default)
        maison.cellar = dico.get("Basement", default)
        maison.attic = dico.get("Attic", default)
        maison.surface_of_the_land = dico.get("Surface of the plot", default)
        maison.sewer_network = dico.get("Connection to sewer network", default)
        maison.terrace_area = dico.get("Terrace surface", default)
        maison.energy_consumption = dico.get("Primary energy consumption", default)
        maison.energy_class = dico.get("Energy class", default)
        maison.co2_emission = dico.get("CO² emission", default)
        maison.heating_type = dico.get("Heating type", default)
        maison.solar_panels = dico.get("Thermic solar panels", default)
        maison.double_glazing = dico.get("Double glazing", default)
        maison.flood_zone = dico.get("Flood zone type", default)
        maison.price = dico.get("Price", default)
        maison.cadastral_income = dico.get("Cadastral income", default)
        maison.agent = dico.get("Website", default)

    if debug:
        print("*******************************************************")
        print("Ce qui a été trouvé sur immoweb : ")
        print("")
        print(dico)
        print("")
        print("*******************************************************")
        print("Résultat du scrapping : ")
        print("")
        remove_not_found = vars(maison).copy()
        for i in vars(maison):
            if vars(maison)[i] == default:
                del remove_not_found[i]

        pprint.pprint(remove_not_found)

    return maison

def recuperer_data_research_page(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    result = soup.find_all('div')

    data = json.loads(soup.find('iw-search')[':results'])

    return data

def collect_data_2_research_page(d):
    if debug:

        print(d)

        url = "https://www.immoweb.be/en/classified/" + str(d.get("id"))

        print(url)

    maison = Data.estate()

    maison.immoweb_id = d.get("id", default)


    if d.get("cluster", default) != default:
        maison.min_price = d["cluster"].get("minPrice", default)
        maison.max_price = d["cluster"].get("maxPrice", default)
        maison.min_room = d["cluster"].get("minRoom", default)
        maison.max_room = d["cluster"].get("maxRoom", default)
        maison.min_surface = d["cluster"].get("minSurface", default)
        maison.max_surface = d["cluster"].get("maxSurface", default)

        if d["cluster"].get("projectInfo", default) != default \
                and d["cluster"].get("projectInfo", default) is not None:
            maison.constructor = d["cluster"]["projectInfo"].get("constructor", default)
            maison.groupId = d["cluster"]["projectInfo"].get("groupId", default)
            maison.phase = d["cluster"]["projectInfo"].get("phase", default)
            maison.project_name = d["cluster"]["projectInfo"].get("projectName", default)
            maison.delivery_date = d["cluster"]["projectInfo"].get("deliveryDate", default)
            maison.sold_percentage = d["cluster"]["projectInfo"].get("soldPercentage", default)
            maison.units_display_mode = d["cluster"]["projectInfo"].get("unitsDisplayMode", default)

    maison.bedroom_range = d.get("bedroomRange", default)
    maison.surface_range = d.get("surfaceRange", default)
    maison.customer_name = d.get("customerName", default)

    if d.get("property", default) != default:
        maison.type_of_property = d["property"].get("type", default)
        maison.subtype_of_property = d["property"].get("subtype", default)
        maison.nbr_bedrooms = d["property"].get("bedroomCount", default)
        maison.title = d["property"].get("title", default)

        if d["property"].get("location", default) != default \
                and d["property"].get("location", default) is not None:
            maison.country = d["property"]["location"].get("country", default)
            maison.region = d["property"]["location"].get("region", default)
            maison.province = d["property"]["location"].get("province", default)
            maison.district = d["property"]["location"].get("district", default)
            maison.locality = d["property"]["location"].get("locality", default)
            maison.postal_code = d["property"]["location"].get("postalCode", default)
            maison.street_name = d["property"]["location"].get("street", default)
            maison.house_number = d["property"]["location"].get("number", default)
            maison.house_box = d["property"]["location"].get("box", default)
            maison.property_name = d["property"]["location"].get("propertyName", default)
            maison.floor = d["property"]["location"].get("floor", default)
            maison.latitude = d["property"]["location"].get("latitude", default)
            maison.longitude = d["property"]["location"].get("longitude", default)
            maison.approximated = d["property"]["location"].get("approximated", default)
            maison.region_code = d["property"]["location"].get("regionCode", default)
            maison.type = d["property"]["location"].get("type", default)
            maison.has_sea_view = d["property"]["location"].get("hasSeaView", default)
            maison.points_of_interest = d["property"]["location"].get("pointsOfInterest", default)
            maison.place_name = d["property"]["location"].get("placeName", default)

        maison.net_habitable_surface = d["property"].get("netHabitableSurface", default)
        maison.room_count = d["property"].get("roomCount", default)
        maison.surface_of_the_land = d["property"].get("landSurface", default)

    if d.get("transaction", default) != "not found":
        maison.certificate = d["transaction"].get("certificate", default)
        maison.type_of_sale = d["transaction"].get("type", default)
        maison.rental = d["transaction"].get("rental", default)

        if d["transaction"].get("sale", default) != default \
                and d["transaction"].get("sale", default) is not None:
            maison.life_annuity = d["transaction"]["sale"].get("lifeAnnuity", default)
            maison.has_starting_price = d["transaction"]["sale"].get("hasStartingPrice", default)
            maison.old_price = d["transaction"]["sale"].get("oldPrice", default)
            maison.price = d["transaction"]["sale"].get("price", default)
            maison.price_per_sqm = d["transaction"]["sale"].get("pricePerSqm", default)
            maison.public_sale = d["transaction"]["sale"].get("publicSale", default)
            maison.to_build = d["transaction"]["sale"].get("toBuild", default)
            maison.vat_type = d["transaction"]["sale"].get("vatType", default)

    maison.price_type = d.get("priceType", default)
    maison.has_360_tour = d.get("has360Tour", default)

    if debug:

        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

        remove_not_found = vars(maison).copy()
        for i in vars(maison):
            if vars(maison)[i] == default or vars(maison)[i] is None:
                del remove_not_found[i]

        pprint.pprint(remove_not_found)
        """for f in d:
             pprint.pprint(d[f])"""

    return maison

def number_of_immoweb_page(url):
    # fonctionne avec Chrome

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    number_of_pages = driver.find_elements_by_css_selector(
        'div.search-results__header a.pagination__link span.button__label')

    number_of_pages = number_of_pages[2]
    number_of_pages = number_of_pages.get_attribute('innerHTML')

    driver.close()

    return int(number_of_pages)

def intermediate_colect_data(type_de_bien, min, max, page):
    url = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
          + str(min) + '&maxPrice=' + str(max) + '&page=' + str(page) + '&orderBy=relevance'

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    data = json.loads(soup.find('iw-search')[':results'])

    for d in data:
        maison = collect_data_2_research_page(d)

        if maison.immoweb_id not in house_data:

            maison.update_date = date.today()
            house_data[int(maison.immoweb_id)] = maison
            print(house_data)
            #pickle.dump(house_data, open('immoweb_1', 'wb'))

    # enregistrer la donnée


def colect_data_research_page(min = 1,
                              max = 50000,
                              type_de_bien = "house"):
    while max < 600000:

        url_for_pages = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
                        + str(min) + '&maxPrice=' + str(max) + '&orderBy=relevance'

        pages = np.arange(1, number_of_immoweb_page(url_for_pages))

        for page in pages:

            intermediate_colect_data(type_de_bien, min, max, page)

                # vérifier que la donnée n'a pas déjà été enregistrée ?

        min += 50000
        max += 50000

    url_for_pages = 'https://www.immoweb.be/fr/recherche/' + type_de_bien + '/a-vendre?countries=BE&minPrice=' \
                    + str(min) + '&maxPrice=' + str(max) + '&orderBy=relevance'

    pages = np.arange(1, number_of_immoweb_page(url_for_pages))

    max = 100000000

    for page in pages:

        intermediate_colect_data(type_de_bien, min, max, int(page))

            # vérifier que la donnée n'a pas déjà été enregistrée ?
            # enregistrer la donnée

def collect_data_3_immoweb_id(immoweb_id):

    maison = Data.estate()

    url = "https://www.immoweb.be/en/classified/" + str(immoweb_id)

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # We only retrieve the content of the script tag
    al = []
    for p in soup.html.find_all():
        for n in p:
            if n.name == "script":
                al.append(str(n))

    # Données JSON:
    x = al[0]

    x = x.replace("<script>", "")
    x = x.replace("window.dataLayer = [", "")
    x = x.replace("];", "")
    x = x.replace("</script>", "")
    x = ' '.join(x.split())

    # parse x:
    y = json.loads(x)

    if debug: print(pprint.pprint(y))

    # récupération des informations présentent dans le premier script :

    if y.get("classified", default) != default:
        maison.attic = y["classified"].get("atticExists", default)
        maison.cellar = y["classified"].get("basementExists", default)
        maison.price = y["classified"].get("price", default)
        maison.transaction_type = y["classified"].get("transactionType", default)

    if y.get("customer", default) != default:
        maison.customer_type = y["customer"].get("family", default)
        maison.customer_name = y["customer"].get("name", default)

    # récupération des informations présentent dans le second script :
    # attention certaines sont présentent dans les 2 scripts, seuls celles du second sont gardées

    x = al[len(al) - 1]

    x = x.replace("<script type=\"text/javascript\">", "")
    x = x.replace("window.classified = ", "")
    x = x.replace(";", "")
    x = x.replace("</script>", "")
    x = ' '.join(x.split())

    y = json.loads(x)

    if debug : print(pprint.pprint(y))

    # n'a pas été pris en compte de "flags" et d'autres infos plus générales.

    if y.get("price", default) != default:
        maison.old_price = y["price"].get("oldValue", default)
        maison.type_of_sale = y["price"].get("type", default)

    maison.price_type = y["priceType"]

    if y.get("property", default) != default:

        if y["property"].get("attic", default) != default and y["property"].get("attic", default) is not None:
            maison.attic_is_isolated = y["property"]["attic"].get("isIsolated", default)
            maison.attic_surface = y["property"]["attic"].get("surface", default)

        if y["property"].get("basement", default) != default \
                and y["property"].get("basement", default) is not None:
            maison.cellar_surface = y["property"]["basement"].get("surface", default)

        maison.nbr_bathrooms = y["property"].get("bathroomCount", default)
        maison.nbr_bedrooms = y["property"].get("bedroomCount", default)

        if y["property"].get("building", default) != default and y["property"].get("building", default) is not None:
            maison.annex_count = y["property"]["building"].get("annexCount", default)
            maison.state_of_the_building = y["property"]["building"].get("condition", default)
            maison.construction_year = y["property"]["building"].get("constructionYear", default)
            maison.nbr_facades = y["property"]["building"].get("facadeCount", default)
            maison.nbr_floor = y["property"]["building"].get("floorCount", default)
            maison.street_facade_width = y["property"]["building"].get("streetFacadeWidth", default)

        if y["property"].get("constructionPermit", default) != default:
            maison.flood_zone = y["property"]["constructionPermit"].get("floodZoneType", default)

        if y["property"].get("energy", default) != default and y["property"].get("energy", default) is not None:
            maison.double_glazing = y["property"]["energy"].get("hasDoubleGlazing", default)
            maison.has_heat_pump = y["property"]["energy"].get("hasHeatPump", default)
            maison.has_photovoltaic_panels = y["property"]["energy"].get("hasPhotovoltaicPanels", default)
            maison.has_thermic_panels = y["property"]["energy"].get("hasThermicPanels", default)
            maison.heating_type = y["property"]["energy"].get("heatingType", default)

        maison.fire_place_count = y["property"].get("fireplaceCount", default)
        maison.fire_place_exists = y["property"].get("fireplaceExists", default)
        maison.garden_orientation = y["property"].get("gardenOrientation", default)
        maison.garden_area = y["property"].get("gardenSurface", default)
        maison.habitable_unit_count = y["property"].get("habitableUnitCount", default)
        maison.has_air_conditioning = y["property"].get("hasAirConditioning", default)
        maison.has_armored_door = y["property"].get("hasArmoredDoor", default)
        maison.has_balcony = y["property"].get("hasBalcony", default)
        maison.has_barbecue = y["property"].get("hasBarbecue", default)
        maison.has_desabled_access = y["property"].get("hasDisabledAccess", default)
        maison.has_door_phone = y["property"].get("hasDoorPhone", default)
        maison.has_dressing_room = y["property"].get("hasDressingRoom", default)
        maison.has_fitness_room = y["property"].get("hasFitnessRoom", default)
        maison.has_garden = y["property"].get("hasGarden", default)
        maison.has_hammam = y["property"].get("hasHammam", default)
        maison.has_internet = y["property"].get("hasInternet", default)
        maison.has_jacuzzi = y["property"].get("hasJacuzzi", default)
        maison.has_laundry_room = y["property"].get("hasLaundryRoom", default)
        maison.has_lift = y["property"].get("hasLift", default)
        maison.has_sauna = y["property"].get("hasSauna", default)
        maison.has_alarm = y["property"].get("hasSecureAccessAlarm", default)
        maison.has_swimming_pool = y["property"].get("hasSwimmingPool", default)
        maison.has_tv_cable = y["property"].get("hasTVCable", default)
        maison.has_tennis_court = y["property"].get("hasTennisCourt", default)
        maison.terrace = y["property"].get("hasTerrace", default)
        maison.has_visiophone = y["property"].get("hasVisiophone", default)
        maison.is_first_occupation = y["property"].get("isFirstOccupation", default)
        maison.is_holiday_property = y["property"].get("isHolidayProperty", default)

        if y["property"].get("kitchen", default) != default and y["property"].get("kitchen", default) is not None:
            maison.kitchen_has_dishwasher = y["property"]["kitchen"].get("hasDishwasher", default)
            maison.kitchen_has_freezer = y["property"]["kitchen"].get("hasFreezer", default)
            maison.kitchen_has_fridge = y["property"]["kitchen"].get("hasFridge", default)
            maison.kitchen_has_micro_wave_oven = y["property"]["kitchen"].get("hasMicroWaveOven", default)
            maison.kitchen_has_oven = y["property"]["kitchen"].get("hasOven", default)
            maison.kitchen_has_steam_oven = y["property"]["kitchen"].get("hasSteamOven", default)
            maison.kitchen_has_washing_machine = y["property"]["kitchen"].get("hasWashingMachine", default)
            maison.kitchen_surface = y["property"]["kitchen"].get("surface", default)
            maison.kitchen_type = y["property"]["kitchen"].get("type", default)

        if y["property"].get("land", default) != default and y["property"].get("land", default) is not None:
            maison.land_has_plot_to_rear = y["property"]["land"].get("hasPlotToRear", default)
            maison.land_is_facing_street = y["property"]["land"].get("isFacingStreet", default)
            maison.land_is_flat = y["property"]["land"].get("isFlat", default)
            maison.land_is_wooded = y["property"]["land"].get("isWooded", default)
            maison.land_width = y["property"]["land"].get("landWidth", default)
            maison.land_latest_use_designation = y["property"]["land"].get("latestUseDesignation", default)
            maison.land_rear_land = y["property"]["land"].get("rearLand", default)
            maison.sewer_network = y["property"]["land"].get("sewerConnection", default)
            maison.surface_of_the_land = y["property"]["land"].get("surface", default)

        maison.has_laundry_room = y["property"].get("laundryRoom", default)

        if y["property"].get("livingRoom", default) != default and y["property"].get("livingRoom", default) is not None:
            maison.living_room_surface = y["property"]["livingRoom"].get("surface", default)

        if y["property"].get("location", default) != default:
            maison.house_box = y["property"]["location"].get("box", default)
            maison.country = y["property"]["location"].get("country", default)
            maison.district = y["property"]["location"].get("district", default)
            maison.floor = y["property"]["location"].get("floor", default)
            maison.has_sea_view = y["property"]["location"].get("hasSeaView", default)
            maison.latitude = y["property"]["location"].get("latitude", default)
            maison.longitude = y["property"]["location"].get("longitude", default)
            maison.locality = y["property"]["location"].get("locality", default)
            maison.house_number = y["property"]["location"].get("number", default)
            maison.place_name = y["property"]["location"].get("placeName", default)
            maison.postal_code = y["property"]["location"].get("postalCode", default)
            maison.property_name = y["property"]["location"].get("propertyName", default)
            maison.province = y["property"]["location"].get("province", default)
            maison.region = y["property"]["location"].get("region", default)
            maison.region_code = y["property"]["location"].get("regionCode", default)
            maison.street_name = y["property"]["location"].get("street", default)

        maison.net_habitable_surface = y["property"].get("netHabitableSurface", default)
        maison.covered_parking_spaces = y["property"].get("parkingCountIndoor", default)
        maison.outdoor_parking_spaces = y["property"].get("parkingCountOutdoor", default)
        maison.room_count = y["property"].get("roomCount", default)
        maison.nbr_shower = y["property"].get("showerRoomCount", default)
        maison.subtype_of_property = y["property"].get("subtype", default)
        maison.terrace_orientation = y["property"].get("terraceOrientation", default)
        maison.terrace_area = y["property"].get("terraceSurface", default)
        maison.nbr_toilet = y["property"].get("toiletCount", default)
        maison.type_of_property = y["property"].get("type", default)

    if y.get("publication", default) != default:
        maison.immoweb_creation_date = y["publication"].get("creationDate", default)
        maison.immoweb_expiration_date = y["publication"].get("expirationDate", default)
        maison.immoweb_last_modification_date = y["publication"].get("lastModificationDate", default)

    if y.get("transaction", default) != default:
        maison.available_date = y["transaction"].get("availabilityDate", default)

        if y["transaction"].get("certificates", default) != default and \
                y["transaction"].get("certificates", default) is not None:
            maison.co2_emission = y["transaction"]["certificates"].get("carbonEmission", default)
            maison.energy_class = y["transaction"]["certificates"].get("epcScore", default)
            maison.energy_consumption = y["transaction"]["certificates"].get("primaryEnergyConsumptionPerSqm",
                                                                             default)

        if y["transaction"].get("sale", default) != default:
            maison.cadastral_income = y["transaction"]["sale"].get("cadastralIncome", default)
            maison.has_starting_price = y["transaction"]["sale"].get("hasStartingPrice", default)
            maison.is_furnished = y["transaction"]["sale"].get("isFurnished", default)
            maison.public_sale = y["transaction"]["sale"].get("publicSale", default)
            maison.vat_type = y["transaction"]["sale"].get("vatType", default)

        maison.price_type = y["transaction"].get("subtype", default)

    if debug:
        print("***************************************************************************")
        print(pprint.pprint(vars(maison)))

    return maison