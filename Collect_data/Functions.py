import re
import requests
import lxml.html as lh
import pprint
from bs4 import BeautifulSoup
import json
import Data


# pour afficher ce qui se passe lors du dev

debug = True


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
        if debug:
            print("la page n'est pas accessible")
            print(dico)

    else:
        maison.available_date = dico.get("Available date", "Not found")
        maison.property_name = dico.get("Property name", "Not found")
        maison.neighbourhood = dico.get("Neighbourhood or locality", "Not found")
        maison.construction_year = dico.get("Construction year", "Not found")
        maison.floor = dico.get("Floor", "Not found")
        maison.nbr_floor = dico.get("Number of floors", "Not found")
        maison.state_of_the_building = dico.get("Building condition", "Not found")
        maison.street_facade_width = dico.get("Street facade width", "Not found")
        maison.nbr_facades = dico.get("Facades", "Not found")
        maison.covered_parking_spaces = dico.get("Covered parking spaces", "Not found")
        maison.outdoor_parking_spaces = dico.get("Outdoor parking spaces", "Not found")
        maison.house_area = dico.get("Living area", "Not found")
        maison.living_room_surface = dico.get("Living room surface", "Not found")
        maison.kitchen_type = dico.get("Kitchen type", "Not found")
        maison.nbr_bedrooms = dico.get("Bedrooms", "Not found")
        maison.bedroom_1_surface = dico.get("Bedroom 1 surface", "Not found")
        maison.bedroom_2_surface = dico.get("Bedroom 2 surface", "Not found")
        maison.bedroom_3_surface = dico.get("Bedroom 3 surface", "Not found")
        maison.bedroom_4_surface = dico.get("Bedroom 4 surface", "Not found")
        maison.bedroom_5_surface = dico.get("Bedroom 5 surface", "Not found")
        maison.nbr_bathrooms = dico.get("Bathrooms", "Not found")
        maison.nbr_shower = dico.get("Shower rooms", "Not found")
        maison.nbr_toilet = dico.get("Toilets", "Not found")
        maison.office_surface = dico.get("Office surface", "Not found")
        maison.office = dico.get("Office", "Not found")
        maison.work_space_surface = dico.get("Work space surface", "Not found")
        maison.cellar = dico.get("Basement", "Not found")
        maison.attic = dico.get("Attic", "Not found")
        maison.surface_of_the_land = dico.get("Surface of the plot", "Not found")
        maison.sewer_network = dico.get("Connection to sewer network", "Not found")
        maison.terrace_area = dico.get("Terrace surface", "Not found")
        maison.energy_consumption = dico.get("Primary energy consumption", "Not found")
        maison.energy_class = dico.get("Energy class", "Not found")
        maison.co2_emission = dico.get("CO² emission", "Not found")
        maison.heating_type = dico.get("Heating type", "Not found")
        maison.solar_panels = dico.get("Thermic solar panels", "Not found")
        maison.double_glazing = dico.get("Double glazing", "Not found")
        maison.flood_zone = dico.get("Flood zone type", "Not found")
        maison.price = dico.get("Price", "Not found")
        maison.cadastral_income = dico.get("Cadastral income", "Not found")
        maison.agent = dico.get("Website", "Not found")

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
            if vars(maison)[i] == "Not found":
                del remove_not_found[i]

        pprint.pprint(remove_not_found)

def recuperer_data_research_page(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    result = soup.find_all('div')

    data = json.loads(soup.find('iw-search')[':results'])

    return data

def collect_data_research_page(data):
    if debug:
        for d in data:
            print(d)

            url = 'https://www.immoweb.be/en/classified/{}'.format(d['id'])

            print(url)

    for d in data:

        maison = Data.estate()

        maison.immoweb_id = d.get("id", "Not found")

        if d.get("cluster", "Not found") != "Not found":
            maison.min_price = d["cluster"].get("minPrice", "Not found")
            maison.max_price = d["cluster"].get("maxPrice", "Not found")
            maison.min_room = d["cluster"].get("minRoom", "Not found")
            maison.max_room = d["cluster"].get("maxRoom", "Not found")
            maison.min_surface = d["cluster"].get("minSurface", "Not found")
            maison.max_surface = d["cluster"].get("maxSurface", "Not found")

            if d["cluster"].get("projectInfo", "Not found") != "Not found" \
                    and d["cluster"].get("projectInfo", "Not found") is not None:
                maison.constructor = d["cluster"]["projectInfo"].get("constructor", "Not found")
                maison.groupId = d["cluster"]["projectInfo"].get("groupId", "Not found")
                maison.phase = d["cluster"]["projectInfo"].get("phase", "Not found")
                maison.project_name = d["cluster"]["projectInfo"].get("projectName", "Not found")
                maison.delivery_date = d["cluster"]["projectInfo"].get("deliveryDate", "Not found")
                maison.sold_percentage = d["cluster"]["projectInfo"].get("soldPercentage", "Not found")
                maison.units_display_mode = d["cluster"]["projectInfo"].get("unitsDisplayMode", "Not found")

        maison.bedroom_range = d.get("bedroomRange", "Not found")
        maison.surface_range = d.get("surfaceRange", "Not found")
        maison.customer_name = d.get("customerName", "Not found")

        if d.get("property", "Not found") != "Not found":
            maison.type_of_property = d["property"].get("type", "Not found")
            maison.subtype_of_property = d["property"].get("subtype", "Not found")
            maison.nbr_bedrooms = d["property"].get("bedroomCount", "Not found")
            maison.title = d["property"].get("title", "Not found")

            if d["property"].get("location", "Not found") != "Not found" \
                    and d["property"].get("location", "Not found") is not None:
                maison.country = d["property"]["location"].get("country", "Not found")
                maison.region = d["property"]["location"].get("region", "Not found")
                maison.province = d["property"]["location"].get("province", "Not found")
                maison.district = d["property"]["location"].get("district", "Not found")
                maison.locality = d["property"]["location"].get("postalCode", "Not found")
                maison.postal_code = d["property"]["location"].get("postalCode", "Not found")
                maison.street_name = d["property"]["location"].get("street", "Not found")
                maison.house_number = d["property"]["location"].get("number", "Not found")
                maison.house_box = d["property"]["location"].get("box", "Not found")
                maison.property_name = d["property"]["location"].get("propertyName", "Not found")
                maison.floor = d["property"]["location"].get("floor", "Not found")
                maison.latitude = d["property"]["location"].get("latitude", "Not found")
                maison.longitude = d["property"]["location"].get("longitude", "Not found")
                maison.approximated = d["property"]["location"].get("approximated", "Not found")
                maison.region_code = d["property"]["location"].get("regionCode", "Not found")
                maison.type = d["property"]["location"].get("type", "Not found")
                maison.has_sea_view = d["property"]["location"].get("hasSeaView", "Not found")
                maison.points_of_interest = d["property"]["location"].get("pointsOfInterest", "Not found")
                maison.place_name = d["property"]["location"].get("placeName", "Not found")

            maison.net_habitable_surface = d["property"].get("netHabitableSurface", "Not found")
            maison.room_count = d["property"].get("roomCount", "Not found")
            maison.surface_of_the_land = d["property"].get("landSurface", "Not found")

        if d.get("transaction", "Not found") != "not found":
            maison.certificate = d["transaction"].get("certificate", "Not found")
            maison.type_of_sale = d["transaction"].get("type", "Not found")
            maison.rental = d["transaction"].get("rental", "Not found")

            if d["transaction"].get("sale", "Not found") != "Not found" \
                    and d["transaction"].get("sale", "Not found") is not None:
                maison.life_annuity = d["transaction"]["sale"].get("lifeAnnuity", "Not found")
                maison.has_starting_price = d["transaction"]["sale"].get("hasStartingPrice", "Not found")
                maison.old_price = d["transaction"]["sale"].get("oldPrice", "Not found")
                maison.price = d["transaction"]["sale"].get("price", "Not found")
                maison.price_per_sqm = d["transaction"]["sale"].get("pricePerSqm", "Not found")
                maison.public_sale = d["transaction"]["sale"].get("publicSale", "Not found")
                maison.to_build = d["transaction"]["sale"].get("toBuild", "Not found")
                maison.vat_type = d["transaction"]["sale"].get("vatType", "Not found")

        maison.price_type = d.get("priceType", "Not found")
        maison.has_360_tour = d.get("has360Tour", "Not found")

        if debug:

            print("+++++++++++++++++++++++++++++++++++++++++++++++++")

            remove_not_found = vars(maison).copy()
            for i in vars(maison):
                if vars(maison)[i] == "Not found" or vars(maison)[i] is None:
                    del remove_not_found[i]

            pprint.pprint(remove_not_found)
            """for f in d:
                 pprint.pprint(d[f])"""